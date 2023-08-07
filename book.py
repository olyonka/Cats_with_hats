class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Book(Product):
    def __init__(self, name, price, quantity, author):
        super().__init__(name, price, quantity)
        self.author = author

    def read(self):
        print(
            f"Book Information:\nTitle: {self.name}\nAuthor: {self.author}\nPrice: {self.price}\nQuantity: {self.quantity}")


# Example usage
book = Book('My little magic', 999.99, 1000000, 'O. Olena')

book.read()