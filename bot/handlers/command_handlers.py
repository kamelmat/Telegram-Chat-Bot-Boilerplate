from telegram import Update
from telegram.ext import ContextTypes
from bot.utils import log_command

@log_command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello! I am a boilerplate bot.')
