class Account:

    def __init__(self, login, pw):
        self.login = login
        self.__password = pw

    def is_correct_password(self, pw):
        return self.__password == pw
