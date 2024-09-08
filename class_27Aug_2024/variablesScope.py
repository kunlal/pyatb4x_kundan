# Global and local variable

my_var = 10
print("outer: ",id(my_var))

def myFunc(a, b):
    print("My Function!")
    global my_var           #outer variable
    print(a + b + my_var)
    print(id(my_var))
    my_var = 20             #local variable
    print("myFunc:",my_var)
    print(id(my_var))


def myFunc2():
    print("myFunc2: ", my_var)      #outer

myFunc(30, 90)
myFunc2()
