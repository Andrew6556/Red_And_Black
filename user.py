import os
from write_and_read import *



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