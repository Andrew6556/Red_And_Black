from math import radians
import random
import time
from exceptions import NotCorrectColorIndex


class RedBlack:
    #класс Game - отвечает за всю логику программы
    
    def __init__(self, user_color_index, bet):
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

    def start_game(self):
        """
        Начало игры - перевешиваем числа,
        и рандомно выбираем выйгрышное число
        """
        self.__shuffle_game_box()
        self.game_number = self.__generate_number()

    def get_prize_color_bet(self):
        if (self.game_number in self.red_numbers and \
            self.user_number in self.red_numbers) or \
            (self.game_number in self.black_numbers and \
            self.user_number in self.black_numbers):
            return self.bet * 2

        elif self.game_number in self.green_numbers and \
            self.user_number in self.green_numbers:
            return self.bet * 14

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

    def __generate_number(self):
        """Генерируем выйграшное число"""
        return random.sample(self.game_box, 1)[0]

    @check_correct_index_color
    def __from_color_index_to_number(self, user_color_index):
        if user_color_index == 1:
            return random.sample(self.red_numbers, 1)[0]
        elif user_color_index == 2:
            return random.sample(self.black_numbers, 1)[0]
        return 0

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
    def checking_winning(self):
        game_result = self.game.get_prize_color_bet()
        if game_result < 0:
            print("К сожанию, вы проиграли")
        else:
            print("Поздравялем с победой!")

class User:

    def __init__(self, user_hash):
        self.username = user_hash["username"]
        self.bank = user_hash["bank"]

    def print_bank(self):
        print(f"Ваш банк -- {self.bank}")

    def update_user_bank(self, bet):
        return self.bank + bet
