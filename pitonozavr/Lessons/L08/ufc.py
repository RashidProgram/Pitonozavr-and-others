import random, time

def create_fighter():
	person = {"удары_руками": 100,
	"удары_в_партере": 100,
	"перевод_в_партер": 110,
	"выносливость": 1000,
	"крит._удар": 5,
	"защита_от_тейкдаунов": 100,
	"защита_от_сабмишнов": 100,
	"защита_от_рук": 50,
	"защита_от_ног": 75,
	"самбмишн": 100,
	"удары_ногами": 150,
	  }
	person["имя"] = input("Введите имя, боец ")
	person["фамилия"] = input("Теперь фамилию ")
	choose = input("""А теперь путь по которому вы шли
	1 - ударник,
	2 - борец, 
	3 - танк,
	4 - тхеквандист,
	5 - греплер,
	6 - нокаутер """)
	if choose == "1":
		person["путь"] = "ударник"
		person["удары_руками"] += 50
		person["крит._удар"] += 5
		person["удары_в_партере"] += 15
	elif choose == "2":
		person["путь"] = "борец"
		person["удары_в_партере"] += 40
		person["перевод_в_партер"] += 35
		person["самбмишн"] += 15
		person["контр_перевод_в_партер"] = 110
		person["защита_от_сабмишнов"] += 25
		person["удары_руками"] -= 25
		person["защита_от_рук"] -= 10
		person["защита_от_ног"] -= 5
		person["удары_ногами"] -= 25
	elif choose == "3":
		person["путь"] = "танк"
		person["выносливость"] += 800
		person["крит._удар"] += 10
		person["удары_руками"] -= 5
	elif choose == "4":
		person["путь"] = "тхеквандист"
		person["удары_ногами"] += 100
		person["крит._удар"] += 10
	elif choose == "5":
		person["путь"] = "греплер"
		person["удары_в_партере"] += 30
		person["перевод_в_партер"] += 25
		person["самбмишн"] += 30
		person["контр_перевод_в_партер"] = 100
		person["защита_от_сабмишнов"] += 35
		person["удары_руками"] -= 20
		person["защита_от_рук"] -= 10
		person["защита_от_ног"] -= 5
		person["удары_ногами"] -= 25
	elif choose == "6":
		person["путь"] = "нокаутер"
		person["победный_удар"] = 10
		person["крит._удар"] += 30
		person["удары_руками"] += 25
	else:
		person["путь"] = "никто"
	return person

def health(player):
	print("У игрока", player["имя"], "осталось", 
		player["выносливость"], "выносливости")

