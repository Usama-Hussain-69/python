def se(l):
    num=[]
    for i in l:
        num.append(i**2)
    return num

number=list(range(1,21))
print(se(number))


# def a (p):
#     num=[]
#     for i in range (len(p)):
#         c=p.pop()
#         num.append(c)
#     return num
# p=list(range(1,9))
# print(a(p))
# c=['usama','hussain']
# a=c[0][-1:0:-1]
# print(a)
# print(len(c))


def re(li):
    num=[]
    for i in range(len(li)):
        num.append(li[i][::-1])
    return num
c=['usama','hussain','usa']
print(re(c))
 
def le(la):
    ax=[]
    bx=[]
    for i in range(len(la)):
        if la[i]%2==0:
            bx.append(la[i])
        else:
            ax.append(la[i])
    print(ax)
    print(bx)
la=list(range(1,100))
print(le(la))

def uni(ai,bi):
    c=[]
    for i in ai:
        if i in ai and i in bi:
            c.append(i)
        else:
            pass
    print(c)
ax=list(range(1,10))
bx=list(range(5,15))
uni(ax,bx)

def lin(lp):
    cx=0
    for i in lp:
        if type(i)==list:
            cx+=1
        else:
            pass
    print(cx)
lp=[1,2,3,[1,2,3],[],[]]
lin(lp)

