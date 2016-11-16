import telebot
import random
import datetime
from telebot import types
global cinturon

pepe="285650927:AAEsuGb5XkzG2WatFjaQdVWLULX3L4lWpYk"
bot=telebot.TeleBot(pepe)
@bot.message_handler(commands=['randompepe'])
def send_Rpepe(message):
	id=random.randint(0,1000);
	file= open(id+".jpg",r)
	bot.send_photo(message.chat.id, file);
	file.close();
bot.polling()
