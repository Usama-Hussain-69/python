for var in range(0,23):
    if var==10 or var==14:
        continue # the continue keyword skip the things in the loop like in that example skip 10 and 14
    
    if var==20:
        break       # the braek keyword is uesd to break the exection of loop in that example breake on 20
    print(var) 

sum=0
i=1
while  i<=10:
    sum=sum+i
    i=i+1
print  (sum)    

for i in range(95,100):# start from 95
    print(f"this is line {i}")

print("hello friend if you want to add number than enter keyword add")
a=input("enter you want : ")
if a=="add":
    
    def ad(x,y,z):   # function define
        return x+y+z
    print(ad(1,2,3))   # function calling with values     
else:
    pass
# import random  # integer type number random generated 
# win=random.randint(1,100)   # random number limit and equal to win variable
# guss=1
# stop=0
# a=int(input("enter a value to find the number betwwen 1 to 100 :"))
# while not stop==1:
#     if a==win:
#         print(f"yes you win and in {guss} time sir ,")
#         stop=1
#     else:
#         if a<win:
#             print("too small value:") 
#         else:
#             print("to high value:")   
#         a=int(input("enter to find the number again:"))
#        guss+=1
