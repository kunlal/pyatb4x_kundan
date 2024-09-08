
# decoratro function

def outside(func):
    def inside(a ,b):
        print("Inside")
        func(a ,b)
    return inside

@outside
def do_something(x ,y):
    print("I im learning programming! in pyATB")
    print( x +y)


# outside = outside(do_something)
do_something(10 ,20)


##decorator example