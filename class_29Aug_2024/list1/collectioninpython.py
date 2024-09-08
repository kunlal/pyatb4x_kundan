# Table of Content:
#
# Counters
# OrderedDict
# DefaultDict
# ChainMap
# NamedTuple
# DeQue
# UserDict
# UserList
# # UserString

#counter is a sub class of dictionary
import collections
from collections import Counter,OrderedDict,defaultdict,ChainMap
#pass an iterable object to counter
#keep count of elements in an interable
lst = [10,'q',20,30,20,40,'b','c','d','e']

print(Counter(lst))

#with dictionary
print(Counter({'a':2,'b':3,'c':2,'d':1}))

#with key/word args
print(Counter(a=10,b=2))




#orderDcictinry remember the order of the keys inserted
dict_var = {'a':2,'b':3,'c':2,'d':1}
print(OrderedDict(dict_var))



#default dictionary form lsit


lst_dic = [1,2,3,4,5,6]

a = defaultdict(int)


for i in lst_dic:
    a[i] = a[i] + 13

print(a.keys())


#second example
b = defaultdict(list)

for i in range(5):
    b[i].append(i)
print(b)



#chain map    incapsulate many dict and return a single list of dictionaries
d1 = {"a":1,"b":2}
d2 = {"c":1,"d":2}
dic3 = { 'f' : 5 }
chainMap = ChainMap(d1,d2)
print(chainMap)
print(type(chainMap))
for i in chainMap.values():
    print(i)


#adding a new dictionary using new_child() meṭhod

a =chainMap.new_child(dic3)
print(a)


#named tuple
#instead of accessing ṭhe elemenṭs from with index , access it with give name
#tuple - student

student = ("kundan","chandena",30)
#cr eating named tuple
StudTuple = collections.namedtuple('Students',['name','address','age'])
#addimng values
a = StudTuple("kundan","chandena",30)
print(a[1])  #accessing with index
print(a.name)    #accessig with given name




#DEQUE #doue ended que from both side unlike simle list
#append pop

queue = collections.deque(["name",1,2,39])

queue.popleft()
queue.appendleft(20)
print(queue)

