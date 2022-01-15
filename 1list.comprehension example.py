####################
# a=[]
# for i in range(1,11):
#     a.append(-i)
# print(a)
######## that is a list comprehension example##############
# a1=[-i for i in range(1,11)]
# print(a1)
#########################
# b=['usama','hussain','hahaha']
# b1=[i[-1::-1] for i in b]
# print(b1)
########################
# a1=[i for i in range(0,11,2)]
# print(a1)
########  or same code with if statement#########
# a=list(range(1,11))
# a1=[i for i in a if i%2==0]
# print(a1)
##################################
# a=[1,1.1,3.4,'usa','abc',2]
# a1=[str(i) for i in a if type(i)==int or type(i)==float]
# print(a1)
############# same code like above ##########
# a=[1,1.1,3.4,'usa','abc',2]
# a1=[str(i) for i in a if (type(i)==int or type(i)==float)]
# print(a1)
#######################
# nums=list(range(1,20))
# a1=[i*2 if(i%2==0) else (-i) for i in nums]
# print(a1)
#################### nested for loop in list ######## 
# a1=[[i for i in range(5)] for j in range(5)]
# print(a1)
#############same code #########
# b1=[[1,2,3] for i in range(5)]
# print(b1)
