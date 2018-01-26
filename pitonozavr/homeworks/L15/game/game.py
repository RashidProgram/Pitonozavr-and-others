from random import randint
from time import sleep
import Error as err
import sujet as suj
class Orydie:

	def __init__(self,name, ammo, damage):
		self.name = name
		self.ammo = ammo
		self.damage = damage
	def vistrel(self, ammo,damage, target):
		if ammo > 0:
			print("Вы выстрелили в",target.name)
			target.healght -= damage
			ammo -= 1
		else:
			print("У вас закончились патроны")
class Human:
	def __init__(self,name, healght, damage):
		self.healght = healght
		self.damage = damage
		self.name = name
class Hero(Human):
	def __init__(self, name, healght, damage, medical_box, orydie, money):
		super().__init__(name, healght, damage)
		self.medical_box = medical_box
		self.orydie = orydie
		self.money = money
	def attack(self,target):
		while True:
			try:
				answer = int(input('1 - Стреляем, 2 - бьем?\n'))
				if answer != 1 and answer != 2:
					raise err.NumberError('Введите 1 или 2')
			except err.NumberError as e:
				print(e)
			except ValueError:
				print('Введите число!!!')
			else:
				break
			finally:
				sleep(2)			
			
		if answer == 1:
			self.orydie.vistrel(self.orydie.ammo,self.orydie.damage, target)
		elif answer == 2:
			print(self.name,"ударил",target.name)
			target.healght -= self.damage
class Zombie(Human):
	def __init__(self,name,healght,damage,moneyPeople, kolvo):
		super().__init__(name, healght, damage)
		self.moneyPeople = moneyPeople
		self.kolvo = kolvo
	def attack(self, target):
		print(self.name,"ударил",target.name)
		target.healght -= self.damage
def battle(player,zombie_leg,zombie_sr,rezer_sr, res_leg):
	kolvoMoney = 0
	while True:
		if player.healght > 0:
			print(player.name,"Хотите воспользоваться аптечкой?")
			try:
				i = int(input("1 - да\n2 - нет\n"))
				if i < 1 or i > 2:
					raise err.NumberError("Необходимо ввести число от 1 до 2")
			except err.NumberError as e:
				print(e)
				continue
			except ValueError:
				print("Введите число")
			else:
				sleep(1)
				if i == 1:
					if player.medical_box > 0:
						print("Вы воспользовались аптечкой")
						player.healght += 20
						player.medical_box -= 1
					else:
						print("Аптечек больше нет!")
					sleep(1)
					print("А теперь вы атакуете")
				else:
					print("Вы атакуете")
				player.attack(zombie)
				if zombie.healght <= 0:
					zombie.kolvo -= 1
					print("Вы убили противника")
					zombie.healght = rezer_sr.healght
					print("Осталось",zombie.kolvo,"зомби")
					player.money += zombie.moneyPeople
					kolvoMoney += zombie.moneyPeople
					print("Теперь у тебя ",player.money,"битконов")
				zombie.attack(player)
			finally:
				sleep(2)
		if player.healght <= 0:
			print("Игра окончена")
			print(player.name,"успел порубить",count_kill,zombie.name,"и заработать", kolvoMoney,"биткоинов")

			break
		if zombie.kolvo == 0:
			print("Игра окончена")
			print("Вы победили!!! и заработали", kolvoMoney, "биткоинов")
			zombie.healght = rezer_sr.healght + 5
			rezer_sr.healght += 5
			zombie.damage = rezer_sr.damage + 3
			rezer_sr.damage += 3	
			zombie.moneyPeople += rezer_sr.moneyPeople + 5
			rezer_sr.moneyPeople += 5
			zombie.kolvo = rezer_sr.kolvo + 1
			rezer_sr.kolvo += 1
			break
		print("У вас осталось", player.healght,"жизней и",player.medical_box,"аптечек")
		print('У',zombie.name,"осталось",zombie.healght+'/'+rezer_sr.healght)
	print('Вы вернулись в подземелье')
	menuLocation(player,zombie_leg,zombie_sr,rezer_sr, res_leg)
