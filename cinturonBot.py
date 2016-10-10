# coding=utf-8
import telebot
import datetime
from telebot import types
global cinturon

cinturon= "258127468:AAGyTigu28F40W4RL2iVckia0mWsrvJu17Y"
markup = types.ReplyKeyboardMarkup(selective=True)
itembtna = types.KeyboardButton('tensian')
itembtnv = types.KeyboardButton('el novio mas fuerte del mundo')
itembtnc = types.KeyboardButton('agus el rojete')
itembtnd = types.KeyboardButton('forri el fachita')
itembtne = types.KeyboardButton('ortegote')
itembtnf = types.KeyboardButton('rafita')
itembtng = types.KeyboardButton('navarro, kappa')
itembtnh = types.KeyboardButton('server el que ya no consume')
itembtni = types.KeyboardButton('gine pollete')
markup.add(itembtna,itembtnv,itembtnc,itembtnd,itembtne,itembtnf,itembtng,itembtnh,itembtni)
bot= telebot.TeleBot("258127468:AAGyTigu28F40W4RL2iVckia0mWsrvJu17Y")
markup2= types.ForceReply(selective=False)
strs = ["" for x in range(20)]
votadosi=0
votadono=0
votados=0
votekick=False
idmesg=0
members=0
kickmember=0
chatid=0
@bot.message_handler(commands=['changecinturon'])
def send_welcome(message):
    if message.from_user.id == 5901753:
        m = bot.send_message(message.chat.id, 'quien es el rajao ahora? que le meto un navajasho'+" @eljiwo" , reply_markup=markup)
        bot.register_next_step_handler(m, answerjieo)
    else:
        bot.reply_to(message,"tu no eres el amo mamon")
def answerjieo(message):
    some_dict = {'tensian':'tensian','el novio mas fuerte del mundo':'el novio mas fuerte del mundo','agus el rojete':'agus el rojete','forri el fachita':'forri el fachita','ortegote':'ortegote','rafita':'rafita','navarro, kappa':'navarro, kappa','server el weedabo':'server el weedabo','gine pollete':'gine pollete'}
    if message.from_user.id == 5901753:
        if message.text in some_dict:
            bot.send_message(message.chat.id, 'ok')
            file = open('cinturon.txt', 'w')
            file.write(some_dict[message.text])
            file.close()
    else:
        bot.reply_to(message,"tu no eres el amo mamon")
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "no te ralles tete, siempre smile <3")
    
@bot.message_handler(commands=['pelea'])
def send_welcome(message):
    bot.send_message(message.from_user.id,"se va a be un follonaco bruter")
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "operativo y a sus ordenes senor franco")	
   
@bot.message_handler(commands=['currentcinturon'])
def send_welcome(message):
    cinturon = open('cinturon.txt').read()
    bot.reply_to(message,cinturon)


@bot.message_handler(commands=['votekicko'])
def send_welcome(message):
    global messag
    global kickmember
    messag=message.reply_to_message
    if ((messag is None)):
        bot.send_message(message.chat.id,'no reply, reply a message from the user u want to start voting for dick')
    else:
         bot.send_message(message.chat.id,'lululululuul')

         kickmember= str(messag.from_user.id)
         kickmember.replace("no","")
         global votekick 
         votekick=True
         chatid=message.chat.id
         bot.send_message(message.chat.id,'reply this shit with yes or no',reply_markup=markup2)
         

    
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    global votados
    global votadono
    global votadosi
    global votekick
    global lastday
    if 'wapo' in message.text:
        bot.reply_to(message,'me dejah velo primo?')
    elif 'chulo' in message.text:
        bot.reply_to(message,'me dejah velo primo?')
    elif message.text =='ping':
        bot.send_message(message.chat.id,'pong')
    elif 'camino de santiago' in message.text:
        bot.reply_to(message,'no hagas lena del arbol caido cabron')
    elif 'libertad' in message.text:
        bot.reply_to(message,'ortega libre')
    elif 'novio' in message.text:
        bot.reply_to(message,'pero ese novio esta mas fuerte que lillo?')
    elif 'espana' in message.text: 
        bot.send_message(message.chat.id,'casalla contra espanya')
    elif 'Espana' in message.text:
        bot.send_message(message.chat.id,'casalla contra espanya')
    elif 'podemos' in message.text:
        bot.send_message(message.chat.id,'que vienen los rojosssss')
    elif 'interrail' in message.text:
        bot.reply_to(message,'chu chu chuuu')
    elif 'novia de giner' in message.text:
        bot.reply_to(message,'yo aun no la he visto huehue')
    elif 'reply this shit with yes or no' in message.text:
        idmesg=message_id
    elif('yes' in message.text):
        
        if(votekick):
            if(message.from_user.id in strs):
                bot.send_message(message.chat.id,'already voted bru')
            else:
                votadosi+=1
                bot.send_message(message.chat.id,message.from_user.username+' voted yes')
                votados+=1
                strs[votados]=message.from_user.id
        if(votadosi==5):
                bot.kick_chat_member(messag.chat.id,kickmember)
                votekick=False
                strs.clear()

    elif('no' in message.text):
        
        if(votekick):
              if(message.from_user.id in strs):
                bot.send_message(message.chat.id,'already voted bru')
              else:
                bot.send_message(message.chat.id,message.from_user.username+' voted no')
                votadono+=1
                votados+=1
                strs[votados]=message.from_user.id
    elif('alberto' in message.text):
        bot.reply_to(message,'el que te deja el culo abierto hueheu')

    #elif('pole' in message.text):
    #     bot.send_message(message.chat.id,'subpole')
    #elif(datetime.datetime.now().time().hour==14):
    #    bot.send_message(message.chat.id,'subpole')        

   

bot.polling()
