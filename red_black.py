import random
import os
from math import radians
from write_and_read import*
from exceptions import NotCorrectColorIndex
from path_file import*

class RedBlack:
    #класс Game - отвечает за всю логику программы
    
    def __init__(self, bet:int, user_color_index=0 , user_number_bet='') -> None:
        self.red_numbers = [number for number in range(1, 51)]
        self.black_numbers = [number for number in range(51, 101)]
        self.green_numbers = [0 for number in range(15)]

        self.game_box = self.red_numbers + self.black_numbers + self.green_numbers

        self.bet = bet

        self.user_number = self.__from_color_index_to_number(user_color_index)
        self.user_number_bet = user_number_bet

    def start_game(self) -> list:
        """
        Начало игры - перевешиваем числа,
        и рандомно выбираем выйгрышное число
        """
        self.__shuffle_game_box()
        self.game_number = self.__generate_number()

    def get_prize_color_bet(self) -> int:
        if (self.game_number in self.red_numbers and \
            self.user_number in self.red_numbers) or \
            (self.game_number in self.black_numbers and \
            self.user_number in self.black_numbers):
            return self.bet * 2

        elif self.game_number in self.green_numbers and \
            self.user_number in self.green_numbers:
            return self.bet * 14

        return -self.bet

    def get_prize_number_bet(self) -> int:
        if self.game_number == self.user_number_bet:
            return self.bet * 30

        return -self.bet

    def check_correct_index_color(function):
        def wrapper(self, user_color_index, *args, **kwargs):
            if user_color_index not in range(0, 3):
                raise NotCorrectColorIndex("Введите корректный индекс цвета")
            return function(self, user_color_index, *args, **kwargs)

        return wrapper

    def __shuffle_game_box(self) -> list:
        return random.shuffle(self.game_box)

    def __generate_number(self) -> int:
        """Генерируем выйграшное число"""
        return random.sample(self.game_box, 1)[0]

    @check_correct_index_color
    def __from_color_index_to_number(self, user_color_index:int) -> int:
        if user_color_index == 1:
            return random.sample(self.red_numbers, 1)[0]
        elif user_color_index == 2:
            return random.sample(self.black_numbers, 1)[0]
        return 0

    def _color_game(self, color: int) -> str:
        return ['green', 'red', 'black'][color] 

    def _result_game_past(self, start_bank:int, end_bank:int)  -> str:
        return ['win' if end_bank > start_bank else 'lose'][0]

    def adding_user_data(self, username:str, password:int, start_bank:int,
                        color:int, end_bank:int) -> None:
        """Сохранения данных пользователя"""
        
        data = read_json_file(f'{USER_STATISTICS_GAME_PATH}')
        for user, data_us in data.items():
            if user == username and data_us["password"] == password:
                data_us["history start bank"].append(start_bank)
                data_us["bet"].append(self.bet)
                data_us["history end bank"].append(end_bank)
                data_us["result"].append(self._result_game_past(start_bank, end_bank))
                data_us["current bank"] = end_bank
                if self.user_number_bet == "":
                    data_us["color"].append(self._color_game(color))
                    break

                data_us["number"].append(color)
                break
        else:
            data.update({
                username:{
                    "password":password,
                    "history start bank":[start_bank],
                    "bet":[self.bet],
                    "color":[self._color_game(color)if self.user_number_bet == "" else None],
                    "number":[color if self.user_number_bet != "" else None],
                    "history end bank":[end_bank],
                    "result":[self._result_game_past(start_bank, end_bank)],
                    "current bank":end_bank
                    }
                })
            
        write_json_file(f'{USER_STATISTICS_GAME_PATH}', data)

    def adding_data_about_the_past_game(self, user_name:str, start_bank:int,
                                        color:int, end_bank:int) -> None:

        if os.stat(f'data/{GAME_STATISTICS_PATH}').st_size:
            data = read_json_file(f'{GAME_STATISTICS_PATH}')
        else:
            data = []

        if self.user_number_bet == '':
            data.append({
                        "name":user_name,
                        "initial bank":start_bank,
                        "bet":self.bet,
                        "color":self._color_game(color),
                        "end bank":end_bank,
                        "result": self._result_game_past(start_bank, end_bank)
                        })
        else:
            data.append({
                        "name":user_name,
                        "initial bank":start_bank,
                        "bet":self.bet,
                        "number":self._color_game(color),
                        "end bank":end_bank,
                        "result": self._result_game_past(start_bank, end_bank)
                        })  
                        
        write_json_file(f'{GAME_STATISTICS_PATH}', data)
