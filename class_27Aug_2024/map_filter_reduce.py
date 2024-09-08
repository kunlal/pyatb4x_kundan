


#map fuction


def addition(x,y):
    return x**y

getResult = map(addition,[1,2,3,5],[2,2,2,2])
print(list(getResult))



#how to know if an object is iterable

try:
    result = iter(34543)
except TypeError as e:
    print(e,"Not an interable")