import json


def read_json_file(file):
    with open(f'data/{file}', "r", encoding="utf-8") as read_file:
        data = json.load(read_file)
    return data

def write_json_file(file, data):
    with open(f'data/{file}', "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

# user_bet = int(input("Введите вашу ставку: "))
# print("0. Зелёное\n1. Красное\n2. Чёрное")
# user_color_choice = int(input("Цвет (выберете цифрой): "))

# user.bank -= user_bet

# game = RedBlack(user_color_choice, user_bet)
# game.start_game()
# prize = game.get_prize_color_bet()

# console = GameInteface(game)

# console.game_result_information()
# console.checking_winning()

# user.bank += prize
# print(f"Ваш банк -- {user.bank}")