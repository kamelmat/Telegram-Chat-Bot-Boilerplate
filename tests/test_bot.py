import pytest
from telegram import Update
from telegram.ext import ContextTypes
from bot.handlers.message_handlers import start, echo

@pytest.mark.asyncio
async def test_start_command():
    update = Update(1, message={"message_id": 1, "date": 1, "chat": {"id": 1, "type": "private"}, "text": "/start"})
    context = ContextTypes.DEFAULT_TYPE()
    
    await start(update, context)
    
    assert update.message.reply_text.call_count == 1
    assert update.message.reply_text.call_args[0][0] == 'Hello! I am a boilerplate bot.'

@pytest.mark.asyncio
async def test_echo():
    update = Update(1, message={"message_id": 1, "date": 1, "chat": {"id": 1, "type": "private"}, "text": "Test message"})
    context = ContextTypes.DEFAULT_TYPE()
    
    await echo(update, context)
    
    assert update.message.reply_text.call_count == 1
    assert update.message.reply_text.call_args[0][0] == 'Test message'
