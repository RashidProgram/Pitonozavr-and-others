class Pupils:
	head = True
	legs = True
	fingers = 10
	marks = 2
	name = None
	def learn(self,name):
		self.name = name
		if self.head == True:
			print("А голову ты дома не забыл???")
		else:
			print(self.head)
rashid = Pupils()
print(rashid.marks)
rashid.learn(input("Как тебя зовут, ученик?"))
print(rashid.name)
	
		