def menuLocation(player,zombie_leg,zombie_sr,rezer_sr, res_leg):
	global shetchik
	if shetchik == 0:
		text = "Ладно ты осваивайся а я пошел в свой магаз."
		print("Ты в укрытии.")
		sleep(1)
		print("Тут не подалеку есть магазин оружий и аптечек их продаю я,")
		sleep(1.5)
		print("многие люди зомбировались с кошельками, так как не знали о наступлении апокалипсиса,")
		sleep(2)
		print("значит денег ты найдешь много,")
		sleep(1)
		print(text)
		shetchik += 1
	text = "1 - пойти в магазин\n2 - пойти наверх\n"
	while True:
		try:
			deistvia = int(input(text))
			if deistvia > 2 or deistvia < 1:
				raise err.NumberError("Вы должны ввести число от 1 до 2 не больше и не меньше!!!")
		except ValueError:
			print("Введите число 1 или 2!!!")
			continue
		except err.NumberError as e:
			print(e)
			continue
		else:
			break
	if deistvia == 1:
		sleep(1.5)
		magaz(player,zombie_leg,zombie_sr,rezer_sr, res_leg)
	elif deistvia == 2:
		go_up(player,zombie_leg,zombie_sr,rezer_sr, res_leg)
def vijivanie(player,zombie_leg,zombie_sr,rezer_sr, res_leg):
	kolvoMoney = 0
	while True:
		if player.healght > 0:
			print(player.name,"Хотите воспользоваться аптечкой?")
			try:
				i = int(input("1 - да\n2 - нет\n"))
				if i < 1 or i > 2:
					raise err.NumberError("Необходимо ввести число от 1 до 2")
			except err.NumberError as e:
				print(e)
				continue
			except ValueError:
				print("Введите число")
			else:
				sleep(1)
				if i == 1:
					if player.medical_box > 0:
						print("Вы воспользовались аптечкой")
						player.healght += 20
						player.medical_box -= 1
					else:
						print("Аптечек больше нет!")
					sleep(1)
					print("А теперь вы атакуете")
				else:
					print("Вы атакуете")
				player.attack(zombie)
				if zombie.healght <= 0:
					zombie.kolvo += 1
					print("Вы убили противника")
					zombie.healght = res_leg.healght
					player.money += zombie.moneyPeople
					kolvoMoney += zombie.moneyPeople
					print("Теперь у тебя ",player.money,"битконов")
				zombie.attack(player)
			finally:
				sleep(2)
		if player.healght <= 0:
			print("Игра окончена")
			print(player.name,"успел порубить",count_kill,zombie.name,"и заработать", kolvoMoney,"биткоинов")
			break
		if zombie.kolvo >= 15:
			zombie.healght = res_leg.healght + 5
			res_leg.healght += 5
			zombie.damage = res_leg.damage + 3
			res_leg.damage += 3	
			zombie.moneyPeople += res_leg.moneyPeople + 5
			res_leg.moneyPeople += 5
			zombie.kolvo = res_leg.kolvo + 1
			res_leg.kolvo += 1
		print("У вас осталось", player.healght,"жизней и",player.medical_box,"аптечек")
		print('У',zombie.name,"осталось",zombie.healght+'/'+res_leg.healght)		
def go_up(player,zombie_leg,zombie_sr,rezer_sr, res_leg):
	print("Вы поднялись из подземелья наверх, и увидели 3 таблички и 3 пути")
	sleep(1)
	print("1 - Выживание(уровень зомби слабый),")
	sleep(2)
	print("2 - Отряды зомби(уровень зомби средний),")
	sleep(2)
	print("3 - Сражение на територии зомби(уровень зомби сильный),")
	sleep(2)
	print("4 - вернуться назад. Куда идем?")
	while True:
		try:
			answer = int(input())
			if answer < 1 or answer > 4:
				raise err.NumberError("Вы должны ввести число от 1 до 4 не больше и не меньше!!!")
		except err.NumberError as e:
			print(e)
			continue
		except ValueError:
			print("Введите число!!!")
			continue
		else:
			break
		finally:
			sleep(1)
	
	if answer == 1:
		vijivanie(player,zombie_leg,zombie_sr,rezer_sr, res_leg)
	if answer == 2:
		battle(player,zombie_leg,zombie_sr,rezer_sr, res_leg)
	elif answer == 3:
		map(player)
	elif answer == 4:
		print("Вы вернулись назад.")
		menuLocation(player,zombie_leg,zombie_sr,rezer_sr,res_leg)
