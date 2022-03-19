import os
import inspect
from write_and_read import*

class User:

    @staticmethod
    def user_authorization(name, password):
        "Авторизация пользователя"
        for users in read_json_file('registered_users.json'):
            if users["username"] == name and users["password"] == password:
                return User(name, password)
            
    def __init__(self, name , password, bank=0):
        self.username = name
        self.password = password
        self.bank = bank

    def _finding_the_current_bank(self):
        for users in read_json_file('game_user_statistics.json'):
            if users['username'] == self.username and users['password'] == self.password:
                self.bank = users["current bank"]
                break
        else:
            if os.stat(f'data/game_statistics.json').st_size:
                for users in read_json_file('registered_users.json'):
                    if users['username'] == self.username and users['password'] == self.password:
                        self.bank = users["bank"]
                        break

    def checking_for_password_complexity(func):
        """Проверяем на сложность пароль"""
        def wrapper(self):
            while len(str(self.password)) < 8:
                if len(str(self.password)) < 8:
                    print(inspect.cleandoc("""
                    Ваш пароль должен содержать минимум 8 символов"""))

                upgrade_password = int(input('Введите пароль(мин. 8 символов)\n'))
                self.password = upgrade_password

            return func(self)
        return wrapper

    def checking_for_correct_login(fucn):
        """Проверяем логин на корректность!
            без цифр, и должен начинаться с @
        """
        def wrapper(self):
            while True:
                if [i for i in self.username if i in ['0','1','2','3','4','5','6','7','8','9']]:
                    print(inspect.cleandoc("""
                            Вашем логине содержаться цифры - это не допустимо!
                            Напоминаю, ваш ник должен начинаться с "@" """
                            ))
                elif not self.username.startswith('@'):
                    print(inspect.cleandoc("""
                            Вашем логин должен начинаться с "@" !
                            Напоминаю, в логине не может быть цифр"""
                            ))
                else:
                    break
                
                correct_nickname = input('Введите корректный ник\n')
                self.username = correct_nickname
                
            return fucn(self)
        return wrapper

    @checking_for_password_complexity
    @checking_for_correct_login
    def user_registration(self):
        """Регистрация пользователя"""

        if os.stat(f'data/registered_users.json',).st_size:
            data = read_json_file('registered_users.json')
        else:
            data = []

        data.append({
            "username":self.username,
            "password":self.password,
            "bank":self.bank
        })

        write_json_file('registered_users.json', data)

    def update_user_bank(self, bet):
        return self.bank + bet

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
