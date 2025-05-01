from message import Message
class User():
    def __init__(self, username):
        self.__username= username
        self.inbox=[]

    def receive_message(self, message):
        self.inbox.append(message)

    def send_message(self, recipient, content):
        message = Message(self.__username, recipient.__username, content)
        recipient.recieve_message(message)

    def view_inbox(self):
        for i in range(len(self.inbox)):
            message= self.inbox[i]
            print( f" From: {message.sender.username}, content: {message.content}")