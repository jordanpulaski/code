#Jordan Pualski
#jordan.pulaski001@albright.edu
#Programming exercises 1,2

#Programming Exercise 1
import time

#main function
def main():
    miles = float(input("Enter a distance in kilometers: "))
    formula(miles)

#output
def formula(miles):
#kilometers to miles conversion, formatting it, and giving an output
    miles = (miles * .6214)
    miles = format(miles,".2f")
    print("Your distance in miles is", miles)
#dont need return because its only running through the program once
#calling the main function
main()

#Programming Exercise 2
print("\n")

#main function to call everything
def main():
    purchaseAmount = userInput()
    purchase(purchaseAmount)    

#gather user input    
def userInput():
    purchaseAmount = int(input("Enter the amount of a purchase: "))
    return purchaseAmount

#calculations and output
def purchase(purchaseAmount):
    stateTax = (purchaseAmount*.05)
    countryTax = (purchaseAmount*.025)
    totalSalesTax = (stateTax+countryTax)
    saleTotal = (purchaseAmount+totalSalesTax)
    print("The state tax is: ", stateTax)
    print("The country tax is ", countryTax)
    print("The sales tax is ", totalSalesTax)
    print("The total of the sale was ", saleTotal)
    
#call the main function
main()

time.sleep(3)



    
