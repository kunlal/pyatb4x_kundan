# function without arguments

def no_args():
    var1 = 10 + 20
    print(var1)
    res = lambda num: num * 10
    a = res(10)
    print(a)


no_args()
print("===========================")

# function with args
print("===========================")


def with_args(num, num2):
    p = 1
    p = p + num + num2
    return p


print(with_args(10, 20))

# function with list arguments
print("===========================")


def lis_args(*var):
    for i in var:
        print("Hello: ", i)


lis_args(10, 20, 30)

print("===========================")


# function with keyword args

def keyword(**keyword):
    for i, j in keyword.items():
        print(i, "=", j)


keyword(name="sumit", age="20")

# keyword with values
print("===========================")


def keyvalues(*args, name="sumit", **keywords):
    print(args)
    print(name)
    print(keywords)


keyvalues(10, 20, "amit", name="amar", address="mumbai", city="delhi")

print("===========================")


# another exampe
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

######output of all#######
