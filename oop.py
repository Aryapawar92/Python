#oop concept

# classes

class Car:

    total = 0

    def __init__(self, model , name , colour , wheel):
        self.model = model
        self.name = name
        self.__wheel = wheel
        # private attribute
        # encapsulation done here

        self.__colour = colour
        Car.total += 1

    def owner(self):
        return f"{self.name} owns it"
    
    #getter method
    def getWheel(self):
        return f"{self.__wheel}"
    
    #setter method
    def setWheel(self , wheel):
        self.__wheel = wheel
    
    def fuelType(self):
        return "It uses Petrol/Diesel"
    
    def carColor(self):
        return f"{self.__colour}"
    
#Inheritance

class ElectricCar(Car):
    def __init__(self, model, name , type , colour , wheel):
        #this is used when you need anything from the parent class
        super().__init__(model, name,colour, wheel)
        self.type = type

    def carType(self):
        return f"{self.type}"
    
    #polymorphism - same method in different classes with different output
    def fuelType(self):
        return "It is a electric car"
    

    
# object

AryaCar = Car("ciaz" , "arya" , "red" , 0)
PrishiCar = ElectricCar("Tesla" , "prishi" , "electric","black" , 1)

# object uses the method in the class

print(AryaCar.owner())
print(AryaCar.fuelType())
print(AryaCar.carColor())
print(AryaCar.getWheel())
AryaCar.setWheel(2)
print(AryaCar.getWheel())

#class variable
print(Car.total)

print(PrishiCar.carType())
print(PrishiCar.fuelType())
print(PrishiCar.carColor())