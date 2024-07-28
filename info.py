import os
# Bot information
API_ID = os.getenv('API_ID', "10942774")
API_HASH = os.getenv('API_HASH', "eb86f562fb093924264c2b76c308e6ea")
BOT_TOKEN = os.getenv('BOT_TOKEN', "7496729209:AAF9VT5XSnB7xxHcS4sFGKw59S2ziIlp3ew")

# stream vars
PORT = int(os.getenv('PORT', '5050'))
BIN_CHANNEL = os.getenv("BIN_CHANNEL", "-1001782160403") #Log Channel
URL = os.getenv("URL", "") #App URL not MongoDB URL
