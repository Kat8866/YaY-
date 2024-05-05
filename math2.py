import math
from random import *

count=0
i=0
m=0
t=0

print("For every addition question you will gain 1 point")
while i<5:
    x=randint(1, 10)
    y=randint(1, 10)
    print (x,"+",y)
    answer= x + y       
    your=int(input("="))
    if your==answer:
        print("Correct!")
        count+=1
        i+=1
    else:
        print("Incorrect")
print("You have ",count," points")


NY=str(input("Would you like to continue to Level 2:"))
if NY=="Yes":
    print("For every multiplication question you will gain 5 point")
    while m<5:
        x=randint(1, 10)
        y=randint(1, 10)
        print (x,"x",y)
        manswer=x*y
        myour=int(input("="))
        if myour==manswer:
            print("Correct!")
            count+=5
            m+=1
        else:
            print("Incorrect")
elif NY=="yes":
    print("For every multiplication question you will gain 5 point")
    while m<5:
        x=randint(1, 10)
        y=randint(1, 10)
        print (x,"x",y)
        manswer=x*y
        myour=int(input("="))
        if myour==manswer:
            print("Correct!")
            count+=5
            m+=1
        else:
            print("Incorrect")
elif NY=="No":
    print("Thank you for playing")
elif NY=="no":
    print("Thank you for playing")
print("You have ",count," points")

FY=str(input("Would you like to continue to Level 3:"))
if FY=="Yes":
    print("For every power question you will gain 15 point")
    while t<5:
        x=randint(1, 10)
        y=randint(2,3)
        power=""
        if y==2:
            power="squared"
        elif y==3:
            power="cubed"
            
        print ("What is",x,power)
        tanswer=x**y
        tyour=int(input("="))
        if tyour==tanswer:
            print("Correct!")
            count+=15
            t+=1
        else:
            print("Incorrect")
if FY=="yes":
    print("For every power question you will gain 15 point")
    while t<5:
        x=randint(1, 10)
        y=randint(2,3)
        power=""
        if y==2:
            power="squared"
        elif y==3:
            power="cubed"
            
        print ("What is",x,power)
        tanswer=x**y
        tyour=int(input("="))
        if tyour==tanswer:
            print("Correct!")
            count+=15
            t+=1
        else:
            print("Incorrect")
elif FY=="No":
    print("Thank you for playing")
elif FY=="no":
    print("Thank you for playing")
print("You have ",count," points")
