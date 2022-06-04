"""
@staticmethod, @classmethod, @isinstance()
"""
from datetime import date, datetime


class Person:
    date_now = datetime.now()

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def year_age(cls, name, year):
        age = datetime.now().year - year
        return cls(name, age)

    def get_info(self):
        print(self.name, self.age)

    @staticmethod
    def is_true(age):
        if age >= 18:
            return True
        return False


person1 = Person('Almaz', 27)
person1.get_info()
person2 = Person.year_age('Nazgul', 1995)
person2.get_info()
print(person1.is_true(20))

"""
Посмотреть IO gram. Асинхронное создание телеграм бота
"""