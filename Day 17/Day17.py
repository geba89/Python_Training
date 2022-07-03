from mimetypes import init


class User:
    def __init__(self, username, id):
        self.username = username
        self.id = id
        self.followers = 0

    def print_info(self):
        print(f"Username: {self.username} / User ID: {self.id} / Followers count: {self.followers}")



user_1 = User("dupsko", "001")

user_1.print_info()