from user import User
from admin import Admin

class ChatApp:
    def __init__(self):
        self.users=[]

    def register_user(self, username, role='user'):
        if role == 'Admin':
            user = Admin(username)
        else:
            user = User(username)
        self.users.append(user)
        return user

    def find_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None