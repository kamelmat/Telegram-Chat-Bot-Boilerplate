import logging
from functools import wraps
from telegram import Update

logger = logging.getLogger(__name__)

def log_command(func):
    @wraps(func)
    async def wrapper(update: Update, context):
        user = update.effective_user
        logger.info(f"User {user.id} used command /{func.__name__}")
        return await func(update, context)
    return wrapper
