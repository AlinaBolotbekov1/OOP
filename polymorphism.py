'''
Основные принципы ООП: Полиморфизм
'''

# Разное поведение одного и того же метода в разных классах

# +

# 4 + 7
# 'str' + 'srting'
# [1, 2, 3] + ['r', 'y']

# len() -> str, list, dict, tuple

# pop 
# list.pop() удаляет с конца, удаляет по индексно
# dict.pop() удаляет по ключу
# set.pop() удаляет рандомно

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f"It's a cat. Cat's name is {self.name}")

#     def make_sound(self):
#         print('meow, meow')



# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f"It's a dog. Dog's name is {self.name}")

#     def make_sound(self):
#         print('gav, gav')


# cat = Cat('Charlie', 3)
# dog = Dog('Kutya', 4)

# for i in (cat, dog):
#     i.make_sound()
#     i.info()

# from math import pi
# class SHape:
#     def __init__(self, name):
#         self.name = name

#     def area(self):
#         pass

#     def fact(self):
#         print('Я фигура в двумерном пространстве')

#     def __str__(self):
#         return self.name
    
# class Square(SHape):

#     def __init__(self, length):
#         super().__init__('Square')
#         self.length = length

#     def area(self):
#         print(self.length ** 2)


#     def fact(self):
#         print('У квадрата все стороны равны')

# class Circle(SHape):
#     def __init__(self, radius):
#         super().__init__('Circle')
#         self.radius = radius

#     def area(self):
#         print(pi * self.radius ** 2)

# square = Square(5)
# circle = Circle(3)

# circle.area()
# circle.fact()
# square.area()
# square.fact()

# for i  in [Square(5), Square(9), Circle(8), Circle(5)]:
#     print(i)
#     i.area()
#     i.fact()
