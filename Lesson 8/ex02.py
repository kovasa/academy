""" Lesson 8 ex.2
    Напишите функцию, которая принимает три аргумента
    1)число, количество денег в исходной валюте, float;
    2)исходная валюта, трехсимвольная строка, str;
    3)целевая валюта, трехсимвольная строка, str;
    и возвращает количество денег в целевой валюте (тип float).
    Для получения курса валют воспользуйтесь https://api.exchangerate-api.com ."""


import requests


def converter(count: float, original: str, target: str):
    """Function that converts and returns a quantity
       money from the source currency to the target currency. """

    resp = requests.get(f'https://api.exchangerate-api.com/v4/latest/{original}')
    info = resp.json()

    return count * info['rates'][target]


def _test():
    count = 100
    original = "USD"
    target = "EUR"
    print(f'{count} {original} = {converter(count, original, target)} {target}')


_test()
