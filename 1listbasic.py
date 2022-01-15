a=[0,1,2,'usama','hussain',3.59,]
b=["hello i am form b variable"]
c=[1,3,0,8,4,2]
d=['a','f','s','y','b','w','c']
# insert(),extend(),append() are adding method of data in the list
a.append('haha') # that add haha in the last of list a 
print(a)
a.append(12)     # that add 12 in the last of list a
print(a)
a.append(b)      # that add list b in the list a
print(a)
a.insert(1,125)  # that add at index 1 with values 125
print(a)
a.insert(1,"as") # that add at index 1 with value of string as
print(a)
a.extend(b)      # that merage element of b in element of a in a list 
print(a)
# del[],.remove(),.clear(),.pop() are delete method in the list
a.pop()   # that pop the data in the last of list
print(a)
a.pop(1)  # that pop the data at index 1 in the list
print(a)
del a[1] # that delete the data at index 1 in the list
print(a)
a.remove(0) # that remove 0(integer) in the list if 0 more than one than remove first coming 0 in the list
a.remove('usama') # that remove that data(string type) in the list if more than one than remove first coming 0 in the list
print(a)
print(c)
print(sorted(c))    # the c list is sorted only for output not for program
c.sort()  # that chnage the index values to sort the list
print(sorted(d))   # the d list is sorted only for output not for program
print(d)
d.sort()   # that chnage the index values to sort the list
ax=d.copy()  # that copy the data of d into ax variable/list
print(ax)
print(a)
a.clear()
print(a)




