#Jordan Pulaski
#jordan.pulaski001@albright.edu
#PE 2
class Car:
    
    def __init__(self, model, make, speed):
        self.__model = model
        self.__make = make
        self.__speed = 0

    def setModel(self, model):
        self.__model = model

    def setMake(self, make):
        self.__make = make

    def setSpeed(self, speed):
        self.__speed = speed

    def getModel(self):
        return self.__model

    def getMake(self):
        return self.__make

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def getSpeed(self):
        return self.__speed
