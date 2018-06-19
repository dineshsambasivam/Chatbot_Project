from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import random

bye = [ "Bye", "bye","BYE", "See you", "Thank You","thank you","thankyou","thanks","THANK YOU","THANKS","THANKYOU"]
bye_responses = [ "Bye.Thanks for using Chatbot." , "Welcome. Thanks for using Chatbot."]

greetings = ["hi","Hi","HI"]
greetings_responses = ["Hello. I'm Chatbot. How can i help you?."]


def get_response(usrText):

    bot = ChatBot('MyBot',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.70,
            'default_response': 'I am sorry, but I do not understand.'
        }
    ],
    trainer='chatterbot.trainers.ListTrainer')
    bot.set_trainer(ListTrainer)
    while True:
        if usrText.strip() in bye:
            return random.choice(bye_responses)
            break
        if usrText.strip() in greetings:
            return random.choice(greetings_responses)
            break
        if usrText.strip() not in bye and usrText.strip() not in greetings:
            result = bot.get_response(usrText)                        
            reply = str(result)
            return(reply)
        
