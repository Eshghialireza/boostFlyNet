from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('TOKEN')
ADMIN_ID = int(os.getenv('ADMIN_ID'))
ADMIN_USERNAME = os.getenv('ADMIN_USERNAME')
