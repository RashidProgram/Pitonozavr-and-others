import telebot
from random import choice
import time
a = False
b = False
c = False
lives = 0
quetions = 0

answer = "D"
	
markup = None


TOKEN = "475188685:AAG6YNADEpe9zMZDN9XANPNv774BO5tUWKk"


bot = telebot.TeleBot(TOKEN)


hello = ["Здравствуйте","Привет","Хай","Приветствую"]


dela = ["У меня все хорошо, а как дела у вас?","Отлично", "Все хорошо","Нормально или как по вашему норм"]



@bot.message_handler(commands = ["questions"])
def questions_game(message):
	global lives
	global quetions
	global answer
	global markup
	global a,b,c


	markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
	markup.add(*[telebot.types.KeyboardButton(name) for name in ['A',
		'B',
		'C']])

	bot.send_message(message.chat.id,"Это Мини игра в которой вы должены ответить на определеное количество вопросов. У вас будет 4 варианта ответа. У вас 3 жизни правильный ответ + 1 жизнь, неправильный - 1 жизнь. Если они у вас закончатся вы проигрываете.Удачи!!!")
	
	msg = bot.send_message(message.chat.id,"А - Фильмы\n В - Литература, С - Программирование", reply_markup=markup);
	
	bot.register_next_step_handler(msg, kek)
def kek(message):
	if message.text == "A":
		a = True
		b, c = False, False
		msg = bot.send_message(message.chat.id,"Вы выбрали жанр \"Фильмы\"");
		lives = 3
		quetions = 5 
		markup = telebot.types.ReplyKeyboardMarkup()
		markup.row('A', 'B')
		markup.row('C', 'D')
		
		answer = "D"
		
	elif message.text == "B":
		b = True
		a, c = False, False
		msg = bot.send_message(message.chat.id,"Вы выбрали жанр \"Литература\"");
		lives = 3
		quetions = 3
		markup = telebot.types.ReplyKeyboardMarkup()
		markup.row('A', 'B')
		markup.row('C', 'D')
		
		answer = "C"
		
		
	elif message.text == "C":
		a,b = False, False
		c = True
		msg = bot.send_message(message.chat.id,"Вы выбрали жанр \"Программиование\"");
		lives = 3
		quetions = 4
		markup = telebot.types.ReplyKeyboardMarkup()
		markup.row('A', 'B')
		markup.row('C', 'D')

	if c == True:
		if lives != 0:
			msg = bot.send_message(message.chat.id,"Что из этого не является языком програмирования:\nA - C++\nB - Objective\nC - СMS\nD - Delfi", reply_markup = markup)
			answer = "C"
			bot.register_next_step_handler(msg, game)		
		else:
			bot.send_message(message.chat.id,"Вы проиграли")
			return 0;

		if lives != 0: 
			msg = bot.send_message(message.chat.id,"Почему Java так назвали\nA - Марка кофе\nB - аббревиатура\nC - Марка кофемашинки\nD - Взяли у JavaScript", reply_markup = markup)
			
			answer = "C"

			bot.register_next_step_handler(msg, game)
		else:
			bot.send_message(message.chat.id,"Вы проиграли")
			return 0;
		

		if lives != 0:	
			msg = bot.send_message(message.chat.id,"Что такое HTML\nA - Язык Программирование\nB - Редактор Кода\nC - Вид CMS\nD - Язык Разметки", reply_markup = markup)
			
			answer = "D"

			bot.register_next_step_handler(msg, game)		
		else:
			bot.send_message(message.chat.id,"Вы проиграли")
			return 0;
		

		if lives != 0:
			msg = bot.send_message(message.chat.id,"for - это\nA - Ветвлени\nB - Функция\nC - Цикл\nD - Метод", reply_markup = markup)
			
			answer = "C"

			bot.register_next_step_handler(msg, game)			
		else:
			bot.send_message(message.chat.id,"Вы проиграли")
			return 0;
	
	elif a == True:
		if lives != 0:
			msg = bot.send_message(message.chat.id,"Сколько частей трансформеров было выпущенно \n A - 3\nB - 6\nC - 4\nD - 5", reply_markup = markup)
			
			answer = "D"

			bot.register_next_step_handler(msg, game)			
		else:
			bot.send_message(message.chat.id,"Вы проиграли")
			return 0;
		

		if lives != 0:	
			
			answer = "B"
			msg = bot.send_message(message.chat.id,"Как звали актера играющего Капитана Америку\nA - Тоби Магуайр\nB - Крис Эванс\nC - Роберт Дауни - младший\nD - Том Круз", reply_markup = markup)
			
			bot.register_next_step_handler(msg, game)		
		else:
			bot.send_message(message.chat.id,"Вы проиграли")
			return 0;
		

		if lives != 0:	
			msg = bot.send_message(message.chat.id,"В каком фильме из перечисленых был человек паук\nA - Мстителиn\nB - Первый мститель\nC - Черепашки ниндзя\nD - никаком ", reply_markup = markup)
			
			answer = "B"

			bot.register_next_step_handler(msg, game)
		else:
			bot.send_message(message.chat.id,"Вы проиграли")
			return 0;
		

		if lives != 0:	
			msg = bot.send_message(message.chat.id,"Режисер фильма \"Матрица\"\nA - Братья Гримм \nB - Стивенс Спилберг\nC - Братья Вачовски\nD - Джеймс Кемерон", reply_markup = markup)
			
			answer = "C"

			bot.register_next_step_handler(msg, game)			
		else:
			bot.send_message(message.chat.id,"Вы проиграли")
			return 0;
		if lives != 0:	
			msg = bot.send_message(message.chat.id,"Как в Гарри Потере называли человека, не волшебника.\nA - Сквиб\nB - Квид\nC - Мраксn\nD - Магл ", reply_markup = markup)
			
			answer = "D"

			bot.register_next_step_handler(msg, game)			
		else:
			bot.send_message(message.chat.id,"Вы проиграли")
			return 0;
	
	elif b == True:

		if lives != 0:
			msg = bot.send_message(message.chat.id,"Сколько томов \"Война и мир\" было написано \n A - 5\nB - 3\nC - 4\nD - 1", reply_markup = markup)
			text = message.text
			answer = "C"
			bot.register_next_step_handler(msg, game)			
		else:
			bot.send_message(message.chat.id,"Вы проиграли")
			return 0;
		
		
		if lives != 0:
			msg = bot.send_message(message.chat.id,"Кто написал Муму \n A - Ф.И Тютчев\nB - И.С.Тургенев\nC - А.С.Пушкин\nD - М.Ю.Лермонтов", reply_markup = markup)
			
			answer = "B"

			bot.register_next_step_handler(msg, game)
		else:
			bot.send_message(message.chat.id,"Вы проиграли")
			return 0;
		

		if lives != 0: 
			msg = bot.send_message(message.chat.id,"Как звали злодея из \"Мастер и Маргарита\" A - Гамель\nB - Мастер\nC - Синедрион\nD - Воланд", reply_markup = markup)
			
			answer = "D"

			bot.register_next_step_handler(msg, game)		
		else:
			bot.send_message(message.chat.id,"Вы проиграли")
			return 0;

	
