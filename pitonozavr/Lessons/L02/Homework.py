def filmi(lives = 3,quetions = 5):
	if lives != 0:		
		answer = input("Сколько частей трансформерров было выпущенно \n а.3  Б.6  в.4 г.5").lower().strip()
		if "5" == answer or answer == "г":
			lives += 1;
			quetions -= 1
			print("Верно. Осталось",quetions,"вопросов и ",lives,"жизней")
		elif otveti == True:
			lives -= 1;
			quetions -= 1
			print ("Неверно. Правильнй ответ 5. Осталось",quetions,"вопросов и ",lives,"жизней");
		else:
			lives -= 1;
			quetions -= 1
			print ("Неверно. Осталось",quetions,"вопросов и ",lives,"жизней");
	else:
		print("Вы проиграли")
		return 0;
	if lives != 0:	
		answer = input("Как звали актера играющего Капитана Америку a.Тоби Магуайр  б.Крис Эванс  в.Роберт Дауни - младший г.Том Круз").lower().strip()
		if answer == "крис эванс" or answer == "крис" or answer == "б":
			lives += 1;
			quetions -= 1
			print("Верно. Осталось",quetions,"вопросов и ",lives,"жизней")
		elif otveti == True:
			lives -= 1;
			quetions -= 1
			print ("Неверно. Правильнй ответ Крис Эванс. Осталось",quetions,"вопросов и ",lives,"жизней")	
		else:
			lives -= 1;
			quetions -= 1
			print ("Неверно. Осталось",quetions,"вопросов и ",lives,"жизней");
	else:
		print("Вы проиграли")
		return 0;
	if lives != 0:	
		answer = input("В каком фильме из перечисленых был человек паук a.Мстители  б.Первый мститель  в.Черепашки ниндзя г.никаком ").lower().strip()
		if answer == "первый мститель" or answer == "первыймститель" or answer == "б":
			lives += 1;
			quetions -= 1
			print("Верно. Осталось",quetions,"вопросов и ",lives,"жизней")
		elif otveti == True:
			lives -= 1;
			quetions -= 1
			print ("Неверно. Правильнй ответ Крис Эванс. Осталось",quetions,"вопросов и ",lives,"жизней")	
		else:
			lives -= 1;
			quetions -= 1
			print ("Неверно. Осталось",quetions,"вопросов и ",lives,"жизней");
	else:
		print("Вы проиграли")
		return 0;
	if lives != 0:	
		answer = input("Режисер фильма \"Матрица\" a.Братья Гримм  б.Стивенс Спилберг  в.Братья Вачовски г.Джеймс Кемерон ").lower().strip()
		if answer == "братья вачовски" or answer == "вачовски" or answer == "в":
			lives += 1;
			quetions -= 1
			print("Верно. Осталось",quetions,"вопросов и ",lives,"жизней")
		elif otveti == True:
			lives -= 1;
			quetions -= 1
			print ("Неверно. Правильнй ответ Крис Эванс. Осталось",quetions,"вопросов и ",lives,"жизней")	
		else:
			lives -= 1;
			quetions -= 1
			print ("Неверно. Осталось",quetions,"вопросов и ",lives,"жизней");
	else:
		print("Вы проиграли")
		return 0;
	if lives != 0:	
		answer = input("Как  в Гарри Потере называли человека, не волшебника. a.Сквиб  б.Квид  в.Мракс г.Магл ").lower().strip()
		if answer == "магл" or answer == "г":
			lives += 1;
			quetions -= 1
			print("Верно. Осталось",quetions,"вопросов и ",lives,"жизней")
		elif otveti == True:
			lives -= 1;
			quetions -= 1
			print ("Неверно. Правильнй ответ Крис Эванс. Осталось",quetions,"вопросов и ",lives,"жизней")	
		else:
			lives -= 1;
			quetions -= 1
			print ("Неверно. Осталось",quetions,"вопросов и ",lives,"жизней");
	else:
		print("Вы проиграли")
		return 0;
def literatura(lives = 3,quetions = 3):
	if lives != 0:
		answer = input("Сколько томов \"Война и мир\" было написано \n a.5  б.3  в.4  г.1").lower().strip()
		if "4" == answer or answer == "в":
			lives += 1;
			quetions -= 1
			print("Верно. Осталось",quetions,"вопросов и ",lives,"жизней")
		elif otveti == True:
			lives -= 1;
			quetions -= 1
			print ("Неверно. Правильнй ответ 4. Осталось",quetions,"вопросов и ",lives,"жизней")
		else:
			lives -= 1;
			quetions -= 1
			print ("Неверно. Осталось",quetions,"вопросов и ",lives,"жизней");
	else:
		print("Вы проиграли")
		return 0;
	if lives != 0:
		answer = input("Кто написал Муму \n а. Ф.И Тютчев б. И.С.Тургенев в. А.С.Пушкин г. М.Ю.Лермонтов").lower().strip()		
		if answer == "тургенев" or answer == "и.с.тургенев" or answer == "б":
			lives += 1;
			quetions -= 1
			print("Верно. Осталось",quetions,"вопросов и ",lives,"жизней")
		elif otveti == True:
			lives -= 1;
			quetions -= 1
			print ("Неверно. Правильнй ответ Тургенев. Осталось",quetions,"вопросов и ",lives,"жизней")
		else:
			lives -= 1;
			quetions -= 1
			print ("Неверно. Осталось",quetions,"вопросов и ",lives,"жизней");
	else:
		print("Вы проиграли")
		return 0;
	if lives != 0:
		answer = input("Как звали злодея из \"Мастер и Маргарита\" а.Гамель б.Мастер в.Синедрион г.Воланд").lower().strip()		
		if answer == "воланд" or answer == "г":
			lives += 1;
			quetions -= 1
			print("Верно. Осталось",quetions,"вопросов и ",lives,"жизней")
		elif otveti == True:
			lives -= 1;
			quetions -= 1
			print ("Неверно. Правильнй ответ Тургенев. Осталось",quetions,"вопросов и ",lives,"жизней")
		else:
			lives -= 1;
			quetions -= 1
			print ("Неверно. Осталось",quetions,"вопросов и ",lives,"жизней");
	else:
		print("Вы проиграли")
		return 0;		
