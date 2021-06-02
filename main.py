from vk_api import vk_api
from colorama import init, Fore
import os

init(autoreset = True)
os.system('cls')

print(Fore.WHITE)

try:
	file = open ("token.txt", "r")
	token = file.read()
	file.close()
except:
	token = input(" Введите token: ")
	save_token = input(" Если хотите сохранить свой токен в 'token.txt' введите 'y' (да) или 'n' (нет): ")

	if save_token.lower() == 'y':
		file = open('token.txt', 'w')
		file.write(token)
		file.close()

		print(Fore.GREEN + ' Token сохранен.')
		print(Fore.WHITE)

try:
	user_id = int(input(" Введите ID страницы: "))
except:
	print(Fore.RED + ' ID введен не верно.')
	input()
	exit()

vk_session = vk_api.VkApi(app_id = 2274003, token = token)
vk = vk_session.get_api()

info = list(vk.users.get(user_id =  user_id, fields = "bdate, city, common_count, contacts, counters, last_seen, online, sex"))

os.system('cls')
print(Fore.WHITE)

name = info[0]['first_name']
surname = info[0]['last_name']

if int(info[0]['online']) == 1:
	online = Fore.GREEN + 'online' + Fore.WHITE

if int(info[0]['online']) == 0:
	online = Fore.RED + 'offline' + Fore.WHITE

if str(info[0]['is_closed']) == 'False':
	status = Fore.GREEN + 'открытый' + Fore.WHITE

if str(info[0]['is_closed']) == 'True':
	status = Fore.RED + 'закрытый' + Fore.WHITE

if int(info[0]['sex']) == 1:
	sex = Fore.WHITE + 'женский'

if int(info[0]['sex']) == 2:
	sex = Fore.WHITE + 'мужской'

if int(info[0]['sex']) == 0:
	sex = Fore.RED + 'не указан' + Fore.WHITE

platform = ''
platform_list = {1 : "телефон", 2 : "iPhone", 3 : "iPad", 4 : "Android", 7 : "браузер"}

if int(info[0]['last_seen']['platform']) in platform_list:
	platform = Fore.WHITE + f"{platform_list[int(info[0]['last_seen']['platform'])]}"

try:
	bdate = Fore.WHITE + info[0]['bdate']
except:
	bdate = Fore.RED + "не указано" + Fore.WHITE

try:
	city = info[0]['city']['title']
except:
	city = Fore.RED + "не указано" + Fore.WHITE

try:
	followers = info[0]['counters']['followers']
except:
	followers = Fore.RED + "не указано" + Fore.WHITE

try:
	videos = info[0]['counters']['videos']
except:
	videos = Fore.RED + "не указано" + Fore.WHITE

try:
	photo = info[0]['counters']['photos']
except:
	photo = Fore.RED + "не указано" + Fore.WHITE

try:
	audio = info[0]['counters']['audios']
except:
	audio = Fore.RED + "не указано" + Fore.WHITE

try:
	groups = info[0]['counters']['pages']
except:
	groups = Fore.RED + "не указано" + Fore.WHITE


print(f" Общее: {name} {surname} [{online}]")
print(f" Тип профиля: {status}")
print(f" Пол: {sex}")
print(f" Дата рождения: {bdate}")
print(f" Город: {city}")
print(f" Платформа: {platform}\n")

print(f" Друзей: {info[0]['counters']['friends']}")
print(f" Общих друзей: {info[0]['common_count']}")
print(f" Друзей онлайн: {info[0]['counters']['online_friends']}")
print(f" Подписчиков: {followers}\n")

print(f" Видео: {videos}")
print(f" Фото: {photo}")
print(f" Аудио: {audio}")
print(f" Подписки: {groups}")

Fore.WHITE
input()
exit()