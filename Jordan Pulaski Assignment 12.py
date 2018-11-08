#Jordan Pulaski
#jordan.pulaski001@albright.edu
#Algorithm Workbench 1,2,3 Program Exercise 1

#Algorithm Workbench 1
#main function
def main():
    name = userInput()
    writeFile(name)

def userInput():
    outfile = input("Please input the name of your file: ")

    while len(outfile) <= 0:
        outfile = input("Please input the name of your file: ")       
        
    return outfile;

#write name in document   
def writeFile(name):
    outfile = open(name, 'w')
    outfile.write('Jordan Pulaski\n')

#close file
    outfile.close()

#call main
main()

#Algorithm Workbench 2
#main 
def main():
    name = readFile()
    output(name)

#opening file    
def readFile():
    outfile = open('jordanPulaski.txt', 'r')
    name = outfile.readline()
    outfile.close()
    return name

#printing whats in the file
def output(name):
    print(name)
    return

#call main    
main()

#Algorithm Workbench 3
#main function
def main():
    outfile = userInput()
    getFile(outfile)
    readFile(outfile)
    return

#get file name
def userInput():
    outfile = input("Please input the name of your file: ")
    while len(outfile) <= 0:
        outfile = input("Please input the name of your file: ")

    return outfile

#put numbers in file
def getFile(outfile):
    outfile = open(outfile, 'w')

    for numbers in range(0,101,1):
        outfile.write(str(numbers)+"\n")
#close and tell user numbers are there        
    outfile.close()
    print("Numbers have been put in file")
    return outfile
#prints whats in the file
def readFile(outfile):
    infile = open(outfile, 'r')
    line = 0
    while line != '':
        line = infile.readline()
        line = line.rstrip('\n')
        print(line)
    infile.close()
    return

main()

#Programming Exercise 1
#main
def main():
    outfile = userInput()
    readFile(outfile)
    return

#get name of file
def userInput():
    outfile = input("Please input the name of your file: ")
    while len(outfile) <= 0:
        outfile = input("Please input the name of your file: ")

    return outfile
#read back whats in file
def readFile(outfile):
    infile = open(outfile, 'r')
    line = 0
    while line != '':
        line = infile.readline()
        line = line.rstrip('\n')
        print(line)
    #close
    infile.close()
    return

#close main
main()

    