def programmirovanie(lives = 3,quetions = 4):
	if lives != 0:
		answer = input("Что из этого не является языком програмирования: а.C++ б.Objective C в.СMS  г.Delfi").lower().strip()
		if answer == "cms" or answer == "в":
			print("Верно. Осталось",quetions,"вопросов и ",lives,"жизней")
			lives += 1;
			quetions -= 1
		elif otveti == True:
			lives -= 1;
			quetions -= 1
			print ("Неверно. Правильнй ответ цикл. Осталось",quetions,"вопросов и ",lives,"жизней")
		else:	
			lives -= 1;
			quetions -= 1
		print ("Неверно. Осталось",quetions,"вопросов и ",lives,"жизней");
	else:
		print("Вы проиграли")
		return 0;
	if lives != 0:
		answer = input("Почему Java так назвали а. Марка кофе Б.аббревиатура в. Марка кофемашинки г.Взяли у JavaScript").lower().strip()
		if "марка кофе" == answer or answer == "а":
			lives += 1;
			quetions -= 1
			print("Верно. Осталось",quetions,"вопросов и ",lives,"жизней")
		elif otveti == True:
			lives -= 1;
			quetions -= 1
			print ("Неверно. Правильнй ответ Марка кофе. Осталось",quetions,"вопросов и ",lives,"жизней")
		else:
			lives -= 1;
			quetions -= 1
			print("Неверно. Осталось",quetions,"вопросов и ",lives,"жизней");
	else:
		print("Вы проиграли")
		return 0;
	if lives != 0:	
		answer = input("Что такое HTML a.Язык Программирование  б.Редактор Кода  в.Вид CMS г.Язык Разметки").lower().strip()
		if answer == "язык разметки" or answer == "разметка" or answer == "г":
			lives += 1;
			quetions -= 1
			print("Верно. Осталось",quetions,"вопросов и ",lives,"жизней")
		elif otveti == True:
			lives -= 1;
			quetions -= 1
			print ("Неверно. Правильнй ответ язык разметки. Осталось",quetions,"вопросов и ",lives,"жизней")	
		else:
			lives -= 1;
			quetions -= 1
			print ("Неверно. Осталось",quetions,"вопросов и ",lives,"жизней");
	else:
		print("Вы проиграли")
		return 0;
	if lives != 0:
		answer = input("for - это а. Ветвление б. Функция в. Цикл г. Метод").lower().strip()
		if answer == "цикл" or answer == "в":
			print("Верно. Осталось",quetions,"вопросов и ",lives,"жизней")
			lives += 1;
			quetions -= 1
		elif otveti == True:
			lives -= 1;
			quetions -= 1
			print ("Неверно. Правильнй ответ цикл. Осталось",quetions,"вопросов и ",lives,"жизней")
		else:	
			lives -= 1;
			quetions -= 1
		print ("Неверно. Осталось",quetions,"вопросов и ",lives,"жизней");
	else:
		print("Вы проиграли")
		return 0;

print("Это квест в котором ты должен ответить на определеное количество вопросов. У вас будет 4 варианта ответа вы можете ответить как буквой(а,б,в или г) так и самим ответом. У вас 3 жизни правильный ответ + 1 жизнь, неправильный - 1 жизнь. Если они у вас закончатся вы проигрываете.Удачи!!!")
yesOrNo = input("Если хотите узнавать правильные ответы после ошибок напишите Да").lower().strip()
import random
if yesOrNo == "да":
	otveti = True;
else:
	otveti = False;

randomInt = random.randint(1,3)
print("Выберете жанр. Если не выберете он быдет выбран рандомно.")
genre = input("Литература, Фильмы или Программирование").lower().strip();
if genre !="литература" and genre !="программирование" and genre !="фильмы" and randomInt == 1 and genre !="програмирование" :
	genre = "литература"
elif genre !="литература" and genre !="программирование" and genre !="фильмы" and randomInt == 2 and genre !="програмирование" :
	genre = "фильмы";		
elif genre !="литература" and genre !="программирование" and genre !="фильмы" and randomInt == 3 and genre !="програмирование" :
	genre = "программирование";

if genre == "литература":
	print("Вы выбрали жанр \"Литература\" ");
	literatura() 
elif genre == "фильмы":
	print("Вы выбрали жанр \"Фильмы\"");
	filmi()
elif genre == "программирование" or genre =="програмирование" :
	print("Вы выбрали жанр \"Программиование\"");
	programmirovanie()
