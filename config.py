from os.path import join

# В кавычки нужно ввести токен из BotFather
TOKEN = '6618766493:AAExSHuMwIt126mg4F4mKUuiahcnOEwG32Y'


# TOKEN = "5713033359:AAEBBgn-55ZDfGVEgLqMTsUmsA3HAjwp5ko"

# Пути к папкам и файлам:

class FileLocation:
    data_dir = 'data/'
    text_dir = data_dir + 'cmd_files/'
    horo_dir = 'data/horo_pics/'

    cmd_help = join(text_dir, 'cmd_help.html')
    cmd_comenda_info = join(text_dir, 'cmd_comenda_info.html')
    cmd_check_rooms_time = join(text_dir, 'cmd_check_rooms_time.html')
    cmd_my_starosta = join(text_dir, 'cmd_my_starosta.html')
    cmd_rasselenie_info = join(text_dir, 'cmd_rasselenie_info.html')
    cmd_horo_help = join(text_dir, 'cmd_horo_help.html')


admin_ids = [
    575238020,  # klepikov
    536591458,  # Makarov
    693189663,  # Trush
    806602991,  # Arsenii
]
