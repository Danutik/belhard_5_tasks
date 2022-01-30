"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
пользователь вводит строку

вернуть True, если она является валидным идентификатором и не является
зарезервированным словом Python, в противном случае вернуть False

Для того, чтобы проверить, является ли строка зарезервированным словом -
нужно воспользоваться функцией iskeyword из пакета keyword. Если строка
является зарезервированным словом Python, то iskeyword возвращает True,
в противном случае она возвращает False:

if iskeyword('def'):
    print('Да')
else:
    print('Нет')


Для того, чтобы проверить, является ли слово валидным идентификатором, нужно
воспользоваться методом строки .isidentifier()

if 'some_identificator'.isidentifier():
    print('Да')
else:
    print('Нет')


ПРИМЕРЫ
--------------------------------------------------------------------------------
- 'hello' -> True
- '123_pr' -> False
- 'def' -> False
"""
from keyword import iskeyword


def is_valid(check_string: str) -> bool:
    """Проверяет является ли строка валидным идентификатором и одновременно
    не является зарезервированным словом Python

    :param check_string: строка для проверки
    :type check_string: str

    :return: True или False в зависимости от того, является ли валидными
        идентификатором и не ключевым словом или нет
    :rtype: bool
    """
    if check_string.isidentifier() and iskeyword(check_string) is not True:
        result = True
    else:
        result = False
    return result


if __name__ == '__main__':
    string = input('Введите строку для проверки: ')
    print(f'Результат: {is_valid(string)}')
