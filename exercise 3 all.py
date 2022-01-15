#a=int(input("enter a number to sum upto that :"))
#sum=0
#i=1
#while i<=a:
 #   sum=sum+i
  #  i=i+1

#print(sum)

#z=input("please enter number of 4 digits(0000) to sum every singal digit like (1+2+3+4)=10  : ")
#b=int(z[0])+ int(z[1])+int(z[2])+int(z[3])
#print(b)


#num=input("enter any number to sum of any lenght  :")
#total=0
#i=0
#while i<len(num):
  #  total=total+int(num[i])
 #   i=i+1
#print(total) 

name=input("please enter your name :")
temp=""
i=0
while i<len(name):
    if name[i] not in temp:# CHECKING THAT letter is present in temp variable or not
     temp+=name[i]
     print(f"{name[i]} : {name.count(name[i])}")
                                     # how many times that letter in coming in name string variable 
    i=i+1
 
