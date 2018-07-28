from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
from chatbot import get_response


class ChatServer(WebSocket):

    def handleMessage(self):
        # echo message back to client
        message = self.data
        response = get_response(message)
        self.sendMessage(response)

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')



server = SimpleWebSocketServer('', 8000, ChatServer)
server.serveforever()
