# I will write a class named Person and assign the init function with attributes listed.

class Person:
    def__init__(self, name, address, telephone):
        self.__name = name
        self.__address = address
        self.__telephone = telephone
    
    # I will create multiple def modules to set the name, address and telephone number of a person
    
    def set_name(self, name):
        self.__name = name
        
    def set_address(self, address):
        self.__address = address
        
    def set_telephone(self, address):
        self.__telephone = telephone
    
    
    # I will create get modules for each attribute to get the results of a person.
    
    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_telephone(self):
        return self.__telephone
    
# I will write a class named Customer with a subclass named Person.

class Customer(Person):
    
    # I will create an init function using the subclasses.
    
    def__init__(self, name, address, phone, customer_number, mailing_list):
        Person.__init__(self, name, address, phone)
        
        # I will create multiple def modules using the attributes of the class Person.
        self.__customer_number = customer_number
        self.__mailing_list = mailing_list
        
    def set_customer_number(self, customer_number):
        self.__customer_number = customer_number
        
    def set_mailing_list(self, mailing_list):
        self.__mailing_list =  mailing_list
        
    def get_customer_number(self):
        return self.__customer_number
    
    def get_mailing_list(self):
        return self.__mailing_list
    
        
        