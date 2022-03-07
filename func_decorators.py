#модуль с декораторами 

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
    def wrapper(self, name, start_bank,
                color, end_bank, *args, **kwargs):
        if end_bank > start_bank:
            result='win'
        else:
            result='lose'

        func(self, name, start_bank, color, end_bank, result, *args, **kwargs)
    return wrapper