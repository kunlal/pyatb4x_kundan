# inner outer function claus

def outer():
    print("Outer Space...")

    def inner():
        print("i im in inner function")

    return inner


a = outer()
a()

# ==========================
# with variables

def calculator():
    def acceptnumber(*lst):
        num = 0
        for i in lst:
            num+=i
        return num
    return acceptnumber


getRes = calculator()
getSum = getRes(10,20,30)
print(getSum)