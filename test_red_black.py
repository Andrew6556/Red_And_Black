import unittest

from red_black import RedBlack, GameInteface

class TestRedBlack(unittest.TestCase):
    """Тестируем функции класса RedBlack"""

    def setUp(self):
        self.game = RedBlack(100, 0)#создаем экземпляр класса
    
    