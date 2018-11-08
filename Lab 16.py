#Jordan Pulaski
#jordan.pulaski001@albright.edu

#Algorithm Workbench 5
#main function
def main():
    userSet = defineSet()
    output(userSet)

#add numbers to the set
def defineSet():
    userSet = set([10,20,30,40])
    return userSet

#print the set with the numbers
def output(userSet):
    print(userSet)
    
    return

main()

#Algorithm Workbench 6
#main
def main():
    set1, set2 = userInput()
    addSets(set1, set2)

#define set 1 and set 2
def userInput():
    set1 = set()
    for number in range (4):
        userInput = -1
        while userInput < 0:
            try:
                userInput = int(input("Enter a positive integer for set 1: "))
            except ValueError:
                print("Invalid Input")
        set1.add(userInput)
        
    set2 = set()
    for number2 in range (4):
        userInput = -1
        while userInput < 0:
            try:
                userInput = int(input("Enter a positive integer for set 2: "))
            except ValueError:
                print("Invalid Input")
        set2.add(userInput)
    return set1, set2

#union them together and print it
def addSets(set1, set2):
    set3 = set1.union(set2)
    print(set3)
    
    return set3

main()

#Algorithm Workbench 7
#main
def main():
    set1, set2 = userInput()
    addSets(set1, set2)

#define set 1 and set 2
def userInput():
    set1 = set()
    for number in range (4):
        userInput = -1
        while userInput < 0:
            try:
                userInput = int(input("Enter a positive integer for set 1: "))
            except ValueError:
                print("Invalid Input")
        set1.add(userInput)
        
    set2 = set()
    for number2 in range (4):
        userInput = -1
        while userInput < 0:
            try:
                userInput = int(input("Enter a positive integer for set 2: "))
            except ValueError:
                print("Invalid Input")
        set2.add(userInput)
    return set1, set2

#union them together and print it
def addSets(set1, set2):
    set3 = set1.intersection(set2)
    print(set3)
    
    return set3

main()

#Programming Exercise 2

def main():
    capitalOne = states()
    userInput(capitalOne)
    

def states():
    capitalOne = {  "montgomery": "alabama",
            "juneau": "alaska",
            "phoenix": "arizona", 
            "little rock": "arkansas",
            "sacramento" : "california",
            "denver": "colorado", 
            "hartford" : "connecticut", 
            "dover": "delaware",
            "tallahassee" : "florida",
            "atlanta" : "georgia",
            "honolulu" : "hawaii",
            "boise" : "idaho",
            "springfield" : "illinois",
            "indianapolis" : "indiana",
            "des moines" : "iowa",
            "topeka" : "kansas",
            "frankfort" : "kentucky",
            "baton rouge" : "louisiana",
            "augusta" : "maine",
            "annapolis" : "maryland",
            "boston" : "massachusetts",
            "lansing" : "michigan",
            "st. paul" : "minnesota",
            "jackson" : "mississippi",
            "jefferson city" : "missouri",
            "helena" : "montana",
            "lincoln" : "nebraska",
            "carson city" : "nevada",
            "concord" : "new hampshire",
            "trenton" : "new jersey",
            "santa fe" : "new mexico",
            "albany" : "new york",
            "raleigh" : "north carolina",
            "bismarck" : "north dakota",
            "columbus" : "ohio",
            "oklahoma city" : "oklahoma",
            "salem" : "oregon",
            "harrisburg" : "pennsylvania",
            "providence" : "rhode island",
            "columbia" : "south carolina",
            "pierre" : "south dakota",
            "nashville" : "tennessee",
            "austin" : "texas",
            "salt lake city" : "utah",
            "montpelier" : "vermont",
            "richmond" : "virginia",
            "olympia" : "washington",
            "charleston" : "west virginia",
            "madison" : "wisconsin",
            "cheyenne" : "wyoming"}
           

def userInput(capitalOne):

    done = True
    
    while done and len(capitalOne) > 0:
        capital, state = capitalOne.popitem()
        print("What is the capital of", state, " or press q to quit")
        guess = input("What is your guess?: ")
        while guess == '':
            try:
                guess = input("What is your guess?")
            except ValueError:
                print("Invalid Input")

        guess = guess.lower()

        if guess == "q"
            finish = True
        elif guess == capital:
            print("correct!")
        else:
            print("Sorry you're incorrect, the correct answer is ", capital)
    
main()           
        
    
#Programming Exercise 3
def main():
    fileName = userInput

def userInput():
        fileName = input("What file do you want to call? ") 

    while len(fileName) <= 0:
         fileName = input("What file do you want to call? ")

    while fileName == '':
        try:
           fileName = input("What file do you want to call? ")
        except ValueError:
            print("Your input does not work.")
    return fileName

def readFile():
    infile =

#Really didnt understand what was going on need help
    
#Programming Exercise 6

def main():
    fileName, fileName2 = userInput()
    wordSet = unique1(fileName)
    wordSet2 = unique2(fileName2)
    union, intersection, in1, in2, difference = getWords(wordSet, wordSet2)
    output(union, intersection, in1, in2, difference)
    return;     

# get input 

def userInput():

    fileName = input("Whats the name of the file you want? ") 

    while len(fileName) <= 0:
         fileName = input("Whats the name of the file you want? ")


    while fileName == '':
        try:
           fileName = input("Whats the name of the file you want? ")
        except ValueError:
            print("Invlalid Input")

    fileName2 = input("Whats the name of the file you want? ") 

    while len(fileName2) <= 0:
         fileName2 = input("Whats the name of the file you want? ")

  
    while fileName2 == '':
        try:
           fileName2 = input("Whats the name of the file you want? ")
        except ValueError:
            print("Invalid Input")
            
    return fileName, fileName2;

# return first file 
def unique1(fileName):
    file = open(fileName, 'r')

    text = file.read()
    text = text.replace('\n', ' ')
    
    wordList = text.split(' ')

    for word in wordList:
        word2 = ''
        for i in range (len(word)):
            if word[i].isalpha():
                word2 += word[i].lower()
        wordList[wordList.index(word)] = word2

    while '' in wordList:
        wordList.remove('')


    wordSet= set(wordList)


    file.close()

    return wordSet;

# return second file 
def unique2(fileName2):
    file = open(fileName2, 'r')

    text = file.read()
    text = text.replace('\n', ' ')
    
    wordList = text.split(' ')

    for word in wordList:
        word2 = ''
        for i in range (len(word)):
            if word[i].isalpha():
                word2 += word[i].lower()
        wordList[wordList.index(word)] = word2

    while '' in wordList:
        wordList.remove('')


    wordSet2= set(wordList)


    file.close()

    return wordSet2;

# get all the differences 
def getWords(wordSet, wordSet2):

    union = ', '.join(wordSet.union(wordSet2))
    intersection = ', '.join(wordSet.intersection(wordSet2))
    in1 = ', '.join(wordSet.difference(wordSet2))
    in2 = ', '.join(wordSet2.difference(wordSet))
    difference = ', '.join(wordSet.symmetric_difference(wordSet2))

    return union, intersection, in1, in2, difference;

# tell user the differences 
def output(union, intersection, in1, in2, difference):
    print("Here are the words that are in either texts:")
    print(union)
    print("\n")

    print("Here are the words that are in both texts:")
    print(intersection)
    print("\n")

    print("Here are the words that are in the first text:")
    print(in1)
    print("\n")

    print("Here are the words that are in the second text:")
    print(in2)
    print("\n")

    print("Here are the words that appear in the one but not both:")
    print(difference)
    print("\n")

main()
time.sleep(3) 
    




