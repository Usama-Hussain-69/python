# l1=[1,2,3,4,5]
# l2=[9,8,7,6,5]
# print(list(zip(l1,l2)))

#############
# l1=[1,2,3,4,5]
# l2=[9,8,7,6,5]
# l=[(1,9),(2,8),(3,7),(4,6),(5,5)]
# a,b=zip(*l)    # the star operator unpack the l than zip give two tuple that become a and b
# print(a)
# print(b)
##############################
num=[]
l1=[1,22,3,14,5]
l2=[9,8,7,6,5]
for i in zip(l1,l2):     # first zip function convert l1 and l2 in pair values that pair will go to in i of for loop
    num.append(max(i))
print(num)
