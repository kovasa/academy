def get_max(max_g=None):
    def fun(a, b, c, d):
        mean = (a+b+c+d)/4
        max_l = max(a, b, c, d)
        nonlocal max_g
        if max_g is None or max_l > max_g:
            max_g = max_l
        return mean, max_g
    return fun


a = get_max()
print(a(1, 2, 3, 4))
print(a(-3, -2, 10, 1))
print(a(7, 8, 8, 1))
