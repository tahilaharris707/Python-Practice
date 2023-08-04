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
    