v = lambda a, b, c : a * b / c

r = v(10, 2, 2)

print(r)


def func(number):
    return lambda x : x * number

y = func(2)

z = y(2)

print(z)
