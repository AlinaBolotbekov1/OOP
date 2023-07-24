'''
Методы экземпляра, класса, статические
'''

# 1. Методы экземпляра класса (instance methods)
# 2. Методы класса (class methods)
# 3. Статические методы (Static methods)

# 1. Методы экземпляра  - обычные методы, которые первым аргументом принимают self (ссылка на объект), нужны для работы с атрибутами объекта

# class A:
#     def instance_method(self):
#         print('Метод экземпляра (объекта)')
#         print('первый аргумент', self)
# obj = A()
# # obj.instance_method()
# A.instance_method(obj)

# 2. Методы класса - метод , который принимает первым аргументом ссылку на класс (cls). Нужны для создания объектов или изменения атрибутов класса.Для создания нужно задекорировать его classmethod

# class B:
#     @classmethod
#     def class_method(cls):
#         print('Метод класса')
#         print('Первый аргумент', cls)


# # B.class_method()
# b = B()
# b.class_method()

# class Car:
#     color = 'green'
#     @classmethod
#     def change_color(cls, value):
#         cls.color = value # меняет состояние класса, что сказывается на всех объектах, созданных от этого класса, методы класса не меняют состояние одного из объектов

#     # def change_color(self, value):
#     #     self.color = value # меняет состояние конкретного объекта

# b = Car()
# a = Car()
# a.change_color('red')
# print(a.color, b.color)

# class Pizza:
#     def __init__(self, radius, *ingredients):
#         self.radius = radius
#         self.ingredients = ingredients

#     def cook(self):
#         print(f'Готовится пицца размером {self.radius} см')
#         print(f'Ингредиенты: {self.ingredients}')

#     @classmethod
#     def four_cheeze(cls, r):
#         pizza = cls(r, 'Моцарелла', 'Чеддер', 'Голландский', 'Дор-Блю')
#         return pizza


# # pizza1 = Pizza(15, 'пепперони', 'чили', 'ананас', 'шоколадная паста','сыр')
# # pizza1.cook()
# pizza_four_cheeze = Pizza.four_cheeze(20)
# pizza_four_cheeze.cook()

# 3. Статические методы -> декоратор @staticmethod, просто функции внутри класса, не принимают ссылку ни на объект, ни на класс. Не взаимодействуют с классом и объектом. Используются только внутри класса. (Дополнительные функции,которые производят какие-то вычисления, преобразование типа данных и тд.)

# class C:
#     @staticmethod
#     def pow_(z):
#         return z ** 2
    

# # c = C()
# # print(c.pow_(3))
# print(C.pow_(3))


# class Cylinder:
#     def __init__(self, diametr, hight):
#         self.diametr = diametr
#         self.hight = hight
#         self.area = self.get_area(diametr, hight)

#     @staticmethod
#     def get_area(d, h):
#         from math import pi
#         circle = pi * d**2 / 4
#         side = pi * d * h
#         area = circle * 2 + side
#         return round(area, 2)
    
# c1 = Cylinder(10, 4)
# print(c1.area)


# class Home:
#     people = 0

#     def __init__(self, name, count_people, last_name):
#         self.name = name 
#         self.count_people = count_people
#         Home.people += count_people
#         self.last_name = last_name

#     def info(self):
#         print(f'Квартира в этом доме принадлежит {self.name} {self.last_name}')

#     @classmethod
#     def f(cls):
#         print(cls.people)

#     @staticmethod
#     def about_home():
#         print('Самый многоэтажный дом')

# a = Home('John', 3, 'Snow')
# b = Home('Sam', 5, 'Snow')
# b.info()
# a.f()
# a.about_home()


# class SmartPhone:
#     __battery_level = 100

#     def __init__(self,imei, os):
#         self.__imei = imei
#         self.__os = os
    
#     def check_battery(self, battery):
#         if self.__battery_level <= battery:
#             raise Exception('Телефон разряжен')

#     @property
#     def battery_level(self):
#         print(self.__battery_level)

#     @property
#     def get_info(self):
#         self.charge_battery(1)
#         self.__battery_level -= 0.5
#         print(f'ОС: {self.__os}\nIMEI: {self.__imei}')

    

#     def play_music(self):
#         self.charge_battery(5)
#         self.__battery_level -= 5
#         print('Слушаем Мирбека Атабекова')
        

#     def video(self):
#         self.charge_battery(10)
#         self.__battery_level -= 7
#         print('Смотрим А4')


#     def charge_battery(self, sec):
#         from datetime import datetime, timedelta
#         from time import sleep
#         now = datetime.now
#         end_time = (now() + timedelta(seconds=sec)).strftime('%M:%S')

#         while now().strftime('%M:%S') != end_time:
#             sleep(1)
#             if self.__battery_level < 100:
#                 self.__battery_level += 1
#             if self.__battery_level == 100:
#                 print(f'Телефон заряжен на {self.__battery_level}%')
#                 break
#             print(f'Идет зарядка, уровень заряда: {self.__battery_level}%')

# a = SmartPhone('123w', 'android')
# # a.play_music()
# a.video()
# # a.video()
# # a.video()
# # a.video()
# # a.video()
# # a.video()
# # a.video()
# # a.video()
# # a.video()
# # a.video()
# # a.video()
# # a.video()
# a.charge_battery(10)