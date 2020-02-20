""" Lesson 8 ex.5
    Напишите шаблон регулярного выражения, который соответствовал бы паролю,
    состоящему из 8-12 символов, среди которых могут быть строчные и заглавные
    буквы латинского алфавита, цифры, нижнее подчеркивание, звездочка, процент
    и амперсанд. Пароль обязательно должен включать в себя одну строчную букву,
    одну заглавную букву и одну цифру."""


import re


def check_pas(password):
    """ Function  that checks for format compliance password"""

    pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[*_%&]*).{8,12}$"
    if re.fullmatch(pattern, password) is None:
        print("The password is not correct")
        return 0
    return 1


def _test():
    print('1:', check_pas('axa_1990P'))
    print('2:', check_pas('9dddOhh_12o'))
    print('3:', check_pas('S23rtuuuu'))
    print('4:', check_pas('23*rt%uuuu'))
    print('5:', check_pas('jfkj00954JJJjj******'))


_test()
