# описываем участников + скорость, нитро, бак, расход топлива, имя, пройденный путь
# на выбор: обычная скорость, нитро + расход топлива в 3 - каждый ход
# Побеждает тот, кто приехал первым, либо тот, у кого позже заккккончилось топливо
import speed as s
import random
import time
import myBot
#Объект создающий игроков
class CreatePlayer:
	name = None
	playerCar = None
	countPeoples = 0
	def getSvoistva(self,name ,notName):
		if name == None or name == "" or name == " ":
			self.name = notName
		else:
			self.name = name
		self.countPeoples += 1
#Количество игроков и их создание
nameForBot = ["Бот-Антон","Бот-Артем","Бот-Паша","Бот-Сергей","Бот-Василий"]
bot = CreatePlayer()
bot.getSvoistva(random.choice(nameForBot),random.choice(nameForBot))
kolvoPlayers = input("Выберете кол-во игроков:1, 2 или 3 ").strip()
players_list = []
player1 = CreatePlayer()
player1.getSvoistva(input("Введите имя первого игрока "),"Аноним")
players_list.append(player1)
if kolvoPlayers == "2":
	player2 = CreatePlayer()
	player2.getSvoistva(input("Введите имя второго игрока "),"Безымяный")
	players_list.append(player2)
	print("Игра на 2")
elif kolvoPlayers == "3":
	player2 = CreatePlayer()
	player2.getSvoistva(input("Введите имя второго игрока "),"Безымяный")
	players_list.append(player2)
	player3 = CreatePlayer()
	player3.getSvoistva(input("Введите имя третьего игрока "),"Скрытный")
	players_list.append(player3)
	print("Игра на 3")
else:
	print("Игра на 1")
	players_list.append(bot)

print("Здравствуйте сейчас устроим гонки:\n вам дадут рандомно одну из наших машин и на них вы посоревнуетесь")
time.sleep(1)
print("Вот список игроков:")
if kolvoPlayers == "2":
	print(player1.name,player2.name,sep = ", ")
elif kolvoPlayers == "3":
	print(player1.name,player2.name,player3.name,sep = ", ")
else:
	print(player1.name,bot.name,sep = ", ")
time.sleep(1)
#Объект создающий машины
class CreateCar():
	name = None,
	speed = 0,
	fuel = 0,
	expen = 0,
	nitro = 0,
	distanse = 0,
	def getSvoistva(self,name,speed = 6,fuel = 30,expen = 3,nitro = 11,distanse = 0):
		self.name = name
		self.speed = speed
		self.fuel = fuel 
		self.expen = expen 
		self.nitro = nitro
		self.distanse = distanse 
#Создание машин		
car1 = CreateCar()
car1.getSvoistva("BetCar", 6, 35, 3, 11, 0)

car2 = CreateCar()
car2.getSvoistva("Black Lightning", 8, 30, 4, 13, 0)

car3 = CreateCar()
car3.getSvoistva("GameshCar", 7, 32, 3.5, 12, 0)

car4 = CreateCar()
car4.getSvoistva("SultanCar", 9, 27, 4, 14, 0)
cars = [car1, car2, car3, car4]
#Выдача машин
s.getCar(players_list,cars)
#Процесс игры
while True:
	if kolvoPlayers == "2":
		s.step(player1,players_list)
		isWhileStop = s.isLose(player1)
		if isWhileStop == True:
			break
		s.step(player2)
		isWhileStop = s.isLose(player2,players_list)
		if isWhileStop == True:
			break
	elif kolvoPlayers == "3":
		if len(players_list) == 3:
			if players_list[0] == player1:
				s.step(player1)
				isWhileStop = s.isLose(player1,players_list)
				if isWhileStop == True:
					break
			if players_list[1] == player2:
				s.step(player2)
				isWhileStop = s.isLose(player2,players_list)
				if isWhileStop == True:
					break
			if players_list[2] == player3:
				s.step(player3)
				isWhileStop = s.isLose(player3,players_list)
				if isWhileStop == True:
					break
		elif len(players_list) == 2:
			s.step(players_list[0])
			isWhileStop = s.isLose(players_list[0],players_list)
			if isWhileStop == True:
				break
			s.step(players_list[1])
			isWhileStop = s.isLose(players_list[1],players_list)
			if isWhileStop == True:
				break

	else:
		s.step(player1)
		isWhileStop = s.isLose(player1,players_list)
		if isWhileStop == True:
			break
		botAnswer = myBot.randomVibor()
		s.stepForbot(bot,botAnswer)
		isWhileStop = s.isLose(bot,players_list)
		if isWhileStop == True:
			break