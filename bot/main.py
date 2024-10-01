import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from .config import TOKEN  # Updated import statement
from .handlers.message_handlers import echo
from .handlers.command_handlers import start
from .handlers.error_handlers import error_handler

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='bot.log'
)
logger = logging.getLogger(__name__)

def main() -> None:
    # Create the Application and pass it your bot's token
    application = Application.builder().token(TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Add error handler
    application.add_error_handler(error_handler)

    logger.info("Bot started")

    # Run the bot until the user presses Ctrl-C
    application.run_polling()

    logger.info("Bot stopped")

if __name__ == '__main__':
    main()
