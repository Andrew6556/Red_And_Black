from red_black import *
from user import *
import inspect

#СДЕЛАТЬ РЕГИСТРАЦИЮ И АВТОРИЗАЦИЮ
while True:
    user_choice = int(input(inspect.cleandoc("""
    Что вы хотите сделать
    1.Зарегистрироваться
    2.Войти 
    """)))

    if user_choice == 1:
        user_name = input('Введите ваше имя\n')
        user_password = int(input('Введите пароль\n'))
        user_bank_game = int(input("Ваш банк: "))
        user = User({
        "username":user_name,
        "password":user_password,
        "bank":user_bank_game 
        })
        user.user_registration()
        
    elif user_choice == 2:
        user_name = input('Введите ваше имя\n')
        user_password = int(input('Введите пароль\n'))
        user_bank_game = int(input("Ваш банк: "))
        user = User({
        "username":user_name,
        "password":user_password,
        "bank":user_bank_game 
        })
        break


# print("Добро пожаловать в игру")

# username = input("Введите ваш ник: ")
# user_bank = int(input("Ваш банк: "))
# user = User({"username": username, "bank": user_bank, "password": 1233})
# user_inteface = UserInterface(user)

# while user.bank != 0:
#     user_bet = int(input("Введите вашу ставку(макс.стака 300р): "))
    
#     if user_bet > 300:
#         print('Это недопустимая ставка, введите число меньше 300')
#         continue

#     if user.bank - user_bet == -user_bank:
#         print('Эта ставка не допустима\nУ вас не достаточно средств для нее')
#         continue

#     print("0. Зелёное\n1. Красное\n2. Чёрное")

#     user_color_choice = int(input("Цвет (выберете цифрой): "))
    
#     # user.bank -= user_bet

#     game = RedBlack(user_color_choice, user_bet)
#     game.start_game()
#     prize = game.get_prize_color_bet()

#     console = GameInteface(game)
#     console.game_result_information()
#     console.checking_winning()

#     user.bank += prize
#     user_inteface.print_bank()

#     game.adding_data_about_the_past_game(username, user_bank, user_color_choice, user.bank)
#     user.adding_user_data(user_bank, user_color_choice, user_bet)
#     choice_end_programm = input('Для выхода из программы напишите "3"\n')

#     if choice_end_programm == 3:
#         print('Вы успешно вышли из программы')
#         break
#     else:
#         print('Хорошо\nУдачной игры')

    









