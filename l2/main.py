from classes.card import *
from classes.bag import *
from classes.player import *

game_type = None
bag = Bag()
players = []


def init():
    """
    Инициализация игры
    """
    global game_type

    player1 = None
    player2 = None

    right_answers = ['1', '2', '3', '4']

    while game_type not in right_answers:
        game_type = input(
            '''
            Тип игры:
             1 - человек против человека
             2 - человек против компа
             3 - комп против компа
             4 - любое кол-во игроков
            ''')
        if game_type not in right_answers:
            print('Ошибка в выборе! Допускается ввод 1,2,3 или 4')

    if game_type == '1':
        player1 = Player(name='Человек1', is_ai=False)
        player2 = Player(name='Человек2', is_ai=False)

    if game_type == '2':
        player1 = Player(name='Человек', is_ai=False)
        player2 = Player(name='Комп', is_ai=True)

    if game_type == '3':
        player1 = Player(name='Комп1', is_ai=True)
        player2 = Player(name='Комп2', is_ai=True)

    if game_type == '4':
        custom_players = input('Введите игроков в виде\n'
                               '"ИМЯ-H/C|ИМЯ-H/C (H-человек,C-комп),\n'
                               'например Ivan-H|Bob-C|Petr-H"\n')
        for player in custom_players.split('|'):
            splitted_player = player.split('-')
            players.append(Player(name=splitted_player[0], is_ai=True if splitted_player[1] == 'C' else False))
    else:
        players.append(player1)
        players.append(player2)

    for player in players:
        card = Card()
        player.card = card
        player.card.player_name = player.name


def main():
    is_game_over = False
    current_player_index = 0

    init()

    last_player_index = len(players)-1

    while not is_game_over:
        number = bag.get_number()
        player = players[current_player_index]

        print(f'Ход игрока {player.name}')
        player.card.show()
        print(f'Выпало число {number}')
        result = player.make_choice(number=number)

        if bag.numbers_left == 0:
            print(f'Игра завершена. Все боченки извлечены')
            break

        if player.card.is_done:
            print(f'Игра завершена. Игрок {player.name} победил')
            break

        if result:
            print('Игра продолжается')
            print(f'Выпавшие числа {bag.got_numbers}\nОсталось боченков {bag.numbers_left}')

            if not current_player_index == last_player_index:
                current_player_index += 1
            else:
                current_player_index = 0

        else:
            print(f'Игра завершена. Игрок {player.name} сделал не правильный выбор')
            is_game_over = True


if __name__ == '__main__':
    main()
