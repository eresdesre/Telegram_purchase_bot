import os
from dotenv import load_dotenv
# Importing the emoji module for displaying emojis
from emoji import emojize


load_dotenv()  # Loading variables from the .env file.

# The token is issued during application registration.
TOKEN = os.getenv('TOKEN')

# DEBUG = True

# The name of the database
NAME_DB = os.getenv('NAME_DB')

# The application version
VERSION = os.getenv('VERSION')

# The author of the application
AUTHOR = os.getenv('AUTHOR')

# The parent directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# The path to the database
DATABASE = os.path.join('sqlite:///'+BASE_DIR, NAME_DB)

COUNT = 0

# Control buttons
KEYBOARD = {
    'CHOOSE_GOODS': emojize(':open_file_folder: Select a product'),
    'INFO': emojize(':speech_balloon: About the store'),
    'SETTINGS': emojize('⚙️ Настройки'),
    'SEMIPRODUCT': emojize(':pizza: fullz'),
    'GROCERY': emojize(':bread: leads'),
    'ICE_CREAM': emojize(':shaved_ice: live CC'),
    '<<': emojize('⏪'),
    '>>': emojize('⏩'),
    'BACK_STEP': emojize('◀️'),
    'NEXT_STEP': emojize('▶️'),
    'ORDER': emojize('✅ ORDER'),
    'X': emojize('❌'),
    'DOWN': emojize('🔽'),
    'AMOUNT_PRODUCT': COUNT,
    'AMOUNT_ORDERS': COUNT,
    'UP': emojize('🔼'),
    'APPLAY': '✅ place an order',
    'COPY': '©️'
}

# The IDs of product categories
CATEGORY = {
    'SEMIPRODUCT': 1,
    'GROCERY': 2,
    'ICE_CREAM': 3,
}

# The names of commands
COMMANDS = {
    'START': "start",
    'HELP': "help",
}
