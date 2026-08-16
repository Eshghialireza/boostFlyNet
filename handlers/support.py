from telegram import Update,InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import ContextTypes
import config
from utils.translator import default as defaultLanguage

async def support_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    admin_username = config.ADMIN_USERNAME
    keyboard = [
        [InlineKeyboardButton(defaultLanguage.get("back"), callback_data="back_main")]
        ]
    await query.edit_message_text(
        text=defaultLanguage.get("support_message").format(admin_username=admin_username),
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode='HTML'
    )