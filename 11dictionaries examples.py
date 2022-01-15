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
    for i in s:
        coun[i]=s.count(i)
    return coun
print(cou("usama hussain Usama Hussain"))
######################33
dic={}
fname,lname=input("enter your f name and commn than lname:").split(",")
dic['first name']=fname
dic['last name']=lname
for i,j in dic.items():
    print(f"{i}{j}")


    

