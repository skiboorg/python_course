class Player:
    """
    Класс игрока
    """
    def __init__(self, name, is_ai, card=None):
        self.name = name
        self.is_ai = is_ai
        self.card = card

    def __make_choice_human(self, number: int):
        """
        Выбор хода игрока человека.
        Возвращает Тrue если выбор правильный
        Возвращает False если выбор не правильный
        """
        choice = ''
        while not choice == '1' and not choice == '2':
            choice = input(
                '''
                Ваш выбор:
                1 - зачеркнуть
                2 - пропустить
                ''')
            if not choice == '1' and not choice == '2':
                print('Ошибка в выборе! Допускается ввод 1 или 2')

        check_number_result = self.card.check_number(number)

        if choice == '1' and not check_number_result:
            return False
        if choice == '1' and check_number_result:
            self.card.mark_number(*check_number_result)
            return True
        if choice == '2' and not check_number_result:
            return True
        if choice == '2' and check_number_result:
            return False

    def __make_choice_ai(self, number: int):
        """
        Выбор хода игрока компа. Всегда делает правильный выбор хода
        """
        check_number_result = self.card.check_number(number)
        if check_number_result:
            self.card.mark_number(*check_number_result)
            print(f'Игрок {self.name} зачеркивает')
        else:
            print(f'Игрок {self.name} пропускает')
        return True

    def make_choice(self, number: int):
        if self.is_ai:
            result = self.__make_choice_ai(number=number)
        else:
            result = self.__make_choice_human(number=number)
        return result
