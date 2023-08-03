# I will create a class named Pet and use the init method to create attributes

class Pet:
    # I will now initiate the init method to initialize the specific attibutes
    
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
        
    # I will create individual methods that will assign a value to the attributes
    
    def set_name(self, name):
        self.__name = name
        
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
        
    def set_age(self, age):
        self.__age = age
    
    # I will create multiple methods that will return a value for each attribute
    
        def get_name(self):
            return self.__name
        
        def get_animal_type(self):
            return self.__animal_type
        
        def get_age(self):
            return self.__age
        