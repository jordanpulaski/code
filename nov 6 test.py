#Jordan Pulaski
#jordan.pulaski001@albright.edu
#PE 2 part 2

import Car

def main():
    
    carModel = input("What is the model of your car?: ")
    carMake = input("What is the make of your car? ")
    carSpeed = int(input("What is the speed of your car?: "))

    myCar = Car.Car(carModel, carMake, carSpeed)
    for i in range(5):
        myCar.accelerate()
        carSpeed = myCar.getSpeed()
        print(carSpeed)
        
    for i in range(5):
        myCar.brake()
        carSpeed = myCar.getSpeed()
        print(carSpeed)


main()
