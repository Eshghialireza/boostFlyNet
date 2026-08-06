from telegram.ext import Application, CommandHandler
import config
from database.db import init_db
from handlers.start import start

# Initialize the database
init_db()

def main():
    # Build the application
    app = Application.builder().token(config.TOKEN).build()
    
    # Adding the start command handler
    app.add_handler(CommandHandler("start", start))
    
    print("Application started...")
    app.run_polling()

if __name__ == "__main__":
    main()