def game(message):
	global lives
	global quetions
	global answer
	global markup
	global a,b,c

	userAnswer = message.text
	
	if userAnswer == answer:
		lives += 1
		quetions -= 1
		bot.send_message(message.chat.id,"Верно. Осталось",quetions,"вопросов и ",lives,"жизней")
	else:
		lives -= 1;
		quetions -= 1
		bot.send_message(message.chat.id,"Неверно. Осталось",quetions,"вопросов и ",lives,"жизней");

	



@bot.message_handler(commands = ["start"])
def start(message):
	bot.send_message(message.chat.id,"Бот запущен")
@bot.message_handler(commands = ["help"])
def help_commands(message):
	text = "Мой бот имеет несколько функций:\n\questions - бот задает вам вопросы а вы на них отвечаете\n\day - бот говорит какой сегодня день и время\nНу и конечно бот может с вами немного поболтать\nАвтор бота Велиханов Рашид"
	bot.send_message(message.chat.id, text)

@bot.message_handler(func = lambda message:True)
def my_message(message):
	message.text = message.text.lower()
	if "привет" in message.text:
		bot.send_message(message.chat.id, choice(hello))
	if "как дела" in message.text:
		bot.send_message(message.chat.id, choice(dela))
	if "Как тебя зовут" in message.text:
		bot.send_message(message.chat.id, "У меня нет имени, но можете называть меня Андрей")
	if "cколько" in message.text and "лет" in message.text:
		bot.send_message(message.chat.id, "Мой возраст: 3 дня")
if __name__ == "__main__":
	bot.polling()