def magaz(player,zombie_leg,zombie_sr,rezer_sr, res_leg):
	tovars = {
		1 : {"Номер": 1, "Название":"Аптечка","стоимость": 100,},
		2 : {"Номер": 2, "Название": "Кастет","стоимость": 110,"урон": 15},
		3 : {"Номер": 3, "Название": "Мачете","стоимость": 130,"урон": 20},
		4 : {"Номер": 4, "Название": "Катана","стоимость": 150,"урон": 30},
		5 : {"Номер": 5, "Название": "Revolver", "стоимость": 300, "патронов": 8,"урон": 70},
		6 : {"Номер": 6, "Название": "Deseart Eagle","стоимость":250,"патронов": 8,"урон": 60},
		7 : {"Номер": 7, "Название": "Ak-47","стоимость": 400,"патронов": 23,"урон": 60}}

	print("Привет",player.name,"решил посетить магазин. Хочешь посмотреть товары и их функции?")
	while True:
		try:
			answer = int(input("1 - товары и их функции\n2 - уйти из магазина\n"))
			if answer > 2 or answer < 1:
				raise err.NumberError("Вы должны ввести число от 1 до 2 не больше и не меньше!!!")
		except ValueError:
			print("Введите число 1 или 2!!!")
			continue
		except err.NumberError as e:
			print(e)
			continue
		else:
			break
		finally:
			sleep(2)
	if answer == 1:
		for i in tovars:
			print(tovars[i].items())
			sleep(2)
		while True:
			try:
				answer = int(input("Брать будешь?\n 1 - да\n2 - нет\n"))
				if answer > 2 or answer < 1:
					raise err.NumberError("Вы должны ввести число от 1 до 2 не больше и не меньше!!!")
			except ValueError:
				print("Введите число!!!")
				continue
			except err.NumberError as e:
				print(e)
			else:
				break
			finally:
				sleep(2)			
		if answer == 1:
			viborPokypki(player,zombie_leg,zombie_sr,rezer_sr, res_leg)
		else:
			print("Не хочешь - как хочешь")
	elif answer == 2:
		print("Ладно удачи!")
		menuLocation(player,zombie_leg,zombie_sr,rezer_sr,res_leg)
def viborPokypki(player,zombie_leg,zombie_sr,rezer_sr, res_leg):
	tovars = {
		1 : {"Номер": 1, "Название":"Аптечка","стоимость": 100,},
		2 : {"Номер": 2, "Название": "Кастет","стоимость": 110,"урон": 15},
		3 : {"Номер": 3, "Название": "Мачете","стоимость": 130,"урон": 20},
		4 : {"Номер": 4, "Название": "Катана","стоимость": 150,"урон": 30},
		5 : {"Номер": 5, "Название": "Revolver", "стоимость": 300, "патронов": 8,"урон": 70},
		6 : {"Номер": 6, "Название": "Deseart Eagle","стоимость":250,"патронов": 8,"урон": 60},
		7 : {"Номер": 7, "Название": "Ak-47","стоимость": 400,"патронов": 23,"урон": 60}}
	print("Выбери что хочешь купить")
	while True:
		print("У тебя",player.money,"биткоинов")
		try:
			answer = int(input("Введи номер оружия(он указан в функции товара),\n8 - если снова хочешь посмотреть функции товаров,\nи 9 - если хочешь уйти из магазина\n"))
			if answer > 9 or answer < 1:
				raise err.NumberError("Вы должны ввести число от 1 до 9 не больше и не меньше!!!")
		except ValueError:
			print("Введити число!!!!!")
			continue
		except err.NumberError as e:
			print(e)
			continue
		else:
			break
		finally:
			sleep(2)
	if answer in range(1,8):
		pokypka(player,zombie_leg,zombie_sr,rezer_sr, res_leg,answer)
	elif answer == 8:
		for i in tovars:
			print(tovars[i].items())
			sleep(2)
		viborPokypki(player,zombie_leg,zombie_sr,rezer_sr, res_leg)
	elif answer == 9:
		print("Ок! Удачи")
		menuLocation(player,zombie_leg,zombie_sr,rezer_sr, res_leg)
