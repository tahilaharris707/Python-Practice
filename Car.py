# I will create a class named "car" with some data attributes and use the init module
# that will initialize the year model and make of the car

class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
        self.__jump = 5
        
        # I will create a module that will increase the car's speed.
        def accelerate(self):
            self.__speed += self.__jump
            
        # I will create a module that will decrease the car's speed.
        def brake(self):
            self.__speed -=self.__jump
            
        # I will create a module that will return the current speed of the car.
        def get_speed(self):
            return self.__speed