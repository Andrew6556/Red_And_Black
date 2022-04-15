from red_black import RedBlack
from game_concol import GameInteface
from user import User
from user_concol import UserInterface
from exceptions import*

import inspect


print("Добро пожаловать в игру")
loop: bool = True
main: bool = True
while main:
    while loop:
        user_choice = int(input(inspect.cleandoc("""
                                Что вы хотите сделать
                                1.Зарегистрироваться
                                2.Войти 
                                """
                            ))
                        )
        
        if user_choice == 1:
            
            while True:
                user_name = input('Введите ваше имя\n')
                user_password = int(input('Введите пароль\n'))
                user_bank_game = int(input("Ваш банк: "))
                
                user = User(user_name, user_password, user_bank_game)
                console = UserInterface(user)
                try:
                    user.user_registration()
                except IncorrectLoginNumbers:
                    console.error_message_in_login()
                except LoginStartsWithNoCharacters:
                    console.error_message_in_login()
                except IncorrectPasswordEntry:
                    console.correct_password_processing()
                else:
                    break
                
            print('Регистрация прошла успешно')
            
        elif user_choice == 2:
            while loop:
                user_name = input('Введите ваше имя\n')
                user_password = int(input('Введите пароль\n'))

                try:
                    user = User.authenticate(user_name, user_password)
                    user_int = UserInterface(user)

                except UserNameDoesNotExist:
                    print('Такого имени не существует в базе')
                except PasswordError:
                    print('Неверный пароль!')

                if user.is_authenticate == True:
                    user_int.print_bank()
                    
                    print(inspect.cleandoc("""
                            Вы хотите добавить денег в банк?
                            1.Да
                            2.Нет
                            """))

                    choice_to_add_money_to_the_bank = int(input('Напишите цифрой, что вы выбрали: '))
    
                    if choice_to_add_money_to_the_bank == 1:
                        addition_amount = int(input('Введите сумму которую хотите добавить\n'))
                        user.update_bank(addition_amount)
                        user_int.print_bank()
                        print('Хорошей игры :)')
                        loop: bool = False

                    elif choice_to_add_money_to_the_bank == 2:
                        print('Хорошей игры :)')
                        loop: bool = False

    print(inspect.cleandoc("""
    Выбирете какой вариант игры вам подходит:
    1.C выбором цвета(их всего три: черный, красный и самый редкий зеленый) - не особо рисковая игра
    2.Наиболее рисковая игра. Выбераете число если оно выпадает, то вы выйграли - большой куш ,но и риск проиграть высок :)
    """))
    
    current_bank = user.bank
    
    choice_game = int(input('Введите вариант игры(цифрой): '))

    if choice_game == 1:
        while main:
            user_bet = int(input("Введите вашу ставку(макс.стака 300р): "))
            
            if user_bet > 300 and user_bet <= 0:
                print('Это недопустимая ставка, введите число меньше 300')
                continue

            if user.bank - user_bet < 0:
                print('Эта ставка не допустима\nУ вас не достаточно средств для нее')
                continue
            
            print("0. Зелёное\n1. Красное\n2. Чёрное")

            user_color_choice: int = int(input("Цвет (выберете цифрой): "))
            
            game = RedBlack(user_bet, user_color_choice)
            game.start_game()
            prize = game.get_prize_color_bet()
            
            console = GameInteface(game)
            console.game_result_information()
            console.checking_winning()

            user.bank += prize
            user_int.print_bank()

            game.adding_data_about_the_past_game(user_name, current_bank, user_color_choice, user.bank)
            game.adding_user_data(user.username, user.password , current_bank, user_color_choice, user.bank)
            game.update_current_bank_json(user.username ,user.password, user.bank)
            choice_end_programm = int(input('Для выхода из программы напишите "3"\n'))

            if user.bank == 0:
                print('Игра окончена!\nУ вас недастаточно средств для продолжения')
                main: bool = False

            if choice_end_programm == 3:
                print('Вы успешно вышли из программы')
                main: bool = False
            else:
                print('Хорошо\nУдачной игры')

    if choice_game == 2:
        while main:
            user_bet = int(input("Введите вашу ставку(макс.стака 300р): "))
            
            if user_bet > 300:
                print('Это недопустимая ставка, введите число меньше 300')
                continue

            if user.bank - user_bet < 0:
                print('Эта ставка не допустима\nУ вас не достаточно средств для нее')
                continue

            print("Выберете число от 0 до 100")

            while True:
                choice_num = int(input("введите число\n"))
                try:
                    if choice_num > 100:
                        raise NumberIsOutOfRange
                except NumberIsOutOfRange:
                    print('Вы ввели не допустимое число\nвведите число до 100!')
                else:
                    break

            game = RedBlack(user_bet, user_number_bet=choice_num)
            game.start_game() 
            prize = game.get_prize_number_bet()
            
            console = GameInteface(game)
            console.game_result_information()
            console.number_game_result()

            user.bank += prize
            user_int.print_bank()

            game.adding_data_about_the_past_game(user_name,  current_bank, choice_num, user.bank)
            game.adding_user_data(user.username, user.password , current_bank, choice_num, user.bank)
            game.update_current_bank_json(user.username ,user.password, user.bank)
            choice_end_programm = int(input('Для выхода из программы напишите "3"\n'))

            if user.bank == 0:
                print('Игра окончена!\nУ вас недастаточно средств для продолжения')
                main: bool = False

            if choice_end_programm == 3:
                print('Вы успешно вышли из программы')
                main: bool = False
            else:
                print('Хорошо\nУдачной игры')
