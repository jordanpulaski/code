#Jordan Pulaski
#jordan.pulaski001@albright.edu
#Lab 9-25-18

import time
#Chapter 2 Programming Exercise 10
#stablish varibles
cookies = 0
sugar = (1.5/48)
butter = (1/48)
flour = (2.75/48)

#input statement
cookies = int(input("How many cookies do you want to  make?: "))

#establish the totals and format the numbers
totalSugar = sugar*cookies
totalButter = butter*cookies
totalFlour = flour*cookies

totalSugar = format(totalSugar,".2f")
totalButter = format(totalButter,".2f")
totalFlour = format(totalFlour,".2f")

#output message
print("You need", totalSugar, "cups of sugar, ",totalButter, "cups of butter, \
and ", totalFlour, "cups of flour")

#Chapter 3 Programming Exercise 15
print("\n")
#establish Variables
time = 0
minute = 60
hour = 3600
day = 86400

#input
time = int(input("Enter a number of seconds: "))

#if statements covering all bases
if (time >= day):
    print("\nThere are" ,format(seconds / day '.2f'), "days in" ,"seconds")
elif (seconds >= hour):
    print("\nThere are" ,format(seconds / hour '.2f'), "days in" ,"seconds")
elif (seconds >= minute):
    print("\nThere are" ,format(seconds / minute '.2f'), "days in" ,"seconds")
#else statement
else:
    print("there is ",seconds, "seconds.")

#Chapter 4 exercise 12
print("\n")
#establish variables
total = 1

#input number
factoral = int(input("Enter a nonnegative integer: "))

#for statement to generate the factorial
for i in range(1,factoral+1):
    
    total *= i

#Outgoing message
print("The factorial of ", factoral, "is ",total)

#Chapter 5 algorithm workbench 1,2,3
#AW 1
print("\n")

#definition
def timesTen(number):
    ten = 10
    number = number*10
    print("Your new number is ",number)
    return number;
#asking user to enter number to apply the def
number = int(input("Enter a number: "))
#recalling the program
timesTen(number)

#AW 2
print("\n")
#establish variables
quantity = 0
#definition
def showValue (quantity):
    quantity = 12
    #printing the number
    print("the number is ",quantity)
    return quantity
#recalling your definition
showValue (quantity)

#AW 3
print("\n")
def myFunction(a,b,c):
    print(a)
    print(b)
    print(c)
    return(a,b,c)

myFunction(3,2,1)

time.sleep(3)
    













