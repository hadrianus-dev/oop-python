class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # this is a public method
    # this method can be called from outside the class
    def presentation(self):
        print(f'Hello my name is {self.name} and I am {self.__checkIfIsAdult()}')

    # this is a private method
    # this method can only be called from inside the class
    def __checkIfIsAdult(self):
        if self.age >= 18:
            return 'Adult'
        else:
            return 'Minor'
        
p1 = Person("John", 36)
p1.presentation()