import random


class Bag:
    """
    Класс мешка с боченками
    """
    got_numbers = []
    numbers_left = 90

    def get_number(self) -> int:
        """
        Получаем случайное число,
        проверяем было ли такое число получено ранее,
        если нет то добавляем в массив
        """
        loop = True
        while loop:
            number = random.randint(1,91)
            if number not in self.got_numbers:
                self.got_numbers.append(number)
                self.numbers_left -= 1
                return number






