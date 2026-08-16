from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
import config
from utils.translator import default as defaultLanguage


async def show_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # show menu
    query = update.callback_query
    await query.answer()
    
    keyboard = [
        [InlineKeyboardButton(defaultLanguage.get("buy"), callback_data="buy")],
        [InlineKeyboardButton(defaultLanguage.get("my_products"), callback_data="my_products")],
        [InlineKeyboardButton(defaultLanguage.get("support"), callback_data="support")],
    ]
    
    # add admin panel button
    if update.effective_user.id == config.ADMIN_ID:
        keyboard.append([InlineKeyboardButton(defaultLanguage.get("admin_panel"), callback_data="admin_panel")])
    
    await query.edit_message_text(
        defaultLanguage.get("main_menu_message"),
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    query = update.callback_query
    await query.answer()
    
    data = query.data
    
    # Main menu
    if data == "main_menu":
        await show_main_menu(update, context)
    
    elif data == "back_main":
        await show_main_menu(update, context)
        
    elif data == "ignore":
        await query.answer()
        return
    
    elif data == "support":
        from handlers.support import support_message
        admin_username = config.ADMIN_USERNAME
        await support_message(update, context)
    
    # Admin panel
    elif data == "admin_panel":
        from handlers.admin.panel import show_admin_panel
        await show_admin_panel(update, context)
        
    elif data == "manage_categories":
        from handlers.admin.panel import manage_categories
        await manage_categories(update, context)
    
    # default case
    else:
        keyboard = [
        [InlineKeyboardButton(defaultLanguage.get("back"), callback_data="back_main")],
    ]
        await query.edit_message_text(
            defaultLanguage.get("unknown_command"),
            reply_markup=InlineKeyboardMarkup(keyboard)
        )