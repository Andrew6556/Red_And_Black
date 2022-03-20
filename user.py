import os
import inspect
from write_and_read import*
from exceptions import*
from path_file import*

class User:

    @staticmethod
    def user_authorization(name, password):
        "Авторизация пользователя"
        for users in read_json_file(USERS_PATH):
            if users["username"] == name and users["password"] == password:
                return User(name, password)
            
    def __init__(self, name , password, bank=0):
        self.username = name
        self.password = password
        self.bank = bank

    def _finding_the_current_bank(self):
        for users in read_json_file(USERS_PATH):
            if users['username'] == self.username and users['password'] == self.password:
                self.bank = users["current bank"]
                break
        else:
            if os.stat(f'data/{GAME_STATISTICS_PATH}').st_size:
                for users in read_json_file(USERS_PATH):
                    if users['username'] == self.username and users['password'] == self.password:
                        self.bank = users["bank"]
                        break
    
    def checking_for_password_complexity(func):
        """Проверяем на сложность пароль"""
        def wrapper(self):
            if len(str(self.password)) < 8:
                raise IncorrectPasswordEntry
            return func(self)
        return wrapper

    def checking_for_correct_login(fucn):
        """Проверяем логин на корректность!
            без цифр, и должен начинаться с @
        """
        def wrapper(self):
            
            if [i for i in self.username if i in ['0','1','2','3','4','5','6','7','8','9']]:
                raise IncorrectLoginNumbers    
            elif not self.username.startswith('@'):
                raise LoginStartsWithNoCharacters

            return fucn(self)
        return wrapper

    @checking_for_password_complexity
    @checking_for_correct_login
    def user_registration(self):
        """Регистрация пользователя"""

        if os.stat(f'data/{USERS_PATH}',).st_size:
            data = read_json_file(USERS_PATH)
        else:
            data = {}

        data.update({
            self.username:{
                "password":self.password,
                "bank":self.bank
                }
                })
        write_json_file(USERS_PATH, data)

    def bonus_on_adding(func):
        """Бонус к сумме при 1000"""
        def wrapper(self, money, *args, **kwargs):
            if money >= 1000:
                money += 100
                print(money)
            
            return func(self, money, *args, **kwargs)
        return wrapper

    @bonus_on_adding
    def update_bank(self, money):
        self.bank += money

class UserInterface:

    def __init__(self, user):
        self.user = user 
    
    def correct_password_processing(self):
        try:
            self.user.user_registration()
        except IncorrectPasswordEntry:
            print('Ваш пароль должен содержать цифр 8')

    def error_message_in_login(self):
        try:
            self.user.user_registration()
        except IncorrectLoginNumbers:
            print('Ваш логин не должен содержать цифр')
            return False
        except LoginStartsWithNoCharacters:
            print('Ваш логин должен начинаться с "@"')

    def print_bank(self):
        """Вывод текущего состояния банка"""
        print(f"Ваш текущий банк -- {self.user.bank}")

    def print_authorization(self, func):
        """Вывод результатов авторизации"""

        if func == True:
            print('Авторизация прошел успешна')
            self.user._finding_the_current_bank()
            return True
        else:
            print('Ошибка вводе данных')
            return False
