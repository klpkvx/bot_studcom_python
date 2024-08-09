from utils import client, admin, other
import aiogram.utils as ut
from aiogram.utils import executor
from create_bot import dp, bot
import config
from asyncio import create_task

from utils.common_utils import get_subscribed_users, send_daily_message


async def on_startup(_):  # info about start bot
    print('Bot has been started\n')
    for user_id in config.admin_ids:
        try:
            await bot.send_message(user_id, "Bot has been started")
        except ut.exceptions.BotBlocked:
            print(f'User: {user_id} blocked this bot')
    users = get_subscribed_users()
    print(users)
    for user_id in users:
        create_task(send_daily_message(user_id))


'''Client_part'''
client.register_handlers_client(dp)

'''Common part'''
other.register_handlers_other(dp)

# Самый последний Хендлер в который все говно будет попадать
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
