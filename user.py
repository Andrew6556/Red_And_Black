import os
from write_and_read import*


class User:
    
    @staticmethod
    def user_authorization(name, password):
        for users in read_json_file('registered_users.json'):
            if users["name"] == name and users["password"] == password:
                return True
            
            else:
                continue

    def __init__(self, user_hash):
        self.username = user_hash["username"]
        self.password = user_hash["password"]
        self.bank = user_hash["bank"]

    def color_game(func):
        """заменяем индекс выбранного цвета на сам цвет"""
        def wrapper(self, name, user_bank,
                        color, *args, **kwargs):
            if color == 0:
                color='green'
            elif color == 1:
                color='red'

            elif color == 2:
                color='black'
            func(self, name, user_bank, color, *args, **kwargs)
        return wrapper

    def result_game_past(func):
        """Конечный результат игры для записи в Json"""
        def wrapper(self, start_bank,
                    color, end_bank, *args, **kwargs):
            if end_bank > start_bank:
                result='win'
            else:
                result='lose'
            func(self, start_bank, color, end_bank, result, *args, **kwargs)
        return wrapper

    @result_game_past
    @color_game
    def adding_user_data(self, start_bank, color,
                        bet, result):
        """Сохранения данных пользователя"""
        if os.stat('data/game_user_statistics.json',).st_size:
            data = read_json_file('game_user_statistics.json')
        else:
            data = []

        # for users_data in read_json_file('game_user_statistics.json'):
        #     if users_data["username"] == self.username and \
        #         users_data["password"] == self.password:
        #         print('a')
        #     else:
        #         data.append({
        #             "username":self.username,
        #             "initial bank":start_bank,
        #             "bet":self.bet,
        #             "color":color,
        #             "end bank":end_bank,
        #             "result": result
        #         })
        data.append({
                    "username":self.username,
                    "initial bank":start_bank,
                    "bet":bet,
                    "color":color,
                    "end bank":self.bank,
                    "result": result
                })   

        write_json_file('game_user_statistics.json', data)

    def user_registration(self):
        """Регистрация пользователя"""

        if os.stat(f'data/registered_users.json',).st_size:
            data = read_json_file('registered_users.json')
        else:
            data = []

        data.append({
            "username":self.username,
            "password":self.password
        })

        write_json_file('registered_users.json', data)

    def update_user_bank(self, bet):
        return self.bank + bet

class UserInterface:

    def __init__(self, user):
        self.user = user 
        
    def print_bank(self):
        """Вывод текущего состояния банка"""
        print(f"Ваш банк -- {self.user.bank}")