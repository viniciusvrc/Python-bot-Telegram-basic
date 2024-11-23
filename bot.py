#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# encoding: utf-8
#import modulo1
import time
import random
import telepot
bot = telepot.Bot('Coloca o token aqui')

def parametros(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == "new_chat_member":
        bot.sendMessage(chat_id, random.choice(["credits - @viniciusvrc"]))
    try:bemvindo = msg['chat']['title']
    except:
        bemvindo= msg['chat']['id']
    msg_id= msg['message_id']
    chat_id = msg['chat']['id']
    comando = msg['text']
    print 'Menssagem: %s' % comando

    if comando == '/ping' :
        bot.sendMessage(chat_id, "Estou ativo")


bot.message_loop(parametros)
print 'bot iniciado'
while 1:
    time.sleep(10)