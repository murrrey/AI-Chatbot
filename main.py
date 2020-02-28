from chatterbot.trainers import ChatterBotCorpusTrainer #method to train the chat bot
from chatterbot import ChatBot #import the chatbot
import os
bot = ChatBot('Test') #create the chatbot

trainer = ChatterBotCorpusTrainer(bot) #set the trainer
for _file in os.listdir('files'):
    chats = open('files/' + _file, 'r').readlines()


trainer.train("chatterbot.corpus.english")


while True:
    request = input('You: ')
    response = bot.get_response(request)

    print('Bonni:', response)
