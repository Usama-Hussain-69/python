char=input("enter some thing to check char: ")
temp=""
for i in range(0,len(char)):
    if char[i] not in temp:
        temp+=char[i]
        print(f"your char is {char[i]} and total time is {char.count(char[i])}")

####################
a=[]
for m in range(1,11):
    a.append(-m)
print(a)
######## that is a list comprehension example##############
a1=[-n for n in range(1,11)]
print(a1)
#########################
b=['usama','hussain','hahaha']
b1=[z[-1::-1] for z in b]
print(b1)
########################
a12=[d for d in range(0,11,2)]
print(a12)
########  or same code with if statement#########
q=list(range(1,11))
d1=[r for r in q if r%2==0]
print(d1)
##################################
ai=[1,1.1,3.4,'usa','abc',2]
z1=[str(w) for w in ai if type(w)==int or type(w)==float]
print(z1)
############# same code with above ##########
ab=[1,1.1,3.4,'usa','abc',2]
y1=[str(t) for t in ab if (type(t)==int or type(t)==float)]
print(y1)
#######################
nums=list(range(1,20))
h1=[k*2 if(k%2==0) else (-k) for k in nums]
print(h1)
#################### nested for loop in list ######## 
v1=[[g for g in range(5)] for j in range(5)]
print(v1)
#############same code #########
m1=[[1,2,3] for g in range(5)]
print(m1)
   



