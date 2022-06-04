"""
Создать класс Money для работы с денежными суммами в котором для рублей и копеек предусмотрены независимые целочисленные данные. Реализовать метод вывода суммы на экран. На основе класса Money создать класс Good для работы с товаром. Предусмотреть метод, осуществляющий уменьшение цены на заданное число процентов.
"""


class Money:
    def __init__(self, rub, kop):
        self.rub = int(rub)
        self.kop = int(kop)

    def show(self):
        total = float(self.rub) + float((self.kop / 100))
        return total


class Good(Money):
    pass

    def procent(self):
        procent = self.show() - self.show() * 0.15
        return f'Сумма к оплате после скидки - {procent} рублей'


test1 = Good(439, 999)
print(test1.show())
print(test1.procent())
