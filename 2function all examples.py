def name1(z):
    return z[-1]

print(name1("UsamaA"))


# function for checking odd and even
def check(a):
    if a%9==0:
        return " yes number is enen"
    else:
        return "yes odd number "

print(check(2))

def max(num1,num2):
    return num1>num2    # that only give answer in the form of ture(if condition ture) and false(if return condition is false)

ax=input("enter first number :")
bx=input("enter second second number :")

print(f"{max(ax,bx)} is ture mean greater first number either second number is greater")


def pelindrome(s):
    if s==s[-1::-1]:
        return "yes palindrome"
    else:
        return "no its no palindrome"
s=input("enter a string to check the palindrome :")
print(pelindrome(s))



