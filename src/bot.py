#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Telegram Translation Bot
🤖 LinguaSpark 🤖
---------------------------
Version: 1.0
Author: Jean Estevez
Github https://github.com/Jean-EstevezT
Description: Real-time text translation using Google Translate API

Features:
🌍 Supports 100+ languages
⚡ Instant translation of any text
🔄 Interactive language selection
📊 User-specific language preferences

Usage:
1. Start the bot with /start
2. Send any text to get automatic translation
3. Use /lang to change target language
4. Use /info to check current settings

Requirements:
- python-telegram-bot
- googletrans==4.0.0-rc1

Note: Replace 'TELEGRAM TOKEN, from @BotFather' with your actual Telegram bot token
---------------------------------------------------------------
"""

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext, CallbackQueryHandler
from googletrans import Translator, LANGUAGES

TOKEN = "TELEGRAM TOKEN, from @BotFather"

# initialize translator
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
    # /start command
    user = Update.effective_user
    logger.info(f"User {user.id} start conversation")

    Update.message.reply_text(
        f""" Hi *{user.first_name}!* I am *LinguaSpark* Bot\n\n
        - Send me any text and I'll translate it automatically\n
        - Use */lang* to change the target language(default: English)\n
        - */help* for assistence
        """)

def help_command(update: Update, context: CallbackContext) -> None:
    # /help command
    help_text = """
        XD *Help* For LinguaSpark Bot :P

        Available Functions:
        - Just Type text and I will translate it
        - /lang - Change language
        - /info - View current language
        - /help - This help  

        Feautres:
        - Supports +100 languages
        - Instant Translation
        - Interactive Interface

        -----------------------------------------
        Jean Estevez
        https://github.com/Jean-EstevezT

    """
    update.message.reply_text(help_text, parse_mode="Markdown")


def lang_command(update: Update, context: CallbackContext) -> None:
    # /lang command and Lenguage selection
    keyboard = []
    top_langs = ['en', 'es', 'fr', 'fr', 'de', 'it', 'pt', 'ru', 'zh-cn', 'ja']
    lang_list = [(code, LANGUAGES[code]) for code in top_langs]

    for i in range(0, len(lang_list), 3):
        row = [InlineKeyboardButton(lang[1], callback_data=lang[0])
               for lang in lang_list[i:i+3]]
        keyboard.append(row)

    # Button to see all languuages
    keyboard.append([InlineKeyboardButton("All *Languages*", callback_data='show all')])
    
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text("*Select Lenguage*:...", reply_markup=reply_markup, parse_mode="Markdown")
    
    logger.info(f'User {update.effective_user.id} requested lenguage change ;)')


def lang_callback(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    language_code = query.data
    user_id = query.from_user.id

    if language_code == 'show_all':
        # print all languages
        all_languages = '\n'.join([f'{code}: {name}' for code, name in LANGUAGES.items()])
        query.edit_message_text(f"*Available Languages:* \n\n {all_languages} \n\nUse /lang to select", 
                                parse_mode='Markdown')
        
        logger.info(f'User {user_id} requested full language list')

        return
    # Save select language
    context.user_data['target_language'] = language_code
    language_name = LANGUAGES.get(language_code, 'unknown')

    query.edit_message_text(f'New *Language*: {language_name}', parse_mode='Markdown')
    logger.info(f'User {user_id} change lenguage to {language_name} ({language_code})')

def info_command(update: Update, context: CallbackContext) -> None:
    # /info command = show settings
    user_id = update.effective_user.id
    target_language = context.user_data.get('Target Language', 'en')
    language_name = LANGUAGES.get(target_language, 'English')

    update.message.reply_text(f'*Current Settings:*\n\nTarget Language: *{language_name}* {target_language}',
                              parse_mode='Markdown')
    logger.info(f'User {user_id} requested setting info')

def translate_message(update: Update, context: CallbackContext) -> None:
    user_text = update.message.text
    user_id = update.effective_user.id
    
    logger.debug(f'User {user_id} sent text: {user_text}')

    target_language = context.user_data.get('target_language', 'en')

    try:
        translation = translator.translate(user_text, dest=target_language)

        response = (
            f'*Original ({translation.src.upper()}): *\n{user_text}\n\n'
            f'*Translation ({target_language.upper()}): *\n{translation.text}'
        )

        update.message.reply_text(response, parse_mode='Markdown')
        logger.info(f'Successful translation for {user_id}: {translation.src} -> {target_language}')
    except Exception as error:
        error_message = 'Translation ERROR. Please try again'
        update.message.reply_text(error_message)

        logger.error(f'Translation error: {str(error)}', exc_info=True)

def error_handler(update: Update, context: CallbackContext) -> None:
    logger.error(f'Error: {context.error}', exc_info=True)

    if update and update.message:
        update.message.reply_text('An Unexpected error, Please try again.')

def main() -> None:
    # Configure logger
    logger.setLevel(logging.INFO)

    # Create UPDATER with TOKEN
    updater = Updater(TOKEN)
    
    register_commands = updater.dispatcher
    register_commands.add_handler(CommandHandler('start', start))
    register_commands.add_handler(CommandHandler('help', help_command))
    register_commands.add_handler(CommandHandler('lang', lang_command))
    register_commands.add_handler(CommandHandler('info', info_command))

    # handle language selection
    register_commands.add_handler(CallbackQueryHandler(lang_command))

    # handle text messages
    register_commands.add_handler(MessageHandler(filters.text & ~filters.command, translate_message))

    # handle errors
    register_commands.add_error_handler(error_handler)

    # Start BOT
    logger.info('Starting Translation Bot...')
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()