#Jordan Pulaski
#jordan.pulaski001@albright.edu
#test prep questions

#Chapter 5 PE 12
def main():
    number1, number2 = userInput()
    Max(number1, number2)

def userInput():
    number1 = ''
    while number1 == '':
        try:
            number1 = int(input("Enter an integer "))
        except ValueError:
            print("wrong input try again")
            
    number2 = ''
    while number2 == '':
        try:
            number2 = int(input("Enter an integer "))
        except ValueError:
            print("wrong input try again")
    return number1, number2

def Max(number1, number2):
    if number1 > number2:
        print("The bigger number is ",number1)
    elif number1 < number2:
        print("The bigger number is ",number2)
    else:
        print("Please enter two numbers that arent equal")

main()

#Chapter 6 PE 4
def main():
    file = userInput()
    name = readFile(file)
    output(name)

def userInput():
    file = input("Enter the name of your file: ")

    while len(file) <= 0:
        file = input("Enter the name of your file: ")

    return file

def readFile(file):
    outfile = open(file, 'r')
    count = 0
    for line in outfile:
        count += 1
    return count

def output(count):
    print("there are", count, "names in this file")

main()
    
#Chapter 7 PE 5
def main():
    file = userInput()
    list1 = readFile(file)
    checkUser(list1)

def userInput():
    file = input("Enter the name of your file: ")

    while len(file) <= 0:
        file = input("Enter the name of your file: ")

    return file

def readFile(file):
    outfile = open(file, 'r')
    list1 = []
    line = outfile.readline()
    while line != '':
        line = line.rstrip('\n')
        list1.append(line)
        line = outfile.readline()
    print(list1)
    return list1

def checkUser(list1):
    checkNumber = input("Enter a number in the list: ")
    if checkNumber in list1:
        print("That is an account")
    else:
        print("Not an account")
main()
        
        
#Chapter 8 PE 2
def main():
    numbers = userInput()
    total = addNumbers(numbers)
    output(total)

def userInput():
    numbers = -1
    while numbers < 0:
        try:
            numbers = int(input("Enter a series of numbers without spaces: "))
        except ValueError:
            print("try again")
    return str(numbers)

def addNumbers(numbers):
    total = 0
    for num in numbers:
        total += int(num)
    return total

def output(total):
    print("The sum of your digits are", total)

main()

#Chapter 9 PE 1

def main():
    roomNumber, instructor, meetingTime = dictionary()
    courseNumber = userInput()
    match(roomNumber, instructor, meetingTime, courseNumber)

def dictionary():
    roomNumber = {"CS101":"3004", "CS102":"4501", "CS103":"6755", "NT110":"1244", "CM241":"1411"}

    instructor = {"CS101":"Haynes", "CS102":"Alvarado", "CS103":"Rich", "NT110":"Burke", "CM241":"Lee"}

    meetingTime = {"CS101":"8am", "CS102":"9am", "CS103":"10am", "NT110":"11am", "CM241":"1pm"}

    return roomNumber, instructor, meetingTime
def userInput():
    courseNumber = ''
    while courseNumber == '':
        courseNumber = input("Enter the name of your Course Number: ")
    courseNumber = courseNumber.upper()
    return courseNumber

def match(roomNumber, instructor, meetingTime, courseNumber):
    print("the room number is", roomNumber[courseNumber])
    print("the instructure is", instructor[courseNumber])
    print("the meetingTime is", meetingTime[courseNumber])

main()
            
    
    
    
            
        
