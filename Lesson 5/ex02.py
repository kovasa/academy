""" Lesson 5 ex.2 """


class Student():
    """ Stores information about exam and labs marks of student. """

    def __init__(self, name, conf):
        self.name = name
        self.conf = conf
        self.list = [[None, 0] for i in range(self.conf["lab_num"])]
        self.max_attempt = 3
        self.max_exam = 0

    def make_lab(self, m, n=None):  # pylint: disable=invalid-name
        """ Saves lab mark.

        Args:
            m (float): lab mark.
            n (int): lab id.

        Returns:
            Student: Class instance.
        """
        if n is None:
            n = next(i for i, x in enumerate(self.list) if x[0] is None)
        if 0 <= n <= self.conf["lab_num"] and \
           self.list[n][1] < self.max_attempt and m <= self.conf["lab_max"]:
            self.list[n][0] = m
            self.list[n][1] += 1
        return self

    def make_exam(self, m):  # pylint: disable=invalid-name
        """ Saves exam mark.

        Args:
            m (float): exam mark.

        Returns:
            Student: Class instance.
        """
        if m <= self.conf["exam_max"]:
            self.max_exam = m
        return self

    def is_certified(self):
        """ Computes sum of all marks and compares with minimum.

        Returns:
            tuple(float, bool): Sum of all marks and True if it >= minimum.
        """
        count = sum([x[0] for x in self.list if x[0] is not None]) + \
            self.max_exam
        passed = (count / (self.conf["exam_max"] + self.conf["lab_max"] *
                           self.conf["lab_num"])) >= self.conf["k"]
        return (count, passed)


def _test():
    ivan = Student("Ivanov", {"exam_max": 30, "lab_max": 7,
                              "lab_num": 10, "k": 0.61})
    ivan.make_lab(6, 4)
    ivan.make_lab(5, 4)
    ivan.make_lab(4)
    ivan.make_lab(6, 2)
    ivan.make_lab(5, 2)
    ivan.make_lab(6, 2)
    ivan.make_lab(7, 2)
    ivan.make_lab(7, 2)
    ivan.make_lab(3)
    ivan.make_lab(5)
    ivan.make_lab(6)
    ivan.make_lab(1, 22)
    ivan.make_lab(4)
    ivan.make_lab(1)
    ivan.make_lab(6)
    ivan.make_lab(10, 9)
    ivan.make_exam(20)
    ivan.make_exam(40)

    print(ivan.is_certified())


_test()
