#list program
from collections import deque

lst = [10,20,20,30]
#append
for i in range(10):
    lst.append(i)
print(lst)

#extend
lstext = [20,50]

lst.extend(lstext)
print(lst)

#inser at pos
lst.insert(3,100)
print(lst)

#remove
lst.remove(20)
print(lst)

#pop
lst.pop()
print(lst)
lst.pop(1)
print(lst)

#geṭ element based on index, start and end limit
a = lst.index(20,1,100)
print(a)

a = lst.count(20)
print(a)

lst.sort(reverse=True)
print(lst)
a = lst[0:]
print(a)

lst.reverse()
print("rev",lst)

queue = deque(lst)
queue.popleft()
print(queue)

#clear
lst.clear()
print(lst)








