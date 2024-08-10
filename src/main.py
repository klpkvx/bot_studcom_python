from utils import client, other
import aiogram.utils as ut
from aiogram.utils import executor
from utils.create_bot import dp, bot
import config
from asyncio import create_task
import logging
import sys
from utils.common_utils import get_subscribed_users, send_daily_message
from utils.authentication import AuthorizationMiddleware


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


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    dp.setup_middleware(AuthorizationMiddleware())
    client.register_handlers_client(dp)  # Events from user
    other.register_handlers_other(dp)  # Other events
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
