#Jordan Pulaski
#jordan.pulaski001@albright.edu
#Lab 10/18/18

import time

#Algorithem Workbench 1
#main
def main():
    myList = userInput()

#list input    
def userInput():
    myList = ["Einstein, Newton, Copernicus, Kepler"]

    print(myList)

main()

#Algorithem Workbench 2
#main
def main():
    myList = userInput()

    
def userInput():
    myList = ["Einstein, Newton, Copernicus, Kepler"]
#for loop to print list
    for x in myList:
        print(x)
        
main()

#Algorithem Workbench 3
#call main
def main():
    numbers1 = lists() 
#move list 1 to list 2 and print it
def lists():
    numbers1 = ['100, 200, 300, 400, 500']
    numbers2 = []

    numbers2 += numbers1

    print(numbers2)

    return numbers2

main()

#Programming Exercise 1
number = 0
total = 0

#main
def main():
    sales = getSales(number)
    output(sales)
    
#get input
def getSales(number):
    total = 0
    
    for x in range(1,8,1):
        number += 1
        sales = float(input("What are the sales for day " + str(number) + "?: "))
        total += sales

    return total
#print total
def output(total):
    print(total)


main()

#Programming Exercise 2
import random

newList = []
#main
def main():
    randomNumber = getRandom()
#get random numbers and put them in list    
def getRandom():
    for x in range(9):
        randomNumber = random.randint(0,9)
        print(randomNumber)

        newList.append(randomNumber)
    
    return randomNumber

main()

#Programming Exercise 4
newList = []
total = 0
highest = 0
lowest = 0
average = 0
#main
def main():
    number = getNumber()
    calculations(number)
    output(highest, lowest, average, total)
    
#get 20 numbers from user
def getNumber():
    newList = []
    
    for x in range(1,21,1):
        number = float(input("Please enter a number: "))

    newList.append(number)
    total += number

    return total
#calculate highest lowest and average
def calculations(number):
    highest = max(number)
    lowest = min(number)
    average = (total/20)

    return highest, lowest, average
#give user output
def output(highest, lowest, average, total):
    highest = 0
    lowest = 0
    average = 0
    print("The sum of your numbers is", total)
    print("The average is", average)
    print("The highest number is", highest)
    print("The lowest number is", lowest)

main()

#Programming Exercise 6
#main
def main():
    number = getNumber()
    calculate(newList, number)
    handlingMultipleErrors(fileName)
#get number and list from user    
def getNumber():
    newList = []
    number = int(input("Please enter a number: ")

    for oneNumber in range(10):
        newList.append(int(input("Choose a number to add to your list: "))
                           
    while newList !='q' or 'Q':
        newList.append(int(input("Enter a number or enter q to quit: "))

    return newList, number
        
def calculate(newList, number):
    secondList = []

    for value in newList:
        if value > number and value != secondList:
            secondList.append(value)
    secondList.sort()

    return secondList
#give output
def output(secondList):
    print("The values greater than your number in your list are", secondList)
    
main()


#Programming Exercise 7
newList = []
#main
def main():
    answerList = getFile()
    answers(answerList)
    handlingMultipleErrors(fileName)
#given info
def getFile():
    answerList = ["A", "C", "A", "A", "D", "B", "C", "A", "C", "B", "A",\
                  "D", "C", "A", "D", "C", "B", "B", "D", "A"]
                       
    return answerList
#get user answers from text file
def answers(answerlist):
    answers = open("jordanPulaski.txt", 'r')
    studentAnswers = []
    #for line in answers:
        #answers.append(line.rstrip("\n"))
    correctSolutions = 0
    
#determinind whether the answers are correct
    for score in range(len(studentAnswers)):
        if studentAnswers[score] == answerList[score]
            correctSolutions = correctSolutions + 1

    if correctSolutions >= 15:
        print("You passed with a score of: ", correctSolutions, "out of 20")

    else:
        print("You failed with a score of: ", correctSolutions, "out of 20")

    return correctSolutions

main()

#Programming Exercise 9
def main():
    file = readFile()
    maxPopulation = maxPopulation(populationList)
    minPopulation = minPopulation(populationList)
    average(populationList)
    output(average, minPopulation, maxPopulation)

#opening population text file
def readFile():
    yearOne = 1950
    file = open("USPopulation.txt", "r")

    populationList = file.read().splitlines()

    for number in range(len(populationList)):
        populationList[number] = int(populationList[number])

    file.close()
    return populationList, yearOne
                       
#getting max population
def maxPopulation(populationList):
    maxPopulation = max(populationList)

    yearsMax = []
    for i in range(len(populationList)):
        if populationList[i] == maxPopulation
            yearsMax.append(i + yearOne)

    return maxPopulation, yearsMax

#getting min population
def minPopulation(populationList):
    minPopulation = min(populationList)

    yearsMin = []
    for i in range(len(populationList)):
        if populationList[i] == minPopulation
            yearsMin.append(i + yearOne)

    return minPopulation, yearsMin

#finding average
def average(populationList):
    for number in populationList:
        numberTotal = populationList[number]
        total = total + numberTotal
    average = total / numberTotal

    return average
#giving user output
def output(average, minPopulation, maxPopulation):
    print("The average is ",average)
    print("The smallest populations size is ", minPopulation)
    print("The largest population size is ", maxPopulation)
                       
main()
time.sleep(3)


#Very confused about assignments 6,7 and 9, lynsie helped me best she could but
#none of my programs will run correctly                       

              


    

        

        
        
