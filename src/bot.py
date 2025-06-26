import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from googletrans import Translator, LANGUAGES

TOKEN = "TELEGRAM TOKEN, from @BotFather"
translator = Translator()

# -----------------------------------------------------------------------------
# Logging settings
logger = logging.getLogger(__name__)
logging.basicConfig(
    format ='%(actime)s - %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO,
    handlers = [
        logging.FileHandler("translation_bot_INFO.log"),
        logging.StreamHandler()
    ]
)

# -----------------------------------------------------------------------------
# Bot Commands

def start() -> None:
    user = Update.effective_user
    logger.info(f"User {user.id} start conversation")

    Update.message.reply_text(f"Hi {user.first_name}! I am LinguaSpark Bot...")

def help_command(Update, context: CallbackContext) -> None:
    help_text = """
        XD *Help For LinguaSpark Bot :P 
    """
    Update.message.reply_text(help_text, parse_mode="Markdown")

def lang_command() -> None:
    pass

def lang_callback() -> None:
    pass

def info_command() -> None:
    pass

