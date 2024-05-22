import logging
import os

import click
from telegram.ext import ApplicationBuilder, MessageHandler

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


@click.command()
def run():
    """
    Run Telegram bot.
    """
    token = os.environ.get("TELEGRAM_TOKEN")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(MessageHandler(filters=None, callback=handle_text))
    logging.info("Starting application ...")
    app.run_polling()


async def handle_text(update, _):
    print(update.message.text)
    await update.message.reply_text("Hello!")