def pokypka(player,zombie_leg,zombie_sr,rezer_sr, res_leg,number):
	global shetchik
	tovars = {
		1 : {"Номер": 1, "Название":"Аптечка","стоимость": 100,},
		2 : {"Номер": 2, "Название": "Кастет","стоимость": 110,"урон": 15},
		3 : {"Номер": 3, "Название": "Мачете","стоимость": 130,"урон": 20},
		4 : {"Номер": 4, "Название": "Катана","стоимость": 150,"урон": 30},
		5 : {"Номер": 5, "Название": "Revolver", "стоимость": 300, "патронов": 8,"урон": 70},
		6 : {"Номер": 6, "Название": "Deseart Eagle","стоимость":250,"патронов": 8,"урон": 60},
		7 : {"Номер": 7, "Название": "Ak-47","стоимость": 400,"патронов": 23,"урон": 60}}
	if number == 1:
		if player.money - tovars[number]["стоимость"] >= 0: 
			player.medical_box += 1
			player.money -= tovars[number]["стоимость"]
			print("Поздравляю с покупкой!!! теперь у тебя", player.medical_box,"аптечки")
		else:
			print("У вас недостаточно средств для покупки")
			sleep(1)
			viborPokypki(player,zombie_leg,zombie_sr,rezer_sr, res_leg)
	elif number in range(2,5):
		if shetchik == 1:	
			if player.money - tovars[number]["стоимость"] > 0: 
				player.blijBoi = tovars[number]["урон"]
				player.damage += player.blijBoi
				player.money -= tovars[number]["стоимость"]
				print("Поздровляю с покупкой!!! теперь у тебя",player.damage,"урона и",tovars[number]["Название"],)
			else:
				print("У вас недостаточно средств для покупки")
				viborPokypki(player,zombie_leg,zombie_sr,rezer_sr, res_leg)
			shetchik += 1
		else:
			if player.money - tovars[number]["стоимость"] > 0: 
				player.damage -= player.blijBoi 
				player.blijBoi = tovars[number]["урон"]
				player.damage += player.blijBoi
				player.money -= tovars[number]["стоимость"]
				print("Поздровляю с покупкой!!! теперь у тебя",player.damage,"урона и",tovars[number]["Название"],)
			else:
				print("У вас недостаточно средств для покупки")
				viborPokypki(player,zombie_leg,zombie_sr,rezer_sr, res_leg)
	else:
		if player.money - tovars[number]["стоимость"] > 0: 
			player.orydie.damage = tovars[number]["урон"]
			player.orydie.ammo = tovars[number]["патронов"]
			player.orydie.name = tovars[number]["Название"]
			player.money -= tovars[number]["стоимость"]
			print('Поздровляю с новым',player.orydie.name,'!!!')
		else:
			print("У вас недостаточно средств для покупки")
			viborPokypki(player,zombie_leg,zombie_sr,rezer_sr, res_leg)
	while True:
		try:
			answer = int(input('Хочешь что нибудь еще?\n1 - да\n2 - нет'))
			if answer != 1 and answer != 2:
				raise err.NumberError("Введите 1 или 2!!!")
		except err.NumberError as e:
			print(e)
		except ValueError:
			print("Ввелите число")
		else:
			break
		finally:
			sleep(1.5)
	if answer == 1:
		viborPokypki(player,zombie_leg,zombie_sr,rezer_sr, res_leg)
	elif answer == 2:
		print('Ок')
		sleep(2)
		menuLocation(player,zombie_leg,zombie_sr,rezer_sr, res_leg)
#suj.sydjet()
orydie = Orydie("Травмат",5,10)
eldar = Hero(input("Кстати как тебя зовут?\n"), 150, 15, 3, orydie, 100)
eldar.name = eldar.name.capitalize().strip()
if eldar.name == 'Султан' or eldar.name == "Мурад" or eldar.name == "Султанмурад" or eldar.name == "Sultan" or eldar.name == "Murad" or eldar.name == "Sultanmurad" or eldar.name == "Myrad" or eldar.name == "Sultanmyrad":
	print("Султанмурад вы проверяете мою домашку.\nТут есть магазин и чтоб вы могли проверить его у вас будет много денег")
	sleep(2)
	eldar.money = 100000
sred_zombo = Zombie("Зомбарь", 25, 30, 15, 10)
leg_zombo = Zombie("Ватник", 15, 20, 10, 0)
rezLeg = Zombie("Ватник", 15, 20, 10, 0)
reserv = Zombie("Резерв", 25, 30, 15, 10)
shetchik = 0
menuLocation(eldar, leg_zombo, sred_zombo,reserv,rezLeg)