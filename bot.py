from telegram.ext import Application, CommandHandler, CallbackQueryHandler
import config
from database.db import init_db
from handlers.start import start
from handlers.menu import menu_handler

# Initialize the database
init_db()

def main():
    # Build the application
    app = Application.builder().token(config.TOKEN).build()
    
    # Adding the start command handler
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(menu_handler))
    
    print("Application started...")
    app.run_polling()

if __name__ == "__main__":
    main()