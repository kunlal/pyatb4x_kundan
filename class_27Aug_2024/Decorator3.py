import time

def time1(func):
    def inner(a,b):

        t1 = time.time()
        func(a,b)
        t2 = time.time()
        print(f"Time Taken by time1 function: {t2-t1}")
    return inner

@time1
def fun1(a,b):
    print("Fun1")
    print(a+b)
    time.sleep(1.5)

@time1
def fun2(a,b):
    print("Fun2")
    time.sleep(1)

fun1(10,20)
fun2(20,30)
