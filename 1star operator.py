# def allsum(*abc): # now due to star operator all input is become a tuple
#     total=0
#     for i in abc:
#         total+=i
#     return total
# print(allsum(1,2,3,4,5,6,7,89,)) # now i gives multiplies arugment to function

#####################
# def all(n,n1,*etc):  # first permater n= 1 second parmeter n1 =2 and reaming all on star operator name etc 
#     print(n)         # their is necerssary to give the value to function parmeter (untill error show ) 
#     print(n1)        # thier is not not necerssary to give the value to function parmeter of star operator that do not show any if not you gives the valeus
#     print(*etc)      # note def all(*etc,n1): that is wrong 
#     mil=1
#     for i in etc:
#         mil*=i
#     return mil
# print(all(1,2,3,4,5,5,6,7,8))

################################
# def sll(n,*args):
#     if args:
#         return [i**n for i in args]
#     else:
#         return "yes second arugment is empty "

# print(sll(3,2,3,4,5,6,7,89))

#########Double star operator (kwargs) ##############
# that taking all input as a dictionary (key and its values)
# def all(n,**abc):  # first as a norma parmeter and reaiming all as a dictionary  
#     for k,v in abc.items():
#         print(f"k for key {k} v for values {v}")
#all(2,usama="usama is name",hussain="hussain is a last name of name ") # you can give more keys and values due to double star operator (**)

###############################################
# def all(**abc):   
#     for k,v in abc.items():
#         print(f"k for key {k} v for values {v}")

# d={'usama':'usama is f name ','hussain':'hussain last name '}
# all(**d) # giving dictionary as a parmeter to the function 

###################################
def cap(l,**kwargs):
    if kwargs.get('reverse str')==True:
        return [name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]

names=['usama','hussain']
    
    