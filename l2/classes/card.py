import random


class Card:
    """
    Класс игровой карточки
    """
    def __init__(self, player_name=None):
        self.player_name = player_name
        self.rows = []
        self.is_done = False
        self.left_numbers = 15

        digits = random.sample(range(1, 91), 15)

        for index, i in enumerate(range(0, 3)):
            row = ['', '', '', '', '', '', '', '', '']
            row_places = random.sample(range(0, 9), 5)
            row_digits = digits[index * 5:index * 5 + 5]

            for index_j, j in enumerate(row_places):
                row[j] = row_digits[index_j]

            self.rows.append(row)

    def show(self):
        """
        Отображение карточки игрока
        """
        print(f'---Карточка игрока {self.player_name}---')
        for row in self.rows:
            row_string = '  '.join([str(item) for item in row])
            print(row_string)
        print('--------------------------------')

    def check_number(self, number: int):
        """
        Проверяем есть ли number в карточке, если есть возвращаем индекс number в ряду и колонке
        Если number нет, возвращяем False
        """
        for row_index, row in enumerate(self.rows):

            if number in row:
                col_index = row.index(number)
                return [row_index, col_index]

        return False

    def mark_number(self, row: int, col: int):
        """
        По индексам row и col заменяем содержимое на -
        """
        self.rows[row][col] = '-'
        self.left_numbers -= 1

        if self.left_numbers == 0:
            self.is_done = True



