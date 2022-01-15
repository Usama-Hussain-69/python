s1={1,2,3,4,5,6,7,1,2,3,4,'a','b'}  # set do not show the duplicte values
s2={9,8,7,6,5,9,8,7,6,'a'}  # we can store in set is integer string float and not list and dictionaries
print(s1)
l=set(s1)
print(l)

#### unoin of sets ###
union=s1|s2   # we used | that symbol to union of sets
print(union)
####### intersection of sets ############
intersection=s1&s2   # we uesd & that symbol to intersection of sets
print(intersection)