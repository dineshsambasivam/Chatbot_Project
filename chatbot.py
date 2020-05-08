from chatterbot import ChatBot
#from chatterbot.trainers import ListTrainer


def get_response(usrText):
    bot = ChatBot('Bot',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": chatterbot.comparisons.levenshtein_distance,
            "response_selection_method": chatterbot.response_selection.get_first_response
        }
    ],
    trainer='chatterbot.trainers.ListTrainer')
    #bot.set_trainer(ListTrainer)
    while True:
        if usrText.strip()!= 'Bye':
            result = bot.get_response(usrText)                        
            reply = str(result)
            return(reply)
        if usrText.strip() == 'Bye':
            return('Bye')
            break
        

        
