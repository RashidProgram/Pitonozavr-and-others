import time
import random
track = 45
def eezzzee(player):
	player.distanse += player.speed
	player.fuel -= player.expen

def neeetrooo(player):
	player.distanse += player.nitro
	player.fuel -= player.expen * 3

def stats(player):
	time.sleep(1.5)
	text =print("Текущее состояние "+player.name+" :",
		"Топливо: " + str(player.playerCar.fuel),
		"Расстояние: " + str(player.playerCar.distanse) + "/" + str(track),
		sep = "\n"
		)
	time.sleep(1.5)
	return text
def step(player):
	print("\nТвой ход, " + player.name +
	". Что будем делать?")
	stats(player)
	print("1 - Просто едем",
	"2 - топиим!!",
	sep = "\n"
	)
	choose = input()
	
	if choose == "1":
		eezzzee(player.playerCar)
	elif choose == "2":
		neeetrooo(player.playerCar)
	else:
		print("Ты ошибся!")
	time.sleep(1)
	time.sleep(1.2)
def getCar(userList,variable):
	i = 0
	while i != len(userList):
		element_cars = random.choice(variable)
		userList[i].playerCar = element_cars
		print("Игроку ",userList[i].name,"достался",element_cars.name)
		variable.remove(element_cars)
		time.sleep(2)
		i += 1

def isLose(player,playerArray):
	whileStop = False
	if player.playerCar.fuel <= 0:
		playerArray.remove(player)
		if len(playerArray) == 1:
			print("У игрока",player.name,
			"закончилось топливо,\nа это значит что",
			playerArray[0].name,"победил!!!"
			)
			whileStop = True
		else:
			print("У игрока",player.name,
			"закончилось топливо \nи в гонке остаются",
			playerArray[0].name,playerArray[1].name
			)
	elif player.playerCar.distanse >= track:
		print(player.name,"первым доходит до финиша и побеждает!!!")
		whileStop = True
	return whileStop

def stepForbot(bot,oneOrTwo):
	print("Ход противника")
	print(bot.name,"думает...")
	time.sleep(3)
	choose = oneOrTwo
	
	if choose == "1":
		print(bot.name,"решил просто ехать")
		time.sleep(1)
		stats(bot)
		eezzzee(bot.playerCar)
	elif choose == "2":
		print(bot.name,"решил газовать")
		time.sleep(1)
		stats(bot)
		neeetrooo(bot.playerCar)
	
	time.sleep(1.2)