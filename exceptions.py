class NotCorrectColorIndex(Exception):
    """Обработка ошибок """

    def __init__(self, text):
        self.text = text