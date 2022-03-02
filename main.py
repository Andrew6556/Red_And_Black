from red_black import *


#проблема с расчетом цены - если в банке 300 и делаем ставку 300 то получаем -300

print("Добро пожаловать в игру")

username = input("Введите ваш ник: ")
user_bank = int(input("Ваш банк: "))
user = User({"username": username, "bank": user_bank})

user_bet = int(input("Введите вашу ставку: "))
print("0. Зелёное\n1. Красное\n2. Чёрное")
user_color_choice = int(input("Цвет (выберете цифрой): "))

user.bank -= user_bet

game = RedBlack(user_color_choice, user_bet)
game.start_game()
prize = game.get_prize_color_bet()

console = GameInteface(game)

console.game_result_information()
console.checking_winning()

user.bank += prize
print(f"Ваш банк -- {user.bank}")

# while user.bank > 0:
#     user_bet = int(input("Введите вашу ставку(макс.стака 300р): "))
#     if user_bet > 300:
#         print('Это недопустимая ставка, введите число меньше 300')
#         continue

#     print("0. Зелёное\n1. Красное\n2. Чёрное")
#     user_color_choice = int(input("Цвет (выберете цифрой): "))
#     user.bank -= user_bet
#     game = RedBlack(user_color_choice, user_bet)
#     game.start_game()
#     prize = game.get_prize_color_bet()
#     console = GameInteface(game)
#     console.game_result_information()
#     console.checking_winning()
#     user.bank += prize
#     print(f"Ваш банк -- {user.bank}")