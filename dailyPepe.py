import telebot
import random
import datetime
from telebot import types
global cinturon

pepe="285650927:AAEsuGb5XkzG2WatFjaQdVWLULX3L4lWpYk"
bot=telebot.TeleBot(pepe)
def num(s):
    try:
        return int(s)
    except ValueError:
        return False
@bot.message_handler(commands=['randompepe'])
def send_Rpepe(message):
	type=random.randint(0,2)
	if(type == 0):
		id=random.randint(0,694)
		type=".jpg"
		dir="/home/pi/Desktop/Bots/pepes/jpg/"
		contador=id+526+32
	elif(type == 1):
		id=random.randint(0,526)
		type=".png"
		dir="/home/pi/Desktop/Bots/pepes/png/"
		contador=id+694+32
	elif(type == 2):
		id=random.randint(0,32)
		type=".gif"
		dir="/home/pi/Desktop/Bots/pepes/gif/"
		contador=id+526+694
	id=str(id)
	file= open(dir+id+type,'rb')
	bot.send_photo(message.chat.id, file);
	#bot.send_message(message.chat.id, 'pepe number: '+str(contador));
	file.close();
bot.polling()