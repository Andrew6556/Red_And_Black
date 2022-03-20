from mimetypes import init


class NotCorrectColorIndex(Exception):
    """Обработка не существующего индекса """

    def __init__(self, text):
        self.text = text

class Incorrect_Password_Entry(Exception):
    pass
    # """Обработка неправильного ввода пароля"""

    # def __init__(self, password):
    #     self.password = password

class IncorrectLoginNumbers(Exception):
    pass