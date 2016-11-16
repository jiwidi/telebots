import telebot
import random
import datetime
from telebot import types
global cinturon

pepe="285650927:AAEsuGb5XkzG2WatFjaQdVWLULX3L4lWpYk"
bot=telebot.TeleBot(pepe)
@bot.message_handler(commands=['randompepe'])
def send_Rpepe(message):
	type=random.randint(0,2)
	if(type is 0)
		id=random.randint(0,1000)
		type=".jpg"
	elif(type is 1)
		id=random.randint(0,1000)
		type=".png"
	elif(type is 2)
		id=random.randint(0,1000)
		type=".gif"
	file= open(id+type,r)
	bot.send_photo(message.chat.id, file);
	file.close();
bot.polling()