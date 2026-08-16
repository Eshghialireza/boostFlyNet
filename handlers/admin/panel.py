from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from utils.translator import default as defaultLanguage
from database.category_dao import list_categories

async def show_admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query= update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton(defaultLanguage.get("manage_categories"),callback_data="manage_categories")],
        [InlineKeyboardButton(defaultLanguage.get("back_main"),callback_data="back_main")]
    ]
    await query.edit_message_text(
        defaultLanguage.get("admin_panel"),
        reply_markup=InlineKeyboardMarkup(keyboard))
    
async def manage_categories(update: Update,context: ContextTypes.DEFAULT_TYPE):
    query= update.callback_query
    await query.answer()
    categories = list_categories()
    keyboard = []
    header_row = [
        InlineKeyboardButton(defaultLanguage.get("name"), callback_data="ignore"),
        InlineKeyboardButton(defaultLanguage.get("status"), callback_data="ignore"),
        InlineKeyboardButton(defaultLanguage.get("delete"), callback_data="ignore")
    ]
    keyboard.append(header_row)
    keyboard.append([InlineKeyboardButton(" ", callback_data="ignore")])
    for category in categories:
        row = [
            InlineKeyboardButton(category["name"], callback_data=f"category_{category['id']}"),
            InlineKeyboardButton(defaultLanguage.get("active_icon") if category["is_active"] else defaultLanguage.get("inactive_icon"), callback_data=f"toggle_status_{category['id']}"),
            InlineKeyboardButton(defaultLanguage.get("delete_icon"), callback_data=f"delete_category_{category['id']}")
        ]
        keyboard.append(row)
    
    row = [
        InlineKeyboardButton(defaultLanguage.get("add_category"), callback_data="add_category"),
        InlineKeyboardButton(defaultLanguage.get("back_main"), callback_data="admin_panel")
    ]
    keyboard.append(row)
    await query.edit_message_text(defaultLanguage.get("admin_panel"),
    reply_markup=InlineKeyboardMarkup(keyboard))
    
async def add_category(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(defaultLanguage.get("add_category_prompt"))
    return "WAITING_FOR_CATEGORY_NAME"