# Chatbot_Project
## ChatBot with interactive UI using simple web socket server 
### Description of files
* Chatbot_train.py file trains the data available in the data folder. Once it is trained , the result will be stored as db.sqlite.
* Chatbot.py uses this db.sqlite to generate responses for user queries.
* server.py sends back message to the client.

### How to run
* Once you downloaded this project , Make sure you install the python packages mentioned in requirement.txt.
* Go to Chatbot_Project directory and run python server.py.
* Above step will open the server. Now right click the index.html page and open with brower. You will be able to see the chat window where you can start the conversation and test.
