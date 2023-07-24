'''
Магические методы в Python (dunder -> double underscore)
'''

# Супер методы
# Служебные методы

# Методы, у которых два нижних подчеркивания в начале и в конце. Мы их не вызываем напрямую, вызываются определенными операторами и функциями 

# __str__, __init__

# __new__ -> конструктор класса, отвечает за создание объекта
# __init__ -> инициализатор, задает созданному объекту атрибуты
# __del__ -> деструктор, отвечает за удаление объекта (срабатывает , когда мы заканчиваем работу с объектом)


# class Point:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         print('Метод init')
    
#     def __del__(self):
#         print('Удаление экземпляра' + str(self))

# point = Point(2, 6)
# b = Point(3, 5)


# class Point:

#     def __new__(cls, *args, **kwargs):
#         print('Вызов метода __new__ для класса' + str(cls))
#         return super().__new__(cls)
    
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         print('Метод init')


# a = Point(3, 7)
# print(a)


# class Word(str):
#     def __new__(cls, *args):
#         string = args[0].replace(' ', '')
#         return str.__new__(cls, string)
    
# word1 = Word('h e l l o')
# print(word1)


# class User:
#     def __new__(cls, name, age):
#         if age > 18:
#             return super().__new__(cls)
#         raise ValueError('Вы слишком молоды')
    
#     def __init__(self, name , age):
#         self.name = name 
#         self.age = age 

#     def __del__(self):
#         print('Пока')
#         # pass

#     def __str__(self):
#         return self.name
    
#     def __repr__(self):
#         return self.name
    
# user1 = User('Sam', 19)
# print(user1)


# import datetime

# print(str(datetime.date.today()))
# print(repr(datetime.date.today()))

# __str__() -> для удобного чтения
# __repr__() -> Ссылка на объект в памяти

# если не определен __str__, то str() использует __repr__

# class MyNumber(int):
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other: int):
#         return f'Это сложение и результат равен: {self.value + other}'
    
#     def __sub__(self, other: int):
#         return f'Это вычитание и результат равен: {self.value - other}'
    
#     def __mul__(self, other: int):
#         return f'Это умножение и результат равен: {self.value * other}'
    
#     def __pow__(self, other: int):
#         return f'Это возведение в степень и результат равен: {self.value ** other}'
    
#     def __truediv__(self, other: int):
#         return f'Это деление и результат равен: {self.value / other}'
    
#     def __floordiv__(self, other: int):
#         return f'Это целочисленное деление и результат равен: {self.value // other}'
    
#     def __mod__(self, other: int):
#         return f'Это остаток от деление и результат равен: {self.value % other}'

    # __truediv__ (деление -> вызывается оператором /)
    # __floordiv__(целочисленное деление -> вызывается оператором //)
    # __mod__(остаток от деления -> вызывается оператором %)
    # __pow__(возведение в степень -> вызывается оператором **, pow)


# obj = MyNumber(10)
# print(obj + 8)
# print(obj - 8)
# print(obj * 8)
# print(obj ** 8)
# print(obj / 8)
# print(obj // 8)
# print(obj % 8)


'''
Магические методы сравнения
'''

# == -> __eq__(self, other) (equal) - равно 
# != -> __ne__(self, other) (not equal) - не равно
# > -> __gt__(self, other) (greater than) - больше
# < -> __lt__(self, other) (less than) - меньше
# >= -> __ge__(self, other) (greater equal) - больше или равно
# <= -> __le__(self, other) (less equal) - меньше или равно

# __invert__(self) -> переворачивает итерируемый объект (~)
# base = Base('Hello world')
# print(~base) 

# __hash__() -> хеширует данные 
# print(hash('hello'))

# __getattribute__(self, item) -> автоматически вызывается при считывании атрибута через экземпляр класса(получение свойства объекта с именем item )

# string = 'hello'
# print(string.lower)
# print(string.__getattribute__('lower'))

# __getattr__ -> вызывается автоматически, каждый раз, когда идет обращение к несуществующему атрибуту объекта (когда атрибут не найден)

# __setattr__ -> вызывается автоматически, когда идет присвоение к какому-нибудь атрибуту определенного значения 

# __delattr__ -> вызывается, когда удаляется атрибут из экземпляра


# from typing import Any


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __getattribute__(self, item: str) -> Any:
#             print('getattribute')
#             return super().__getattribute__(item)
#             # if item == 'x':
#             #     raise ValueError('Доступ запрещен')
#             # return super().__getattribute__(item)

#     def __setattr__(self, item: str, value) -> None:
#         print('setattr')
#         super().__setattr__(item, value)


#         if item == 'z':
#             raise AttributeError('Недопустимое имя атрибута')
#         super().__setattr__(item, value)

#     def __getattr__(self, item):
#         print('getattr')
#         # return False -> дефолтное значение несуществующего атрибута

#     def __delattr__(self, item: str):
#         print('delattr')
#         super().__delattr__(item)
         
         
         
# a = Point(2, 3)
# # del a.x -> delattr
# # a.z = 2 -> 
# # a.y = 3
# # a.u = 3
# # a.k -> getattr
# print(a.__dict__)


# __getitem__ -> когда мы обращаемся в квадратных скобках (по индексу, по ключу, делаем срезы)

# string = 'hello'
# print(string[0])
# print(string.__getitem__(0))

# __setitem__ -> когда создаем пару ключ: значение или изменяем
# __delitem__ -> когда удаляем

# class A:
#     def __getitem__(self, index):
#         print('getitem')
        


#     def __setitem__(self, a, b):
#         print('setitem')
        

#     def __delitem__(self, index):
#         print('delitem')
        

# a = A()
# a.list_ = [1, 2, 3]
# # a.dict_ = {0: 'hello'}
# a[1]
# a[1] = 9
# del a[2]
