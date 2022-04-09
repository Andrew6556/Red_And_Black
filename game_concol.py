import time
import random

class GameInteface:
    
    def __init__(self, game:object):
        self.game = game
    
    def drop_effect(function):
        def wrapper(self, *args, **kwargs):
            game_number_index = self.game.game_box.index(self.game.game_number)
            print_time = 20 + random.randint(0, 20)
            if game_number_index >= print_time:
                numbers = self.game.game_box[game_number_index - 20:game_number_index]
            else:
                numbers = self.game.game_box[game_number_index: game_number_index + 20]

            [(print(f"{number}\n", end='') ,time.sleep(.1 + index/25))
                for index, number in enumerate(numbers, 1)]
            
            return function(self, *args, **kwargs)

        return wrapper

    # @drop_effect
    def game_result_information(self) -> None:
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

    def number_game_result(self):
        "результат игры с выбором числа"
        game_result = self.game.get_prize_number_bet()
        if game_result < 0:
            print("К сожанию, вы проиграли")
        else:
            print("Поздравялем с победой!")
