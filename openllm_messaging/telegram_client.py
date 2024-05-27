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
    flask_backend = "http://localhost:5000/text"
    telegram_bot = TelegramBot(flask_backend)
    telegram_bot.start()
