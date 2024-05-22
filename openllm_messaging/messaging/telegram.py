import logging
import os

import requests
from telegram.ext import ApplicationBuilder, MessageHandler, Application

from openllm_messaging.llm.model_message import ModelMessage


class TelegramBot:
    def __init__(self, llm_backend: str):
        self.llm_backend = llm_backend
        self.app = self.initialize_application()

    def initialize_application(self) -> Application:
        token = os.environ.get("TELEGRAM_TOKEN")
        app = ApplicationBuilder().token(token).build()
        app.add_handler(MessageHandler(filters=None, callback=self.handle_text))
        logging.info("Starting application ...")
        return app

    def start(self):
        self.app.run_polling()

    async def handle_text(self, update, _):
        backend_response = requests.post(
            self.llm_backend, json={"prompt": update.message.text}
        )
        message = ModelMessage(**backend_response.json())
        await update.message.reply_text(self.format_response(message))

    @staticmethod
    def format_response(message: ModelMessage) -> str:
        return f"{message.content}\n\n*This message used {message.tokens} tokens.*"
