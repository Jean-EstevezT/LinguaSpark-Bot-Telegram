#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Telegram Translation Bot
🤖 LinguaTranslateSpark 🤖

t.me/LinguaTranslateSparkBot
---------------------------
Version: 1.0
Author: Jean Estevez
X: @jeantvz
Github: https://github.com/Jean-EstevezT
Description: Real-time text translation using deep-translator

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
- deep-translator

Note: Replace 'TELEGRAM TOKEN, from @BotFather' with your actual Telegram bot token
---------------------------------------------------------------
"""

import logging
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackContext,
    CallbackQueryHandler
)
from deep_translator import GoogleTranslator

TOKEN = "TELEGRAM TOKEN, from @BotFather"
LANGUAGES = {
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'it': 'Italian',
    'pt': 'Portuguese',
    'ru': 'Russian',
    'zh': 'Chinese',
    'ja': 'Japanese'
    # You can add more
}

# -----------------------------------------------------------------------------
# Logging settings
logger = logging.getLogger(__name__)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO,
    handlers = [
        logging.FileHandler("translation_bot_INFO.log"),
        logging.StreamHandler()
    ]
)

# -----------------------------------------------------------------------------
# Bot Commands

async def start(update: Update, context: CallbackContext) -> None:
    # /start command
    user = update.effective_user

    welcome_text = (
        f"Hello <b>{user.first_name}</b>! I'm <b>LinguaSpark Bot</b> 🌍\n\n"
        "Send me any text and I’ll translate it instantly.\n\n"
        "Use the buttons below to access features:"
    )

    keyboard = [
        [InlineKeyboardButton("🌐 Change Language", callback_data='command_lang')],
        [InlineKeyboardButton("ℹ️ Info", callback_data='command_info')],
        [InlineKeyboardButton("❓ Help", callback_data='command_help')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        welcome_text,
        parse_mode="HTML",
        reply_markup=reply_markup
    )

async def send_lang_menu(query, context):
    keyboard = []
    lang_list = list(LANGUAGES.items())

    for i in range(0, len(lang_list), 3):
        row = [InlineKeyboardButton(name, callback_data=code)
               for code, name in lang_list[i:i + 3]]
        keyboard.append(row)

    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        "Please select your target language:",
        reply_markup=reply_markup,
        parse_mode="HTML"
    )

async def send_info_message(query, context):
    target_language = context.user_data.get('target_language', 'en')
    language_name = LANGUAGES.get(target_language, 'English')

    await query.edit_message_text(
        f"<b>Current Settings:</b>\nTarget Language: <b>{language_name}</b> ({target_language})",
        parse_mode="HTML"
    )

async def send_help_message(query, context):
    help_text = """
    <b>📘 Help — LinguaSpark Bot</b>

    <b>Available Commands:</b>
    <code>/lang</code> – Change target language  
    <code>/info</code> – Show current settings  
    <code>/help</code> – Display this help message  

    <b>Features:</b>
    – Supports 100+ languages  
    – Instant translation  
    – User-specific preferences  
    – Interactive interface  

    <b>👤 Author:</b> Jean Estevez
    """
    await query.edit_message_text(help_text, parse_mode="HTML")

async def start_menu_callback(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'command_lang':
        await send_lang_menu(query, context)
    elif query.data == 'command_info':
        await send_info_message(query, context)
    elif query.data == 'command_help':
        await send_help_message(query, context)


async def help_command(update: Update, context: CallbackContext) -> None:
    # /help command
    help_text = """
    <b> Help — LinguaSpark Bot</b>

    <b>Available Commands:</b>
    <code>/lang</code> – Change target language  
    <code>/info</code> – Show current settings  
    <code>/help</code> – Display this help message  

    <b>Features:</b>
    – Supports 100+ languages  
    – Instant translation  
    – User-specific preferences  
    – Interactive interface  

    <b>👤 Author:</b> Jean Estevez
    """
    await update.message.reply_text(help_text, parse_mode="HTML")
    logger.info(f"User {update.effective_user.id} requested help")

async def lang_command(update: Update, context: CallbackContext) -> None:
    # /lang command and Lenguage selection
    keyboard = []
    lang_list = list(LANGUAGES.items())

    for i in range(0, len(lang_list), 3):
        row = [InlineKeyboardButton(lang[1], callback_data=lang[0])
               for lang in lang_list[i:i+3]]
        keyboard.append(row)

    # Button to see all languuages
    keyboard.append([InlineKeyboardButton("All Languages", callback_data='show all')])
    
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Please select your target language:",
                                reply_markup=reply_markup,
                                parse_mode="HTML")

    logger.info(f'User {update.effective_user.id} requested lenguage change ;)')


async def lang_callback(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    language_code = query.data
    user_id = query.from_user.id

    context.user_data['target_language'] = language_code
    language_name = LANGUAGES.get(language_code, 'Unknown')

    await query.edit_message_text(f"Target language changed to: <b>{language_name}</b>",
                                  parse_mode="HTML")
    logger.info(f'User {user_id} set language to {language_name} ({language_code})')

async def info_command(update: Update, context: CallbackContext) -> None:
    # /info command = show settings
    user_id = update.effective_user.id
    target_language = context.user_data.get('target_language', 'en')
    language_name = LANGUAGES.get(target_language, 'English')

    await update.message.reply_text(
        f"<b>Current Settings:</b>\nTarget Language: <b>{language_name}</b> ({target_language})",
        parse_mode="HTML"
    )
    logger.info(f'User {user_id} requested settings info')

async def translate_message(update: Update, context: CallbackContext) -> None:
    user_text = update.message.text
    user_id = update.effective_user.id
    
    logger.debug(f'User {user_id} sent text: {user_text}')

    target_language = context.user_data.get('target_language', 'en')

    try:
        loop = asyncio.get_running_loop()
        translated_text = await loop.run_in_executor(
            None,
            lambda: GoogleTranslator(target=target_language).translate(user_text)
        )

        response = (
            f"<b>Original:</b>\n{user_text}\n\n"
            f"<b>Translation ({target_language.upper()}):</b>\n{translated_text}"
        )

        await update.message.reply_text(response, parse_mode="HTML")
        logger.info(f'Successful translation for {user_id} to {target_language}')
    
    except Exception as error:
        error_message = 'Translation error. Please try again.'
        await update.message.reply_text(error_message)
        logger.error(f'Translation error: {str(error)}', exc_info=True)

async def error_handler(update: Update, context: CallbackContext) -> None:
    logger.error(f'Error: {context.error}', exc_info=True)

    try:
        if update and update.message:
            await update.message.reply_text('An unexpected error occurred. Please try again.')
    except Exception as e:
        logger.error(f"Error in error handler: {e}")

def main() -> None:
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CallbackQueryHandler(start_menu_callback, pattern='^command_'))

    # Register commands
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('lang', lang_command))
    application.add_handler(CommandHandler('info', info_command))

    # Handle language selection
    application.add_handler(CallbackQueryHandler(lang_callback))

    # Handle text messages
    application.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, 
        translate_message
    ))

    # Handle errors
    application.add_error_handler(error_handler)

    # Start BOT
    logger.info('Starting Translation Bot...')
    application.run_polling()

if __name__ == '__main__':
    main()