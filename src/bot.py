import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from googletrans import Translator, LANGUAGES

TOKEN = "TELEGRAM TOKEN, from @BotFather"

# -----------------------------------------------------------------------------
# Logging settings
logger = logging.getLogger(__name__)


def start() -> None:
    user = Update.effective_user
    Update.message.reply_text(f"Hi {user.first_name}! I am LinguaSpark Bot...")
