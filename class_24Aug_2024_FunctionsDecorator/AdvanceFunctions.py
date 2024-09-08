# lambda function
# anonymous function
# decorator

# lambda


lmb = lambda x: x ** x
print((lmb(10)))

lmb2 = lambda a, b: a + b
print(lmb2(10, 20))

lmb3 = lambda x: x.upper()
print(lmb3("sumit"))

lmb4 = lambda x: 10 * x if x > 5 else 5 * 2
print(lmb4(2))

is_even_list = [lambda args=x: args * 10 for x in range(1, 5)]
for item in is_even_list:
    print(item())


def square(i):
    return lambda : i * 2


lmb6 = [square(i) for i in range(10)]
for i in lmb6:
    print(i())


import math


# def give_me_power(num):
#     return math.pow(num, 2)
#
# op=  give_me_power(10)
# print(op)

op2 = lambda x: math.pow(int(input("Enter the the number\n")),5) * x
print(op2(2))
