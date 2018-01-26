import time
class Player:
	def __init__(self,healght,damage,name):
		self.name = name
		self.healght = healght
		self.damage = damage
		self.name = name
		self.money = 100
	def attack(self,enemy):
		print(self.name,"нанес",str(self.damage),"урона ",enemy.name)
		enemy.healght -= self.damage
class Enemy(Player):
	def __init__(self,name,player,hp,dmg,kolvo):
		self.name = name
		self.healght = player.healght/hp
		self.damage = player.damage/dmg
		self.kolvo = kolvo
		self.hp = hp
	def get_money(self):
		return self.money
	def set_money(self, number):
		if self.password == "1лол2кек3":
			self.money = int(number)
		else:
			pass
	
person1 = Player(100,20,input("Введите имя игрока.Поменять его вы не сможете"))
orgs = Enemy("орг",person1,4,2,5)
def attack(player,enemy):
	person1.attack(enemy)
	enemy.attack(player)
while orgs.kolvo != 0:
	attack(person1,orgs)
	time.sleep(1)
	if person1.healght <= 0:
		print("Вы погибли")
		break
	elif orgs.healght <= 0:
		orgs.kolvo -= 1
		print("Вы убили орга и к вашим монетам прибавилось 10")
		person1.password = "1лол2кек3"
		person1.money += 10
		person1.password = "2"
		orgs.healght = person1.healght/orgs.hp
	else:
		print("У орга осталось "+str(orgs.healght)+" хп")
	input("Нажмите Enter")