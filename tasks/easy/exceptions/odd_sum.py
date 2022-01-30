"""
Написать функцию odd_sum, которая принимает список, который может состоять
из различных элементов.
Если все элементы списка целые числа, то функция должна посчитать сумму
нечетных чисел.
Если хотя бы один элемент не является целым числом, то выкинуть ошибку
TypeError с сообщением "Все элементы списка должны быть целыми числами"
Задачу стоит выполнить с помощью одного цикла

Написать блок if __name__ == '__main__', в котором
нужно описать обработку исключения try-except-else-finally
"""


def odd_sum(int_list: list) -> int:
    summa = 0
    try:
        for i in int_list:
            if not isinstance(i, int):
                raise TypeError("Все элементы списка должны быть целыми числами")
            if i % 2 == 1:
                summa += i
    except TypeError as exc:
        print(exc)
        raise
    return summa


if __name__ == '__main__':
    some_list = [1, 2, 3, '123']
    try:
        odd_sum(some_list)
    except TypeError as exc:
        print(exc)
        print("Все элементы списка должны быть целыми числами")
    except ValueError as exc:
        print(exc)
        print("Все элементы списка должны быть целыми числами")
    else:
        print("Сумма нечетных чисел: ", odd_sum(some_list))
    finally:
        print("Готово")
