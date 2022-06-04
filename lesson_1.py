# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_area(self):
#         area = self.width * self.height
#         return area
#
#     def per(self):
#         perimetr = 2 * (self.width + self.height)
#         return perimetr
#
#     def is_square(self):
#         if self.height == self.width:
#             return 'It is a square'

"""
Наследование
"""

# class Doctor:
#     def __init__(self, name, education, age, gender):
#         self.name = name
#         self.education = education
#         self.age = age
#         self.gender = gender
#
#     def tread(self, patient):
#         print(f'{patient} - Здоров')
#
#     def get_info(self):
#         print(self.name, self.age, self.education, self.gender, self.opyt)


# Наследует класс доктор, как его методы так и его атрибуты
# class Dantist(Doctor):
#     def __init__(self, opyt, name, education, age, gender):
    #     self.opyt = opyt
    #     self.name = name
    #     self.education = education
    #     self.age = age
    #     self.gender = gender
    # Вместо того чтобы так пописывать легче начледовать через Doctor.__init__
    #     Doctor.__init__(self, name, education, age)
#         super().__init__(name, education, age, gender)
#         self.opyt = opyt
#
#     def tread(self, patient):
#         print(f'{patient} покажите зубы')
#
#
# class Travmatolog(Dantist, Doctor):
#     pass

# doctor = Doctor('Nazgul', 'politeh', 33, 'female')
# doctor.get_info()
# dan1 = Dantist(4, 'Naz', 'har', 34, 'male')
# dan1.get_info()
# dan1.tread('Nodira')

#
# doc1 = Doctor('Macintosh', 'masachusets', 34, 'male')
# trav1 = Travmatolog(2, 'Bill', 'Oxford', 45, 'male')
# trav1.tread('Mark')
# trav1.get_info()
# doc1.get_info()

class PhoneOld:
    def __init__(self, model, memory):
        self.model = model
        self.memory = memory

    def get_memory(self):
        return self.memory


class Camera:
    def __init__(self, pix, count):
        self.pix = pix
        self.count = count

    def set_pix(self, pm):
        self.pix += pm
        return self.pix


class NewPhone(PhoneOld, Camera):
    # Прописыва.тся оба т.к оба класса не связанны друг с другом
    def __init__(self, model, memory, pix, count):
        PhoneOld.__init__(self, model, memory)
        Camera.__init__(self, pix, count)

    def set_pix(self, pm):
        self.pix = (self.pix + pm) * self.count
        return self.pix


ph1 = NewPhone('Samsung', '1t', 677, 4)
ph2 = NewPhone('Samsung1', '2t', 7, 1)
ph3 = NewPhone('Samsung2', '3t', 77, 3)
cam = Camera(77, 4)
cam1 = Camera(97, 5)
lists = [ph1, ph2, ph3, cam, cam1]
for i in lists:
    print(i.set_pix(34))


# ph2 = NewPhone('Iphone', '2t', 455, 3)
# print(ph1.get_memory())
# print(ph1.set_pix(34))

