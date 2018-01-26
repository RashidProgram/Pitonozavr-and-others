import telebot

TOKEN = "475188685:AAG6YNADEpe9zMZDN9XANPNv774BO5tUWKk"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(regexp="privet")
def answer(message):
	bot.send_message(message.chat.id, "Тебе тоже привет")

@bot.message_handler(func = lambda message:True)
def my_message(message):
	if "как дела" in message.text:
		bot.send_message(message.chat.id, "У меня хорошо! Как у тебя")
	
if __name__ == "__main__":
	bot.polling()