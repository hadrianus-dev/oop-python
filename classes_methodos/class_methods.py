class ShoppingCart:
    tax = 1.5 # static attribute
    def __init__(self, items: list) -> None:
        self.items = items

    def calculate_total_tax(self) -> float:
        total_tax = self.tax * sum(item['price'] for item in self.items)
        return total_tax
    
    @classmethod
    def changeTax(cls, value: float) -> None:
        cls.tax = value  # change the static attribute value


shopping_cart = ShoppingCart([{'name': 'apple', 'price': 0.5}, {'name': 'banana', 'price': 10}])
print(shopping_cart.calculate_total_tax())  # 1.5
print('-------Change Tax--------')
ShoppingCart.changeTax(2.5)
print(shopping_cart.calculate_total_tax())  # 2.0