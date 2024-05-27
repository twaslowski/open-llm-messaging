import logging

import click
from openllm_messaging.messaging.telegram_client import TelegramBot

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


@click.command()
def run():
    """
    Run Telegram bot.
    """
    llm_backend = "http://openai-server:5001"
    telegram_bot = TelegramBot(llm_backend)
    telegram_bot.start()
