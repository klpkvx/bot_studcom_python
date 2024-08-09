from os.path import join

# В кавычки нужно ввести токен из BotFather
TOKEN = '6618766493:AAExSHuMwIt126mg4F4mKUuiahcnOEwG32Y'


# TOKEN = "5713033359:AAEBBgn-55ZDfGVEgLqMTsUmsA3HAjwp5ko"

# Пути к папкам и файлам:

class FileLocation:
    data_dir = 'data/'
    html_dir = data_dir + 'html/'
    horo_dir = data_dir + 'horo_pics/'
    json_dir = data_dir + 'json/'

    cmd_help = join(html_dir, 'cmd_help.html')
    cmd_comenda_info = join(html_dir, 'cmd_comenda_info.html')
    cmd_check_rooms_time = join(html_dir, 'cmd_check_rooms_time.html')
    cmd_my_starosta = join(html_dir, 'cmd_my_starosta.html')
    cmd_rasselenie_info = join(html_dir, 'cmd_rasselenie_info.html')
    cmd_horo_help = join(html_dir, 'cmd_horo_help.html')


admin_ids = [
    575238020,  # klepikov
    536591458,  # Makarov
    693189663,  # Trush
    806602991,  # Arsenii
]
