import telebot
from random import choice
import time

lives = 0
quetions = 0

answer = "D"
	



TOKEN = "475188685:AAG6YNADEpe9zMZDN9XANPNv774BO5tUWKk"


bot = telebot.TeleBot(TOKEN)


hello = ["Здравствуйте","Привет","Хай","Приветствую"]


dela = ["У меня все хорошо, а как дела у вас?","Отлично", "Все хорошо","Нормально или как по вашему норм"]



@bot.message_handler(commands = ["questions"])
def questions_game(message):
	markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
	markup.add(*[telebot.types.KeyboardButton(name) for name in ['A',
		'B',
		'C']])

	bot.send_message(message.chat.id,"Это Мини игра в которой вы должены ответить на определеное количество вопросов. У вас будет 4 варианта ответа. У вас 3 жизни правильный ответ + 1 жизнь, неправильный - 1 жизнь. Если они у вас закончатся вы проигрываете.Удачи!!!")
	
	msg = bot.send_message(message.chat.id,"А - Фильмы\n В - Литература, С - Программирование", reply_markup=markup);
	
	bot.register_next_step_handler(msg, game)

def game(message):
	global lives
	global quetions
	global answer
	if message.text == "A":
		bot.send_message(message.chat.id,"Вы выбрали жанр \"Фильмы\"");
		lives = 3
		quetions = 5 
		markup = telebot.types.ReplyKeyboardMarkup()
		markup.row('A', 'B')
		markup.row('C', 'D')
		if lives != 0:
			msg = bot.send_message(message.chat.id,"Сколько частей трансформеров было выпущенно \n A - 3  B - 6  C - 4 D - 5", reply_markup = markup)
			print(message.text,lives,quetions,answer,"222")
			bot.register_next_step_handler(msg, prov)	
			print(message.text,lives,quetions,answer,"111")
		else:
			bot.send_message(message.chat.id,"Вы проиграли")
			return 0;
def prov(message):
	global lives
	global quetions
	global answer
	userAnswer = message.text
	print(message.text,lives,quetions,answer,"333")	
	if userAnswer == answer:
		lives += 1
		quetions -= 1
		bot.send_message(message.chat.id,"Верно. Осталось "+str(quetions)+"вопросов и "+str(lives)," жизней")
	else:
		lives -= 1;
		quetions -= 1
		bot.send_message(message.chat.id,"Неверно. Осталось "+str(quetions)+" вопросов и "+str(lives)+" жизней");

if __name__ == "__main__":
	bot.polling()