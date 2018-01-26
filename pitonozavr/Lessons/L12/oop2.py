class Worker:
	def __init__(self,qualif,salary,hemmer):
		self.qualif = qualif
		self.salary = salary
		self.hemmer = hemmer
	def work(self):
		print("Пашу как пахарь")
	def badwork(self):
		print("НАДОЕЛА ЭТА РАБОТА!!!\n НО ЕСЛИ УВОЛЮСЬ СТАНУ БОМЖОМ :(((")
# petrovich = Worker()
# print(petrovich.salary)
# petrovich.work()
# petrovich.badwork()

# ivanish = Worker()
# print(ivanish.salary)
# ivanish.work()
# ivanish.badwork()

eldar = Worker(True, 0, 2000000)
print(eldar.salary)

class Miner(Worker):
	def mine(self):
		print("Я намайнил",self.salary,"крипторубль")
# aminka = Miner(True, 0.0001, -10)
# aminka.mine()
# aminka.badwork()
# print(aminka.qualif)

class Proger(Worker):
	def __init__(self, language, cofee, qualif,salary,expa, name):
		super().__init__(qualif,salary,expa)
		self.language = language
		self.cofee = cofee
		self.name = name
	def attack(self, target):
		print("Прогер хакнул " + target)

	def work(self):
		print("Валяться, попивая кофе у себя на районе")

moloch = Proger(True, 5000000, 4, "Paskal + Delfi", "Java", "Малик")

class Gastranomer(object):
	def __init__(self, salary, heavy_hand, name):
		self.salary = salary
		self.heavy_hand = heavy_hand
		self.name = name
	def attack(self, target):
		print(self.name + " \nСо всего размаха ударил " + target + "\n с силой"+ self.heavy_hand)
sulik = Proger(0, 0, 0, "Scrange", "mcCoffee", "Сулейман")
ela = Gastranomer(5, 1000, "эля")
def fight(fighter1,fighter2):
	fighter1.attack(fighter2.name)
fight(sulik, ela)




		