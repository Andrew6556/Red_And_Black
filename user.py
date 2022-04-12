import os
from write_and_read import read_json_file, write_json_file
from exceptions import*
from path_file import*

class User:

    @staticmethod
    def authenticate(name:str, password:int) -> object:
        try: 
            user_hash = read_json_file(USERS_PATH)[name]
        except KeyError:
            raise UserNameDoesNotExist
        
        if user_hash["password"] == password:
            return User(name, password)
        
        raise PasswordError

    def __init__(self, name:str , password:int, bank=0) -> None:
        self.username = name
        self.password = password
        self.bank = bank

    def authentication_checks(func):
        def wrapper(self):
            for user, data_us in read_json_file(USER_STATISTICS_GAME_PATH).items():
                if user == self.username and self.password == data_us['password']:
                    func(self)
                    break
            else:
                raise UserDoesNotAuthenticated
        return wrapper

    @authentication_checks
    def _finding_the_current_bank(self) -> None:
        for user, data_us in read_json_file(USER_STATISTICS_GAME_PATH).items():
            if user == self.username and self.password == data_us['password']:
                self.bank = data_us["current bank"]
                break 
        else:
            for user, data_us in read_json_file(USERS_PATH).items():
                if user == self.username and self.password == data_us['password']:
                    self.bank = data_us["bank"]
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
            if list(filter(lambda letter:letter.isdigit(), self.username)):
                raise IncorrectLoginNumbers    
            elif not self.username.startswith('@'):
                raise LoginStartsWithNoCharacters
            return fucn(self)
        return wrapper

    @checking_for_password_complexity
    @checking_for_correct_login
    def user_registration(self):

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
            
            return func(self, money, *args, **kwargs)
        return wrapper

    @bonus_on_adding
    def update_bank(self, money:int) -> None:
        self.bank += money
