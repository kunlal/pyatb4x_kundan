##############################################
# generator

def generator():
    print("===================")
    for i in range(3):
        yield i+ 10


for i in generator():
    print(i)

# secind meṭhod
a = generator()
print(a.__next__())
print(next(a))
print(a.__next__())


# generator without for loop


def generatir_withoutloop():
    print("++++++++++++")
    yield 10
    yield 10 + 20
    yield 30


a = generatir_withoutloop()
print(next(a))
print(next(a))


# iterator


def creating_interator():
    lst = [10, 20, 30, 40]

    obj = iter(lst)
    return obj


b = creating_interator()
print("-------------")
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))      #StopIteration




