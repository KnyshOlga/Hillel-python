class Item:

    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f"{self.name}, price: {self.price}"


lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")

print(lemon)
print(apple)


class User:

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname}"


buyer = User("Ivan", "Ivanov", "02628162")

print(buyer)


class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
        return f"User: {self.user} \nItems: \n{', '.join([f'{product.name}: {cnt} pcs.' for product, cnt in self.products.items()])}"

    def get_total(self):
        self.total = sum(product.price * cnt for product, cnt in self.products.items())
        return self.total


cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)

print(cart)

assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"

cart.add_item(apple, 10)
print(cart)

assert cart.get_total() == 40
