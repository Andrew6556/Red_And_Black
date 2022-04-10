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

class NumberIsOutOfRange(Exception):
    pass

class UserNameDoesNotExist(Exception):
    pass

class PasswordError(Exception):
    pass