from red_black import*
from user import*
import inspect


print("Добро пожаловать в игру")
loop = True
while True:
    while loop:
        user_choice = int(input(inspect.cleandoc("""
        Что вы хотите сделать
        1.Зарегистрироваться
        2.Войти 
        """)))
        
        if user_choice == 1:
            user_name = input('Введите ваше имя\n')
            user_password = int(input('Введите пароль\n'))
            user_bank_game = int(input("Ваш банк: "))
            user = User(
            user_name,
            user_password,
            user_bank_game 
            )
            user.user_registration()
            print('Регистрация прошла успешно')
            
        elif user_choice == 2:
            while loop:
                user_name = input('Введите ваше имя\n')
                user_password = int(input('Введите пароль\n'))

                user = User(user_name, user_password)
                user_int = UserInterface(user)

                if user_int.print_authorization(user_name, user_password) == True:
                    # loop = False
                    user_int.print_bank()
                    print(inspect.cleandoc("""
                            Вы хотите добавить денег в банк?
                            1.Да
                            2.Нет
                            """))

                    choice_to_add_money_to_the_bank = int(input('Напишите цифрой, что вы выбрали: '))
    
                    if choice_to_add_money_to_the_bank == 1:
                        addition_amount = int(input('Введите сумму которую хотите добавить\n'))
                        user_int.add_money_in_bank(addition_amount)
                        user_int.print_bank()
                        print('Хорошей игры :)')
                        loop = False

                    elif choice_to_add_money_to_the_bank == 2:
                        print('Хорошей игры :)')
                        loop = False

    user_bet = int(input("Введите вашу ставку(макс.стака 300р): "))
    
    if user_bet > 300:
        print('Это недопустимая ставка, введите число меньше 300')
        continue

    # if user.bank - user_bet == -user_bank:
    #     print('Эта ставка не допустима\nУ вас не достаточно средств для нее')
    #     continue

    print("0. Зелёное\n1. Красное\n2. Чёрное")

    user_color_choice = int(input("Цвет (выберете цифрой): "))
    
    game = RedBlack(user_color_choice, user_bet)
    game.start_game()
    prize = game.get_prize_color_bet()

    console = GameInteface(game)
    console.game_result_information()
    console.checking_winning()

    user.bank += prize
    user_int.print_bank()

    # game.adding_data_about_the_past_game(username, user_bank, user_color_choice, user.bank)
    # user.adding_user_data(user_bank, user_color_choice, user_bet)
    choice_end_programm = input('Для выхода из программы напишите "3"\n')

    if choice_end_programm == 3:
        print('Вы успешно вышли из программы')
        break
    else:
        print('Хорошо\nУдачной игры')



    









