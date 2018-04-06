from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)

# for files in os.listdir('C:\Python27\Lib\site-packages\chatterbot_corpus\data\Bangla/'):
#     data = open('C:\Python27\Lib\site-packages\chatterbot_corpus\data\Bangla/' + files , 'r').readlines()
#     bot.train(data)


while True:
    message = raw_input('You: ')
    if message.strip() != 'Bye':
        reply = bot.get_response(message)
        print 'ChatBot:' , reply
    if message.strip() == 'Bye':
        print'ChatBot : Bye'
        break

