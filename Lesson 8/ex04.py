""" Lesson 8 ex.4
    Напишите шаблон регулярного выражения, который соответствовал бы
    следующему формату времени: YYYY-MM-DDThh:mm:ss±hh:mm (ISO формат)."""


import re


def check(string):
    """ Function  that checks for format
        compliance YYYY-MM-DDThh:mm:ss±hh:mm"""

    pattern = r"^\d{4}-(0[1-9]|1[0-2])-([0-2]\d|3[01])"\
              r"T([01]\d|2[0-3]):([0-5]\d):([0-5]\d)"\
              r"[+-]([01]\d|2[0-3]):([0-5]\d)$"
    return re.fullmatch(pattern, string)

print(check('2013-12-02T18:25:10+03:00'))
print(check('2020-02-20T20:20:02-02:30'))
print(check('2013-20-31T18:25:10+03:00'))
