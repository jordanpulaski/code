#Jordan Pulaski
#jordan.pulaski001@albright.edu
#Programming Exercises 3,4,5

#Program Exercise 3
def main():
    outfile = userInput()
    readFile(outfile)
    handlingMultibleErrors(outfile)
    return

#get file name
def userInput():
    outfile = input("Please input the name of your file: ")
    while len(outfile) <= 0:
        outfile = input("Please input the name of your file: ")

    return outfile

#prints whats in the file
def readFile(outfile):
    number = 0
    infile = open(outfile, 'r')
    line = 0
    while line != '':
#prints whats in the file with numbers
        line = infile.readline()
        line = line.rstrip('\n')
        number = number + 1
        print(number ,":", line)
    infile.close()
    return

#handles errors
def handlingMultibleErrors(outfile):
    try:
        myFile = open(outfile)
        line = myFile.readline()
    except FileNotFoundError:
       print("File not found")
#call main
main()

#Program Exercise 4
def main():
    outfile = userInput()
    readFile(outfile)
    handlingMultibleErrors(outfile)
    return

#get file name
def userInput():
    outfile = input("Please input the name of your file: ")
    while len(outfile) <= 0:
        outfile = input("Please input the name of your file: ")

    return outfile

#prints whats in the file
def readFile(outfile):
    infile = open(outfile, 'r')
    line = 0
    count = 0
    while line != '':
        line = infile.readline()
        line = line.rstrip('\n')
        count += 1
        print(count)
    infile.close()
    return

def handlingMultibleErrors(outfile):
    try:
        myFile = open(outfile)
        line = myFile.readline()
    except FileNotFoundError:
       print("File not found")
    except ValueError:
        print("Wrong input try again")
    except:
        print("Error not found")
        

main()

#Programming Exercise 5
def main():
    outfile = userInput()
    readFile(outfile)
    handlingMultibleErrors(outfile)
    return

#get file name
def userInput():
    outfile = input("Please input the name of your file: ")
    while len(outfile) <= 0:
        outfile = input("Please input the name of your file: ")

    return outfile

#prints whats in the file
def readFile(outfile):
    infile = open(outfile, 'r')
    line = 0
    total = 0
    while line != '':
#summing the numbers in the file
        line = infile.readline()
        line = line.rstrip('\n')
        total += int(line)
        print(total)
    infile.close()

def handlingMultibleErrors(outfile):
    try:
        myFile = open(outfile)
        line = myFile.readline()
    except FileNotFoundError:
       print("File not found")
    except ValueError:
        print("Wrong input try again")
    except:
        print("Error not found")
#call main
main()


#Programming Exercise #7
def main():
    number = userInput()
    fileName = userInput ()
    getFile(number, fileName)
    handlingMultipleErrors(fileName)
    

def userInput():
    fileName = input("Please input the name of your file: ")
    while len(fileName) <= 0:
        fileName = input("Please input the name of your file: ")
    number = int(input("Enter the amount of random numbers you want in your file: "))
    while number < 0:
        number = int(input("Please try again: "))

    return fileName, number

def getFile(number, fileName):
    import random
    
    outfile = open(fileName, "w")
    for numbers in range(number):
        outfile.write(str(random.randint(0,500)+"\n"))
        
    outfile.close()
    print("Numbers have been put in file")
    return outfile
                      
def handlingMultipleErrors(fileName):
    try:
        myFile = open (filename)
        line = myFile.readline()

        comparison = ""
        while line != comparison:
            print(line)
        myFile.close()

    except FileNotFoundError:
        print("Cant find the file")
    except ValueError:
        print("No valid integer line")
                      

main()

#Programming Exercise 8
def main():
    outfile = userInput()
    readFile(outfile)
    return

#get file name
def userInput():
    outfile = input("Please input the name of your file: ")
    while len(outfile) <= 0:
        outfile = input("Please input the name of your file: ")

    return outfile


def readFile(outfile):
    infile = open(outfile, 'r')
    line = 0
    number = 0
    count = 0
    total = 0
    
    while line != '':
        print(line.rstrip("\n"))
        line = infile.readline()
        number = int(line)
        total += number
        count += 1

    print("Total of random number is: ")
    print("The number of random numbers is: ")
    
  
    infile.close()
    return

def handlingMultipleErrors(fileName):
    try:
        myFile = open (filename)
        line = myFile.readline()

        comparison = ""
        while line != comparison:
            print(line)
        myFile.close()

    except FileNotFoundError:
        print("Cant find the file")
    except ValueError:
        print("No valid integer line")

main()

#Programming Exercise 9
def main():
    outfile = userInput()
    readFile(outfile)
    handlingMultipleErrors(fileName)
    return

#get file name
def userInput():
    outfile = input("Please input the name of your file: ")
    while len(outfile) <= 0:
        outfile = input("Please input the name of your file: ")

    return outfile


def readFile(outfile):
    infile = open(outfile, 'r')
    line = 0
    number = 0
    total = 0
    
    while line != '':
        line = infile.readline()
        for line in infile:
            total += int(line)
            count += 1

    average = total / number

    print("Your average number is: ")
    
  
    infile.close()
    return

def handlingMultipleErrors(fileName):
    try:
        myFile = open (filename)
        line = myFile.readline()

        comparison = ""
        while line != comparison:
            print(line)
        myFile.close()

    except FileNotFoundError:
        print("Cant find the file")
    except ValueError:
        print("No valid integer line")
main()

#Programming Exercise 10
def main():
    fileName = userInput()
    getFile(fileName)
    handlingMultipleErrors(fileName)
    

def userInput():
    fileName = input("Please input the name of your file: ")
    while len(fileName) <= 0:
        fileName = input("Please input the name of your file: ")

    return fileName

def getFile(fileName):
    import random
    
    outfile = open(fileName, "w")
    
    while name != "q" and name != 'Q':
        score = float(input("Enter the score of the golf player" +name+": "))

        outfile.write(name + "\n")
        outfile.write(str(score) + "\n")

        name = input("Enter the name of the golfer or enter q if you're done: ")
    return outfile

def readFile(fileName):

    inFile = open(fileName, "r")

    line = 0

    while line != "":
        line = inFile.readline()
        line = line.rstrip('\n')
        print(line)

    inFile.close()
                           
                      
def handlingMultipleErrors(fileName):
    try:
        myFile = open (filename)
        line = myFile.readline()

        comparison = ""
        while line != comparison:
            print(line)
        myFile.close()

    except FileNotFoundError:
        print("Cant find the file")
    except ValueError:
        print("No valid integer line")
                      

main()

                     

    
