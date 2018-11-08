#Jordan Pulaski
#jordan.pulaski001@albright.edu

#Algorithm Workbench 5
#main
def main():
    statement = userInput()
    results = website(statement, ".com")
    output(results)

#basecase and input statement
def userInput():
    statement = ''
    if statement == '':
        try:
            statement = input("Enter a website: ")
        except ValueError:
            print("Your input is incorrect")
    

    return statement
#making sure the entered word ends with .com
def website(statement, message):
    results = statement.endswith(message)
    return results

#true or false
def output(results):
    print(results)

main()

#Algorithm Workbench 6
#main
def main():
    word = userInput()
    newWord = upper(word)
    output(newWord)

#basecase and user input
    
def userInput():
    word = ''
    if word == '':
        try:
            word = input("Enter a word: ")
        except ValueError:
            print("try again")

    return word

#making a new string that replaces all t with T
def upper(word):
    newWord = ''
    for x in range(0,len(word)):
        if word[x] == "t":
            newWord += "T"
        else:
            newWord += word[x]
            
    return newWord

#give user new string
def output(newWord):
    print(newWord)

main()

#Algorithm Workbench 7
#main
def main():
    backwardsString= reverse()
    output(backwardsString)

#make the string reverse
def reverse():
    string = input("Enter a word: ")

    backwardsString = ''.join(reversed(string))

    return backwardsString

#print output
def output(backwardsString):
    
    print(backwardsString)

    return


#Programming Exercise 1
#main
def main():
    name = userInput()
    letters = Letter(name)
    
#Get first middle and last name and do basecase
def userInput():
    name = ''
    if name == '':
        try:
            name = input("Enter your first, middle, and last name: ")
        except ValueError:
            print("Sorry try again")
            
    return name
#print only the first letter of each name by spliting the input
def Letter(name):
    names = name.split()
    letters = [word[0] for word in names]
    print(''.join(letters))

    return letters

main()

#Programming Exercise 5
#main
def main():
    phoneNumber = userInput()
    convert(phoneNumber)
#Get phone number from user
def userInput():
    phoneNumber = ''
    if phoneNumber == '':
        try:
            phoneNumber = input("Enter you phone number in the form of XXX-XXX-XXXX: ")
        except ValueError:
            print("Sorry try again!")
            
    return phoneNumber
#convert letters to numbers
def convert(phoneNumber):
    for r in (("A","2"),("B","2"),("C","2"),("D","3"),("E","3"),("F","3"),("H","4"),("I","4"),("G","4") +
              ("J","5"),("K","5"),("L","5"),("M","6"),("N","6"),("O","6"),("P","7"),("Q","7"),("R","7") +
              ("S","7"),("T","8"),("U","8"),("V","8"),("W","9"),("X","9"),("Y","9"),("Z","9")):
        numbers = phoneNumber.replace(*r)
    print(numbers)

    return numbers

main()

#Programming Exercise 6
def main():
    outfile = userInput()
    newList = readFile(outfile)
    average(newList)
    
#Input the name of the file you want read (text.txt)    
def userInput():
    outfile = input("Please input the name of your file: ")
    while len(outfile) <= 0:
        outfile = input("Please input the name of your file: ")

    return outfile

#prints whats in the file
def readFile(outfile):
    number = 0
    infile = open(outfile, 'r')
    lines = infile.read().splitlines()
    newList = []
    for line in lines:
        newList.append(len(line.split()))
                       
    infile.close()
    return newList
#find the average amount of words
def average(newList):
    averageFunction = sum(newList) / sum(newList)
    print("the average number of words is ",averageFunction)
    
    
    return averageFunction

#When i run my program i get the average as 1 not the actual answer?

main()
    

