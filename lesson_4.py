class Product:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight


class Buy(Product):
    def __init__(self, name, price, weight, quantity):
        Product.__init__(name, price, weight)
        self.quantity = quantity
        self.total_weight = self.weight * self.quantity
        self.total_price = self.price * self.quantity

    def get_information(self):
        return f'Product information is: {self.name, self.price, self.weight}.' \
               f'Buying products information is: {self.name, self.total_price, self.total_weight,self.quantity}'


class Check(Buy, Product):
    pass


onj = Check('Bread', 57.0, 0.2, 10)
print(onj.get_information())