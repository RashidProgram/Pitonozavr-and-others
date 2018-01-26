def my_sum(y, z):
	# x = y + z
	return y + z
print(my_sum(2, 5))
def my_div(x, y):
	return x / y
print(my_div(2, 10))
def lucku_list(judge, victim, sherif, executioner):
	print(sherif + " требую екзукуции и справедливости")
	print(judge + " благословляю на казнь!")
	print(executioner + " отправил " + victim + " на курсы по Паскалю")
lucku_list(judge = "Бабушка Аня", sherif = "Гоминид", victim = "Сулейманчик", executioner = "Гаджи")

def freid(victim, is_mad = True):
	if  is_mad == True:
		print("Фреид, потирая руки, достает сигару и тушит об " + victim)
	elif  is_mad == False:
		print("Фреид, с грустью зажигаетсигару о пламени сердца " + victim)
	else:
		print("Вы и есть Фреид")
freid("Эльдар", True)
print(2, 3, 4, "Эльдар")
def reptiloid_list(*args, **kwargs):
	print("Остерегайтесь их:", args)
	print("Стрелять без предупреждения по:", kwargs)
reptiloid_list("Сулейманчек","Султанмурад","Гаджи","Эльдар",
	"Вера Андреевна",jidomasson = "Саид",lemurian = "Эльдар")