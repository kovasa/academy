""" Lesson 8 ex.1
    Напишите функцию, которая возвращает размер HTML документа по адресу https://google.com.
    Т.е. нужно получить страницу и вернуть ее размер (количество символов)."""


import requests


def size(url):
    """Function that returns the size of an HTML document
       in characters"""
    resp = requests.get(url)
    if resp:
        return len(resp.text)
    return 0


print("number of characters:", size('https://google.com'))
