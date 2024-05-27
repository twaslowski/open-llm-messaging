import base64
import logging
import os

import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, Application
from telegram.ext import filters as Filters

from openllm_messaging.shared.model_message import ModelMessage


class TelegramBot:
    def __init__(self, llm_backend: str):
        self.llm_backend = llm_backend
        self.app = self.initialize_application()

    def initialize_application(self) -> Application:
        token = os.environ.get("TELEGRAM_TOKEN")
        app = ApplicationBuilder().token(token).build()
        app.add_handler(
            MessageHandler(filters=Filters.PHOTO, callback=self.handle_image)
        )
        app.add_handler(MessageHandler(filters=None, callback=self.handle_text))
        logging.info("Starting application ...")
        return app

    def start(self):
        self.app.run_polling()

    async def handle_text(self, update, _):
        backend_response = requests.post(
            f"{self.llm_backend}/text", json={"prompt": update.message.text}
        )
        message = ModelMessage(**backend_response.json())
        await update.message.reply_text(self.format_response(message))

    async def handle_image(self, update, _):
        """
        Handles receiving exactly one image.
        :param update: Telegram Update object.
        :param _: CallbackContext. Unused.
        :return:
        """
        path = await self._download_image(update)
        with open(path, "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode("utf-8")
            backend_response = requests.post(
                f"{self.llm_backend}/image", json={"image": image_data}
            )
            message = ModelMessage(**backend_response.json())
            await update.message.reply_text(self.format_response(message))

    @staticmethod
    async def _download_image(update: Update) -> str:
        """
        Downloads an image from a Telegram chat. Returns a local file path.
        :param update: Telegram Update object containing the image id.
        :return:
        """
        photo = update.message.photo[-1]
        logging.info(
            f"Received image from {update.effective_user.id}: {update.message.photo[-1].file_id}"
        )
        image = await photo.get_file()
        filename = f"tmp/{update.effective_user.id}_{photo.file_id}.jpeg"
        await image.download_to_drive(filename)
        return filename

    @staticmethod
    def format_response(message: ModelMessage) -> str:
        return f"{message.content}\n\n*This message used {message.tokens} tokens.*"
