class MyClass:
    # this is the first pillar of oop, the encapsulation
    # encapsulation is a way to hide the implementation details from the user of the class 
    def __init__(self) -> None:
        self.__value = None

    def setter_value(self, value: int) -> None:
        self.__value = value

    def getter_value(self) -> int:
        return self.__value


my_class = MyClass()

my_class.setter_value(10)

print(my_class.getter_value())