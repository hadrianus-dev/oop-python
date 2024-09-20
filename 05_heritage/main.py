class Mammal:
    def __init__(self, local = 'Angola') -> None:
        self.localization = local
    
    def walking(self) -> None:
        print(f'the animal is walking in {self.localization}')

class Dog(Mammal):
    def __init__(self, name: str, age: int, localization: str) -> None:
        super().__init__(localization)
        self.name = name
        self.age = age

    def bark(self) -> None:
        print(f'the dog {self.name} is barking in {self.localization}')


my_dog = Dog('Rex', 3, 'Angola')

my_dog.bark()
my_dog.walking()