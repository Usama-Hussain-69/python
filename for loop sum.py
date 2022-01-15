# sum every single digits in the string of num
num=input("please enter a number :")
b=len(num) # find the lenght
c=0

for i in range (0,b):
     c+=int(num[i])
     i+=1

print(c)


