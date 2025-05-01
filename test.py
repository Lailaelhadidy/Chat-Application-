from chat_app import ChatApp

app = ChatApp()

user1 = app.register_user("Alice", "alice@example.com")
user2 = app.register_user("Bob", "bob@example.com")
admin = app.register_user("Admin1", "admin@example.com", role="admin")

user1.send_message(user2, "Hello Bob!")
user2.send_message(user1, "Hi Alice!")

print("User1's Inbox before deletion:")
user1.view_inbox()
print("User2's Inbox before deletion:")
user2.view_inbox()

admin.delete_message(user2, user2.inbox[0])

print("User2's Inbox after deletion:")
user2.view_inbox()