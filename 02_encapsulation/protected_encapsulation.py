class Mammal:
    def __init__(self, local = 'Angola') -> None:
        self.localization = local
        self._size = 1.23 # protected attribute
    
    def _walk(self) -> None: # protected method
        print(f'the animal is walking in {self.localization}')

class Dog(Mammal):
    def __init__(self, name: str, localization: str) -> None:
        super().__init__(localization)
        self.name = name

    def bark(self) -> None:
        print(f'the dog {self.name} is barking in {self.localization}')


my_dog = Dog('Rex', 'Angola')   

my_dog.bark()
my_dog._walk() # this method is protected