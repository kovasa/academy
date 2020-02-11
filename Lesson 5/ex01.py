""" Lesson 5 ex.1 """


class Complex():
    """ Provides operations for complex numbers. """

    def __init__(self, string):
        self.real = float(string.split()[0])
        self.imaginary = float(string.split()[1])

    def __add__(self, other):
        return Complex(f"{self.real + other.real} \
                         {self.imaginary + other.imaginary}")

    def __sub__(self, other):
        return Complex(f"{self.real - other.real} \
                       {self.imaginary - other.imaginary}")

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        image = self.real * other.imaginary - other.real * self.imaginary
        return Complex(f"{real} {image}")

    def __truediv__(self, other):
        real = (self.real * other.real + self.imaginary * other.imaginary) / \
               (other.real ** 2 + other.imaginary ** 2)
        image = (self.imaginary * other.real - self.real * other.imaginary) / \
                (other.real ** 2 + other.imaginary ** 2)
        return Complex(f"{real} {image}")

    def __abs__(self):
        return Complex(f"{(self.real ** 2 + self.imaginary ** 2) ** 0.5} 0")

    def __str__(self):
        sign = '+' if self.imaginary >= 0 else ''
        return \
            f"{format(self.real, '.2f')}{sign}{format(self.imaginary, '.2f')}i"


def _test():
    comp1 = Complex(input())
    comp2 = Complex(input())
    print(comp1 + comp2)
    print(comp1 - comp2)
    print(comp1 * comp2)
    print(comp1 / comp2)
    print(abs(comp1))
    print(abs(comp2))


_test()
