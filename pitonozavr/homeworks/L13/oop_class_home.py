class Dog:
	def __init__(self, name, breed, color, barking):
		self.name = name
		self.breed = breed
		self.color = color
		self.barking = barking
	def atack(self,enemy):
		print(self.name, "Напал на", enemy.name, "и начал на него лаять: \""+ self.barking + "\"")
sharik = Dog("Шарик","немецкая овчарка","черно-белый","ГАВ!! ГАВ ГАВ")
muzgar = Dog("Музгар","Кавказкая овчарка","красивый","ГААААААВВ!!!!!!! ГАААААААВВ!!!")
def attack(person1, person2):
	person1.atack(person2)
attack(sharik, muzgar)
attack(muzgar, sharik)