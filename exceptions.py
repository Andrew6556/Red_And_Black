class NotCorrectColorIndex(Exception):
    """Обработка не существующего индекса """

    def __init__(self, text):
        self.text = text
class IncorrectPasswordEntry(Exception):
    pass
class IncorrectLoginNumbers(Exception):
    pass
class LoginStartsWithNoCharacters(Exception):
    pass