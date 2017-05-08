import telebot
import datetime
from telebot import types
global cinturon

bot= telebot.TeleBot("")
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
@bot.message_handler(commands=['votekick'])
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
    if('yes' in message.text):
        
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
                strs=[]

    elif('no' in message.text):
        
        if(votekick):
              if(message.from_user.id in strs):
                bot.send_message(message.chat.id,'already voted bru')
              else:
                bot.send_message(message.chat.id,message.from_user.username+' voted no')
                votadono+=1
                votados+=1
                strs[votados]=message.from_user.id
    

    #elif('pole' in message.text):
    #     bot.send_message(message.chat.id,'subpole')
    #elif(datetime.datetime.now().time().hour==14):
    #    bot.send_message(message.chat.id,'subpole')        

   

bot.polling()
