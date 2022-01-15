import random  # integer type number random generated 
win=random.randint(1,100)   # random number limit and equal to win variable
guss=1
stop=0
a=int(input("enter a value to find the number betwwen 1 to 100 :"))

while not stop==1:
    if a==win:
        print(f"yes you win and in {guss} time sir ,")
        stop=1
    else:
        if a<win:
            print("too small value:")
            
        else:
            print("to high value:")   
        a=int(input("enter to find the number again:"))
        guss+=1


                     
            