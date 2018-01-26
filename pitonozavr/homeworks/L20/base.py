import time
import sqlite3
import numbError as n
school_students = sqlite3.connect("hot_countries.db")
runner = school_students.cursor()
def register():
	runner.execute("DROP TABLE students")

	runner.execute("""CREATE TABLE students (
		name VARCHAR(25),
		lastname VARCHAR(25),
		arg INT,
		login VARCHAR(25),
		password VARCHAR(25)
		)""")
	login = (input("Введите логин\n"))
	a = runner.execute("SELECT login FROM students")
	while login in a:		
		print("Такой логин уже есть")
		time.sleep(1)
		login = (input("Введите другой"))
	name = input("Введите имя\n") 
	lastname = input("Введите фамилию\n")
	arg = n.intError("Введите возраст\n",0,1000,1)
	password = input("Введите пароль\n")

	ins = "INSERT INTO students VALUES(?, ?, ?, ?, ?)"
	inf = name,lastname,arg,login,password
	runner.execute(ins, inf)
	
def avtorise():
	login = input("Введите логин\n")
	password = input("Введите пароль\n")
	userInf = (login,password)
	logAndPass = runner.execute("SELECT login, password FROM students")
	for element in logAndPass:
		if userInf == element:
			print("Вы успешно авторизовались")
			break
	else:
		print("Вы ввели неправильно логин или пароль")
print("Приветствуем вас на нашем сайте. Хотите войти или зарегестрироваться")
time.sleep(1.8)
while True:
	answer = n.intError("1 - войти\n2 - зарегестрироваться\n3 - выйти\n",1,3,1)
	if answer == 1:
		avtorise()
	elif answer == 2:
		register()
	else:
		print("До свидания")
		break
school_students.commit()

runner.close()
school_students.close()