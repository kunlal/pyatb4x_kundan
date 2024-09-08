def decorator_sum(func):
    def inner(a, b):
        print("Addition")
        c = a + b
        func(c, a)
    return inner


def decorator_sub(func):
    def inner(a, b):
        print("Subtraction")
        c = b - a
        func(c,b)
        print("after ")
    return inner


# to be decorated
@decorator_sum
@decorator_sub
def decorate_me(x, y):
    print("Hello Thanks for your decoration service up and down")
    print(x+y)


decorate_me(10, 20)



