"""
Определить класс Car с полями название, цвет, цена, const полем CompanyName.

Создать  конструктор - дефолтный и с параметрами.
Создать свойство доступа к полю цвет.

Определить методы Input () - для ввода данных о машине с консоли ,
Print () - для вывода данных о машине на консоль
и ChangePrice (float x) - для изменения цены на х% Ввести данные о 3 авто.

Уменьшить их цену на 10%, вывести данные об авто. Ввести новый цвет
и покрасить авто с цветом white в указанный цвет
"""


class Car:
    def __init__(self, model, color, price):
        self.model = model
        self.__color = color
        self.price = price

    def input_information(self):
        information = input("Car's additional information: ")
        return information

    def change_price(self):
        discount = float(self.price) * 0.1
        final = self.price - discount
        return final

    @property
    def get_color(self):
        return self.__color

    @get_color.setter
    def change_color(self, new):
        self.__color = new


car1 = Car('BMW', 'black', 20000)
car2 = Car('Mercedez', 'black', 22000)
car3 = Car('Audi', 'black', 15000)
print(f"Price has changed to: {car1.change_price()}")
car3.change_color = input('New color: ')
print(f"Color has been changed to {car3.get_color}")
