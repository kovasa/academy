""" Lesson 8 ex.6
    Напишите шаблон регулярного выражения, который соответствует вопросительным
    предложениям, в которых одно слово (более 2 символов) повторяется 4 или
    более раз."""


import re


def check_sentence(string):
    """ Function  that checks for format compliance sentence"""

    pattern = r".*(\b\w{2,})(?:.*\1){3,}.*\?"

    if re.fullmatch(pattern, string) is None:
        return 0
    return 1


def _test():
    print('1:', check_sentence('abc kfogd abc ldongke t abc orpfnjd abc ru?'))
    print('2:', check_sentence('tttabcttt t abc orpabcfnjd abc ru?'))
    print('3:', check_sentence('kfogd abc ldongke t abc orpfnjd abc ru abc?'))
    print('4:', check_sentence('abc r ldongke abc t orpfnjd abc ru dftyj abc ty ?'))



_test()
