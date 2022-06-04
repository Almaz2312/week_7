"""
Setup and practice PostgreSQL in linux terminal
"""


class Product:
    def __init__(self, name, price, weight):
        self.__name = name
        self.__price = price
        self.__weight = weight

    def get_price(self):
        return self.__price

    def get_name(self):
        return self.__name

    def get_weight(self):
        return self.__weight


class Buy(Product):
    def __init__(self, name, price, weight, quantity):
        super(Buy, self).__init__(name, price, weight)
        self.__quantity = quantity

    def get_quantity(self):
        return self.__quantity

    def calculation(self):
        name = self.get_name()
        price = self.get_price()
        weight = self.get_weight()
        quantity = self.get_quantity()
        total_price = price * quantity
        total_weight = weight * quantity
        print(f'Product: {name}\nPrice: {price}\nWeight: {weight}\n'
              f'Total weight: {total_weight}\nTotal price: {total_price}')


class Check(Buy):
    # def __init__(self, name, price, weight, quantity):
    #     super().__init__(name, price, weight, quantity)
    pass


obj = Check('bread', 57, 12, 100)
obj.calculation()