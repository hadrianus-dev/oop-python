class Switcher:
    def __init__(self, room: str):
        self.room = room

    def turn_on(self) -> None:
        print(f'Turned on the {self.room} light')

    def turn_off(self) -> None:
        print(f'Turned off the {self.room} light')

class Person:
    def __init__(self, switcher: Switcher):
        self.switcher = switcher

    def turn_on_light(self) -> None:
        self.switcher.turn_on()
    
    def turn_off_light(self) -> None:
        self.switcher.turn_off()

my_switcher = Switcher('bedroom')
my_person = Person(my_switcher)
my_person.turn_off_light()
my_switcher = Switcher('kitchen')
my_person = Person(my_switcher)
my_person.turn_on_light()
