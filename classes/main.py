class MyClass:
    # class is a blueprint for creating objects. They are an representation of objects or real-world entities.
    # attributes are variables that belong to the class.
    # methods are functions that belong to the class.

    # constructor, every class can have a constructor method. 
    # The constructor method is called when an instance of the class is created.
    def __init__(self, a, b):
        # attributes
        self.a = a 
        self.b = b

    # methods
    # methods can have parameters. In this case we have one parameter c.
    def method_one(self, c):
        return self.a + self.b + c
    
