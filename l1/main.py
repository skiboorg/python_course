import requests
from bs4 import BeautifulSoup


def init():
    depth = ''
    url = input('Начальный URL:')
    show_in = ''
    filename = ''
    while not depth.isdigit():
        depth = input('Глубина парсинга с начального URL:')
        if not depth.isdigit():
            print('Ошибка! Значение глубина парсинга должно быть числом')
    while not show_in == '1' and not show_in == '2' :
        show_in = input('''Вывод результата в
         1 - терминале
         2 - файле
         ''')
        if not show_in == '1' and not show_in == '2':
            print('Ошибка в выборе! Допускается ввод 1 (терминал) или 2 (файл)')
    if show_in == '2':
        filename = input('Введите имя файла:')
    return url, int(depth), show_in, filename


def get_urls_from_target_url(target_url: str, show_in_terminal: bool, filename: str):
    response = requests.get(target_url)
    parsed_urls=[]

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a')
        for link in links:
            href = link.get('href')
            if href and len(href) > 5 and href[:4] == 'http':
                if href not in parsed_urls:
                    parsed_urls.append(href)

        if show_in_terminal:
            print('Целевой URL: ', target_url)
            print('Список полученный URL с целевой страницы',parsed_urls)
        else:
            with open(f'{filename}.txt', 'a') as f:
                f.write(f'Целевой URL: {target_url}\n')
                f.write('Полученные ссылки:\n')
                for url in parsed_urls:
                    f.write(f'{url}\n')
                f.write('-------------------------------------------\n')

        return parsed_urls


def main():
    start_url, max_depth, show_result_in, filename = init()
    show_in_terminal = True if show_result_in == '1' else False

    start_url_parsed_urls = get_urls_from_target_url(target_url=start_url,
                                                     show_in_terminal=show_in_terminal,
                                                     filename=filename)

    for url in start_url_parsed_urls[:max_depth]:
        get_urls_from_target_url(target_url=url,
                                 show_in_terminal=show_in_terminal,
                                 filename=filename)


if __name__ == '__main__':
    main()