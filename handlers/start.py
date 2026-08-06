from telegram import Update
from database.user_dao import register_user
from telegram.ext import ContextTypes
from utils.translator import default as defaultLanguage

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    register_user(user.id, user.username, user.full_name)
    
    welcome_text = defaultLanguage.get('welcome')
    
    await update.message.reply_text(welcome_text)


