import unittest


from red_black import RedBlack
from user import User
from write_and_read import read_json_file
from path_file import*

class TestRedBlack(unittest.TestCase):
    """Тестируем методы класса RedBlack"""

    def setUp(self):
        self.game = RedBlack(100, 0)#создаем экземпляр класса
    
    def test_roulette_is_stirred(self):
        """Тестируем __shuffle_game_box сработала она как надо"""
        start_box = self.game.game_box
        self.game.start_game()
        self.assertNotEqual(start_box, self.game.start_game)

    def test_calculation_of_correct_winnings_on_green(self):
        """
            Тестируем на правильный подсчет выйгрыша
        """
        self.game = RedBlack(100, 0)
        self.game.start_game()
        result_bet_prize = self.game.get_prize_color_bet()
        if result_bet_prize == 1400:
            self.assertEqual(result_bet_prize, 1400)
        elif result_bet_prize == 1400:
            self.assertEqual(result_bet_prize, 200)
        else:
            self.assertEqual(result_bet_prize, -100)
    
    def test_adding_user_data(self):
        """Проверяем добавился наш пользователь в json"""

        self.game.adding_user_data("@a", 12345678, 1000, 1, 1200)
        for i , value in read_json_file(USER_STATISTICS_GAME_PATH).items():
            if i == "@a":
                self.assertEqual("@a", i)
        
    def test_check_on_adding_new_data(self):
        """Тестируем adding_user_data 
            на добавление навых данных к пользователю
        """
        for i , value in read_json_file(USER_STATISTICS_GAME_PATH).items():
            if i == '@Andrey':
                initial_data_user = value

        self.game.adding_user_data('@Andrey', 12345678, 1200, 1, 1200)
        for i , value in read_json_file(USER_STATISTICS_GAME_PATH).items():
            if i == '@Andrey':
                end_data_user = value
        
        self.assertNotEqual(initial_data_user, end_data_user)

    def test_preservation_of_the_last_game(self):
        """Проверка на добавление данных о прошедшей игре"""
        before_addinglen = (read_json_file(GAME_STATISTICS_PATH))
        self.game.adding_data_about_the_past_game('Святой Гриша', 123321456,
                                                    1500, 2, 1200)

        after_addinglen = (read_json_file(GAME_STATISTICS_PATH))
        self.assertLess(before_addinglen,  after_addinglen)

    class TestUser(unittest.TestCase):
        """Тестируем методы класса User"""

    def setUp(self):
        self.user = User('@Andrey', 12345678, 999)

    def test_registration(self):
        """Проверяем добавление пользователя в базу после регистрации"""
        self.user = User('@Сырник лучший', 12345678, 999)
        self.user.user_registration()

        users = []
        for names , value in read_json_file(USERS_PATH).items():
            users.append(names)

        self.assertIn('@Сырник лучший', users)

    def test_update_bank(self):
        """проверяем корректно отработал метод"""

        initial_bank = self.user.bank
        self.user.update_bank(100)
        self.assertGreater(self.user.bank, initial_bank)



unittest.main()