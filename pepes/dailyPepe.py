import telebot
import random
import os
import glob
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
@bot.message_handler(commands=['getpepe'])
def send_Pepe(message):
    number=message.text[8:]
    aux=int(float(number))
    if(aux>=0 and aux<=1252):
        number=number.strip();
        filename = glob.glob(number+'*.*')
        extension= os.path.splitext(filename[0])[1]
        file= open(filename[0],'rb')
    
        if(extension==".gif"):
            bot.send_document(message.chat.id,file)
        else:
            file= open(filename[0],'rb')
            bot.send_photo(message.chat.id, file);
        file.close()
    else:
        bot.send_message(message.chat.id,'wrong number');
@bot.message_handler(commands=['randompepe'])
def send_Rpepe(message):
    id=random.randint(0,1252)
    dir='/home/jiwidi/GITHUB/telebots/pepes'
    id=str(id)
    filename = glob.glob(id+'*.*')
    file= open(filename[0],'rb')
    extension= os.path.splitext(filename[0])[1]
    if(extension==".gif"):
        bot.send_document(message.chat.id,file)
    else:
        bot.send_photo(message.chat.id, file);
        bot.send_message(message.chat.id, 'pepe number: '+str(id));
    file.close();
bot.polling()