def attack(attacker, defender, upOrDown):
	if upOrDown == True:
		act = input("Что будешь делать,"+attacker["имя"]+"\n1 - удар рукой, 2 - удар ногой, 3 - попытка перевода в партер, 4 - ждать действия противника ")
		kritikal = random.randint(1,100)
		print(kritikal)
		if act == "1":
			if attacker["путь"] == "нокаутер":
				if kritikal in range(1,int(attacker["победный_удар"])):
					loss = defender["выносливость"]
					print(attacker["имя"],"Отправил в нокаут противника")
					defender["выносливость"] -=loss 
					return
			if kritikal in range(1,int(attacker["крит._удар"])):
				print(attacker["имя"],"Зарядил противнику")
				loss = random.randint((attacker["удары_руками"] - 30) * 5,(attacker["удары_руками"] + 30) * 5 )
			else:
				loss = random.randint(attacker["удары_руками"] - 30,attacker["удары_руками"] + 30)
			damage = loss - int(defender["защита_от_рук"])
			print(attacker["имя"], "нанес", int(damage), "урона")
			defender["выносливость"] -= damage
			time.sleep(1.4)
		elif act == "2":
			if kritikal in range(1,int(attacker["крит._удар"])):
				print(attacker["имя"],"Зарядил противнику")
				loss = random.randint((attacker["удары_ногами"] - 30) * 5,(attacker["удары_ногами"] + 30) * 5)
			else:
				loss = random.randint(attacker["удары_ногами"] - 30,attacker["удары_ногами"] + 30)
			damage = loss - int(defender["защита_от_ног"])
			print(attacker["имя"], "нанес", int(damage), "урона")
			defender["выносливость"] -= damage
			time.sleep(1.4)
		elif act == "3":
			if defender["путь"] == "борец" or defender["путь"] == "греплер":
				parter = random.randint(attacker["перевод_в_партер"] - 30,attacker["перевод_в_партер"] + 10)
				defparter = random.randint(defender["контр_перевод_в_партер"] - 10,defender["контр_перевод_в_партер"] + 30)
				print(parter,defparter)
				if (parter - defparter) > 0:
					upOrDown = False
					print(attacker["имя"],"перевел бой в партер")
					time.sleep(1.4)
				else:
					upOrDown = False
					print(attacker["имя"],"хотел перевести бой в партер,\n но из-за опытности противника в борьбе проиграл позиции")
					time.sleep(1.4)
			else:
				parter = random.randint(attacker["перевод_в_партер"] - 30,attacker["перевод_в_партер"] + 5)
				defparter = random.randint(defender["защита_от_тейкдаунов"] - 5,defender["защита_от_тейкдаунов"] + 30)
				print(parter,defparter)
				if (parter - defparter) > 0:
					upOrDown = False
					print(attacker["имя"],"перевел бой в партер")
					time.sleep(1.4)
				else:
					print("Была проведенна неудачная попытка перевода боя в партер")
					time.sleep(1.4)
		else:
			print(attacker["имя"],"хотел что-то сделать, но похоже передумал")
			time.sleep(1.4)
	elif upOrDown == False:
		act = input("Что будешь делать, "+attacker["имя"]+"\n1 - удар рукой,\n 2 - подняться из партера,\n 3 - попытка сабмишна,\n 4 - ждать действия противника ")
		kritikal = random.randint(1,100)
		if act == "1":
			if attacker["путь"] == "нокаутер":
				if kritikal in range(1,int(attacker["победный_удар"])):
					loss = defender["выносливость"] 
			if kritikal in range(1,int(attacker["крит._удар"])):
				loss = random.randint((attacker["удары_в_партере"] - 30) * 5,(attacker["удары_в_партере"] + 30) * 5)
			else:
				loss = random.randint(attacker["удары_руками"] - 30,attacker["удары_руками"] + 30)
			damage = loss - int(defender["защита_от_рук"])
			print(attacker["имя"], "нанес", int(damage), "урона")
			defender["выносливость"] -= damage
			time.sleep(1.4)
		elif act == "2":
			parter = random.randint(attacker["перевод_в_партер"] - 30,attacker["перевод_в_партер"] + 10)
			defparter = random.randint(defender["защита_от_тейкдаунов"],defender["защита_от_тейкдаунов"] + 30)
			print(parter,defparter)
			if (defparter - parter) > 0:
				upOrDown = True
				print(attacker["имя"],"перешел в стойку")
				time.sleep(1.4)
			else:
				print("Была проведенна неудачная попытка подняться в стойку")
				time.sleep(1.4)
		elif act == "3":
			submition = attacker["самбмишн"]
			defSubmition = random.randint(defender["защита_от_сабмишнов"] + 10,defender["защита_от_сабмишнов"] + 40)
			if defSubmition - submition <= 0:
				damage = attacker["самбмишн"] * 5
				defender["выносливость"] -= damage
				if defender["выносливость"] <= 0:
					print(attacker["имя"],"сделал сабмишн и противник сдался")	
				else:
					upOrDown = True
					print(attacker["имя"],"сделал сабмишн и отнял у противника",damage,"урона")
			else:
				upOrDown = True
				print("была проведена неудачная попытка самбмишна")
		time.sleep(1.4)
	return upOrDown
person1 = create_fighter()
person2 = create_fighter()
print("В этом бою встеретятся два новичка в ufc посмотрим на что они способны")
time.sleep(1)
print("Поприветстувуйте бойца справа")
time.sleep(1)
print(person1["имя"],"!!!")
time.sleep(1)
print(person1["путь"],"!!!")
time.sleep(1)
print(person1["фамилия"],"!!!")
print("А вот и боец слева, ")
time.sleep(1)
print("Поприветстувуйте")
time.sleep(1)
print(person2["имя"],"!!!")
time.sleep(1)
print(person2["путь"],"!!!")
time.sleep(1)
print(person2["фамилия"],"!!!")
time.sleep(2)
print("Начался бой противники пока не предпринимают действий, похоже",person1["имя"],"что-то хочет сделать")
TrueOrFalse = attack(person1,person2,True)
while True:
	TrueOrFalse = attack(person2, person1, TrueOrFalse)
	if person2["выносливость"] <= 0:
		print(person1["имя"], "выграл")
		break	
	if person1["выносливость"] <= 0:
		print(person2["имя"], "выграл")
		break
	health(person1)
	health(person2)

	TrueOrFalse = attack(person1,person2,TrueOrFalse)
	if person2["выносливость"] <= 0:
		print(person1["имя"], "выграл")
		break	
	if person1["выносливость"] <= 0:
		print(person2["имя"], "выграл")
		break
	health(person1)
	health(person2)


