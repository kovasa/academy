""" Lesson 8 ex.3
    Напишите функцию, которая получает два аргумента
    1)путь к файлу изображения jpeg на компьютере (строка);
    2)имя целевого файла (строка)
    отправляет файл HTTP POST запросом на https://postman-echo.com/post .
    В ответе будет получен файл изображения jpeg, в виде octet-stream,
    который нужно раскодировать и сохранить на компьютере под целевым
    именем, переданным в аргументе.
    Функция должна вернуть размер сохраненного файла.
"""


import base64
import os
import requests


def save_jpeg(path_in: str, name_out: str):
    """Sends HTTP POST request to https://postman-echo.com/postfile,
       saves octet-stream response into JPEG file and
       returns its size.
    """
    url_post = 'https://postman-echo.com/post'
    files = {'photo': open(path_in, 'rb')}

    req = requests.post(url_post, files=files)
    dir_in, name_in = os.path.split(path_in)
    res = req.json()['files'][name_in].split(',')[-1]

    filename = os.path.join(dir_in, name_out)
    with open(filename, 'wb') as f_out:
        code = base64.decodebytes(res.encode('utf-8'))
        f_out.write(code)

    return code.__sizeof__()


def _test():
    print(save_jpeg('E:\\orig.jpeg', 'test.jpeg'))


_test()
