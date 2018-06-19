from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

def setup():
    chatbot = ChatBot('Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    trainer='chatterbot.trainers.ListTrainer')
    for file in os.listdir('C:/Users/Yuvashree/Youtube_tutor/Chatbot/data/'):
        convData = open(r'C:/Users/Yuvashree/Youtube_tutor/Chatbot/data/' + file,encoding='latin-1').readlines()
        chatbot.set_trainer(ListTrainer)
        chatbot.train(convData)
        #print("Training completed")
    

setup()
