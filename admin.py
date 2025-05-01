from setuptools.discovery import chain_iter

from user import User
class Admin(User):
    def __init__(self, username, user_lists):
        super().__init__(username)
        self.user_lists= user_lists

    def delete_message(self, user, message):
        """for i in range(len(user.inbox)):
            if user.inbox[i].content == message.content and user.inbox[i].sender == message.sender:
                user.inbox[i].pop(i)
                print(f"Message deleted from {user.username}s inbox")
                return"""
        if message in user.inbox:
            user.inbox.remove(message)
            print(f" message from {message.sender.username} to {user.username} deleted")

    def delete_user(self, chat_app, user):
        """for i in range(len(self.user_lists)):
            if self.user_lists[i].username == user.username:
                self.user_lists[i].pop(i)
                print(f" user {user.username} is deleted")
                return"""
        if user in chat_app.users: #same of loop
            chat_app.users.remove(user)
            print(f" user {user.username} deleted")
        else:
            print(f" username not found ")