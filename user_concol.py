from exceptions import*

class UserInterface:
    
    def __init__(self, user:object):
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
        except LoginStartsWithNoCharacters:
            print('Ваш логин должен начинаться с "@"')

    def print_bank(self):
        """Вывод текущего состояния банка"""
        print(f"Ваш текущий банк -- {self.user.bank}")

    def print_authorization(self, func):
        """Вывод результатов авторизации"""
        if func != None:
            print('Авторизация прошел успешна')
            self.user._finding_the_current_bank()
            return True
        else:
            print('Ошибка вводе данных')