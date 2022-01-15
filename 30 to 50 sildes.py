#only if statement
a=input("Are you Programmer yes\\not:")
if a=="yes":
  print("ok you are a programmer")
# for if else statement
b=int(input("enter a number to check is number greater than 20 or not :"))
if b<20:
    print("yes your enter number is less than 20 ")
else:
    print("your enter number is greater than 20 ")
# for if else if statement
c=int(input("please enter your marks to check your grade :"))
if c>90 and c<=100:
    print("your grade is A+")
elif c>85 and c<=89:
    print("your grade is A") 
elif c>80 and c<=84:
    print("your grade is B+")
elif c>50 and c<=79:
    print("your grade is C") 
else:
    print(f"sorry to say your are Fail (F) because {c} ")


name=input("please enter name :")
if 'A' in name: 
    print("yes your name has english letter A")
else:
    print("yes not present:")    

