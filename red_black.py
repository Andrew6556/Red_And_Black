import random
import time
import os
from math import radians
from write_and_read import*
from exceptions import NotCorrectColorIndex
from path_file import*

class RedBlack:
    #класс Game - отвечает за всю логику программы
    
    def __init__(self, user_color_index, bet, user_number_bet=0):
        # список красный числе от 1 до 50
        self.red_numbers = [number for number in range(1, 51)]
        # список черных числе от 50 до 100
        self.black_numbers = [number for number in range(51, 101)]
        # список зеленых числел
        self.green_numbers = [0 for number in range(15)]#генерерирует список их 15 нулей
        #массив всех чисел
        self.game_box = self.red_numbers + self.black_numbers + self.green_numbers
        #ставка пользователя
        self.bet = bet
        self.user_number = self.__from_color_index_to_number(user_color_index)
        self.user_bet_number = user_number_bet

    def start_game(self):
        """
        Начало игры - перевешиваем числа,
        и рандомно выбираем выйгрышное число
        """
        self.__shuffle_game_box()
        self.game_number = self.__generate_number()

    def get_prize_color_bet(self):
        """Результат ставки - выйграл или проиграл"""
        #если игровое число,есть в красном списке и
        #число пользователя,есть в красном списке то он выйграл
        if (self.game_number in self.red_numbers and \
            self.user_number in self.red_numbers) or \
            (self.game_number in self.black_numbers and \
            self.user_number in self.black_numbers):
            return self.bet * 2

        elif self.game_number in self.green_numbers and \
            self.user_number in self.green_numbers:
            return self.bet * 14

        return -self.bet

    def get_prize_number_bet(self):
        if self.game_number == self.user_number:
            return self.bet * 20

        return -self.bet


    def check_correct_index_color(function):
        """Обработка неправильного ввода"""

        def wrapper(self, user_color_index, *args, **kwargs):
            if user_color_index not in range(0, 3):
                raise NotCorrectColorIndex("Введите корректный индекс цвета")
            return function(self, user_color_index, *args, **kwargs)

        return wrapper

    def __shuffle_game_box(self):
        """
            Перемешиваем все числа
            Теперь у нас полноценная рулетка :)
        """
        return random.shuffle(self.game_box)
        #random.shuffle перемешивает список

    def __generate_number(self):
        """Генерируем выйграшное число"""
        return random.sample(self.game_box, 1)[0]# <= Возращает не массив с чиcлом ,а только число
        #random.sample берет массив за первый аргумент 
        #и из него возращет рандомный список чисел(смотря скок надо)
        

    @check_correct_index_color
    def __from_color_index_to_number(self, user_color_index):
        if user_color_index == 1:
            return random.sample(self.red_numbers, 1)[0]
        elif user_color_index == 2:
            return random.sample(self.black_numbers, 1)[0]
        return 0

    def color_game(func):
        """заменяем индекс выбранного цвета на сам цвет"""
        def wrapper(self, name, password, user_bank,
                        color, *args, **kwargs):
            if color == 0:
                color='green'
            elif color == 1:
                color='red'

            elif color == 2:
                color='black'
            
            func(self, name, password, user_bank, color, *args, **kwargs)
        return wrapper

    def result_game_past(func):
        """Конечный результат игры для записи в Json"""
        def wrapper(self, name, password,  start_bank,
                    color, end_bank, *args, **kwargs):
            
            if end_bank > start_bank:
                result='win'
            else:
                result='lose'
                
            func(self, name, password, start_bank, color,
                end_bank, result, *args, **kwargs)
        return wrapper

    @result_game_past
    @color_game
    def adding_user_data(self, username, password, start_bank,
                        color, end_bank, result):
        
        """Сохранения данных пользователя"""
        
        data = read_json_file(f'{USER_STATISTICS_GAME_PATH}')
        for users, data_us in data.items():
            if users == username and data_us["password"] == password:
                data_us["history start bank"].append(start_bank)
                data_us["bet"].append(self.bet)
                data_us["color"].append(color)
                data_us["history end bank"].append(end_bank)
                data_us["result"].append(result)
                data_us["current bank"] = end_bank
                break
            
        else:
            # если нет ,то добавляем usera в базу данных
            data.update({
                "username":{
                    "password":password,
                    "history start bank":[start_bank],
                    "bet":[self.bet],
                    "color":[color],
                    "history end bank":[end_bank],
                    "result":[result],
                    "current bank":end_bank
                    }
                })

        write_json_file(f'{USER_STATISTICS_GAME_PATH}', data)

    @result_game_past
    @color_game
    def adding_data_about_the_past_game(self, user_name, password, start_bank,
                                        color, end_bank, result):

        if os.stat(f'data/{GAME_STATISTICS_PATH}').st_size:
            data = read_json_file(f'{GAME_STATISTICS_PATH}')
        else:
            data = {}

        data.update({
                    user_name:{
                        "initial bank":start_bank,
                        "bet":self.bet,
                        "color":color,
                        "end bank":end_bank,
                        "result": result
                    }
                })   

        write_json_file(f'{GAME_STATISTICS_PATH}', data)
class GameInteface:
    
    def __init__(self, game):
        self.game = game
    
    def drop_effect(function):
        def wrapper(self, *args, **kwargs):
            game_number_index = self.game.game_box.index(self.game.game_number)
            print_time = 20 + random.randint(0, 20)
            if game_number_index >= print_time:
                numbers = self.game.game_box[game_number_index - 20:game_number_index]
            else:
                numbers = self.game.game_box[game_number_index: game_number_index + 20]

            for index, number in enumerate(numbers, 1):
                print(f"{number}\n", end='')
                time.sleep(.1 + index/25)
                
            return function(self, *args, **kwargs)

        return wrapper

    @drop_effect
    def game_result_information(self):
        if self.game.game_number in self.game.red_numbers:
            print(f"Выпало красное -- {self.game.game_number}")
        elif self.game.game_number in self.game.black_numbers:
            print(f"Выпало чёрное -- {self.game.game_number}")
        else:
            print(f"Выпало зелёное -- {self.game.game_number}")

    @drop_effect
    def number_pick_game_result(self):
        if self.game.game_number == self.game.user_bet_number or \
            self.game.game_number != self.game.user_bet_number:
            print(f"Выпало -- {self.game.game_number}")

    def number_game_result(self):
        game_result = self.game.get_prize_color_bet()
        if game_result < 0:
            print("К сожанию, вы проиграли")
        else:
            print("Поздравялем с победой!")

    def checking_winning(self):
        game_result = self.get_prize_number_bet()
        if game_result < 0:
            print("К сожанию, вы проиграли")
        else:
            print("Поздравялем с победой!")

