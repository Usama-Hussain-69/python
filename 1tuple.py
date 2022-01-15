########### Tuple #########
ap=(1,2,3,4,5,'usama',4.0)
print(ap[0::2])
bp=('x')  # here b is integer
cp=('x',) # here c is tuple
ax='usama','cs','ieff' # that is also a tuple 
print(ax[2])
ax=('usaama','cs','ieff')
bx,cx,dx=(ax)
print(bx)
print(cx)
print(dx)
# and we can also used list inside tuples than we can peform all action 
########### Dictionary #########
dic={
    'name':'what is your name ',
    'age' : 23,
    'etc' :'anything can be sense',

}
print(dic)
dic["usa"]=["one is american",'and second is usa',]
dic["us"]={"one is american",'and second is usa',}
print(dic)
dic.pop('etc')
print(dic)
################

def cub(n):
    dic={ }
    for i in range(1,n+1):
        dic[i]=i**3
    return dic
print(cub(4))
##############
def cou(s):
    coun={}
    for m in s:
        coun[m]=s.count(m)
    return coun
print(cou("usama hussain Usama Hussain"))
#####################
dic={}
fname,lname=input("enter your f name and commn than lname:").split(",")
dic['first name']=fname
dic['last name']=lname
for y,z in dic.items():
    print(f"{y}{z}")

