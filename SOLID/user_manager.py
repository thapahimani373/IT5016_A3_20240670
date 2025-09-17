class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserSaver:
    def save(self, user):
        print(f"Saving {user.name} to a file")  # Only saves – one job.

class UserEmailer:
    def send(self, user):
        print(f"Sending email to {user.email}")  # Only emails – one job.

# Analysis: Single Responsibility (SOLID) means each class does one thing. This keeps code clean and easy to fix – if saving breaks, only UserSaver needs work. I researched this and see it reduces bugs, which is great for my practice.
user = User("Emma", "emma@email.com")
saver = UserSaver()
emailer = UserEmailer()
saver.save(user)
emailer.send(user)
