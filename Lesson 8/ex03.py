""" Lesson 8 ex.3
    Напишите функцию, которая получает два аргумента
    1)путь к файлу изображения jpeg на компьютере (строка);
    2)имя целевого файла (строка)
    отправляет файл HTTP POST запросом на https://postman-echo.com/post .
    В ответе будет получен файл изображения jpeg, в виде octet-stream,
    который нужно раскодировать и сохранить на компьютере под целевым
    именем, переданным в аргументе.
    Функция должна вернуть размер сохраненного файла."""


import requests


def save_jpeg(url: str, name: str):
    """Function  that sends an HTTP file and the response
       file saves and returns its size. """

    url_post = 'https://postman-echo.com/post'
    files = {'photo': open(url, 'rb')}
    req = requests.post(url_post, files=files)
    res = req.content

    filename = f'E:\{name}'
    with open(filename, 'wb') as f:
        f.write(res)


def _test():
    save_jpeg('E:\orig.jpeg', 'test.jpeg')


_test()
