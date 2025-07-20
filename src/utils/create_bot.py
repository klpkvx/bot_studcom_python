from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN
import requests
import os


def get_json_from_table(list_name):
    urlGetSheets = "https://sheets.googleapis.com/v4/spreadsheets/"
    sheetId = "1Kl35dxvKcUXNLS_0HZYomSXuQcPBMbtQ-gI-Blyv96Y"
    # Get API key from environment variable for security
    keyToken = os.getenv('GOOGLE_SHEETS_API_KEY')
    if not keyToken:
        raise ValueError("GOOGLE_SHEETS_API_KEY environment variable is not set")
    
    listName = list_name
    fullGetUrl = urlGetSheets + sheetId + "/values/" + listName + "?key=" + keyToken
    r = requests.get(url=fullGetUrl)
    if r.status_code != 200:
        raise Exception(f"Failed to fetch data from Google Sheets: {r.status_code}")
    print(f'Database {list_name} successfully loaded!')
    return r.json()


bot = Bot(TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
database_table = get_json_from_table("MAIN_DATA")
other_data_table = get_json_from_table("OTHER_DATA")
food_ds_table = get_json_from_table('FOOD')
shop_ds_table = get_json_from_table('SHOP')
admin_ds_table = get_json_from_table('ADMINISTRATION_DS')
