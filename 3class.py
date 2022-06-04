"""
Разработать три класса, которые следует связать между собой, используя наследование:класс Product, который имеет три элемент-данных — имя, цена и вес товара (базовый класс для всех классов);класс  Buy, содержащий данные о количестве покупаемого товара в штуках, о цене за весь купленный товар и  о весе товара (производный класс для класса Product и базовый класс для класса Check);класс Check, не содержащий никаких элемент-данных. Данный класс должен выводить на экран информацию о товаре и о покупке ( производный класс для класса Buy);
Для взаимодействия с данными классов разработать set- и get—методы. Все элемент-данные классов объявлять как private.
"""


class Product:
    def __init__(self, name, price, weight):
        self.__name = name
        self.__price = price
        self.__weight = weight

    @property
    def get_name(self):
        return self.__name

    @property
    def get_price(self):
        return self.__price

    @property
    def get_weight(self):
        return self.__weight

    @get_name.setter
    def name_setter(self, new):
        self.__name = new

    @get_price.setter
    def price_setter(self, new):
        self.__price = new

    @get_weight.setter
    def weight_setter(self, new):
        self.__weight = new


class Buy(Product):
    def __init__(self, name, price, weight, quantity):
        super().__init__(name, price, weight)
        self.__quantity = quantity

    @property
    def get_quantity(self):
        return self.__quantity

    @property
    def get_total_weight(self):
        self.__total_weight = self.get_weight * self.get_quantity
        return self.__total_weight

    @property
    def get_total_price(self):
        self.__total_price = self.get_quantity * self.get_price
        return self.__total_price

    @get_quantity.setter
    def setter(self, new):
        self.__quantity = new

    def show_information(self):
        return f'Product name: {self.get_name}\nProduct price: {self.get_price}\n' \
               f'Product weight: {self.get_weight}\nBuying products quantity: {self.get_quantity}\n' \
               f'Buying products total weight: {self.get_total_weight}\n' \
               f'Buying products total price: {self.get_total_price}'


class Check(Buy):
    pass


obj = Check('Bread', 57.0, 0.2, 10)
print(obj.show_information())
