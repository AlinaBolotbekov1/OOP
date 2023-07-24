'''
Основные принципы ООП: Инкапсуляция
'''

'''
Принцип ООП у которого есть две трактовки: 
1. Объединение всех свойств и методов в единую капсулу или класс
2. Сокрытие данных ->  ограничение доступа к методам  и атрибутам
'''

# 1. Инкапсуляция как связь

# class Phone:
#     number = '+996777888999' 

#     def print_num(self):
#         print(f'Мой номер: {self.number}')

# nokia = Phone()
# nokia.print_num()
'''Связали поведение объекта с его данными'''

# 2. Инкапсуляция как сокрытие данных (управление доступом)

# class Point:
#     def __init__(self, x, y):
#         self._x = x
#         self._y = y

# pt = Point(5, 7)
# pt._x = 'hello'
# print(pt._x, pt._y)

# pt = Point(4, 5)
# print(pt.x , pt.y)

# pt.x = 8
# pt.y = 'coord_y'
# print(pt.x , pt.y)

# 3 модификатора доступа 
# 1. public -> публичный (без нижнего подчеркивания) - данные доступны всем (name, x, y, number, print_number, create ...)
# 2. _protected -> защищенный (с одним подчеркиванием в начале) -> данные доступны как внутри класса, так и у дочерних
# 3. __private -> приватный (с двумя подчеркиваниями) - данные доступны только внутри класса которому они принадлежат

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y

#     def set_coord(self, new_x, new_y):
#         if type(new_x) in (int, float) and type(new_y) in (int, float):
#             self.__x = new_x
#             self.__y = new_y
#         else:
#             raise ValueError('Координаты должны быть числами')
        
#     def get_coords(self):
#         return self.__x, self.__y
    

# pt = Point(5, 7)
# print(pt.get_coords())
# pt.set_coord(2, 4)
# print(pt._Point__x, pt._Point__y)


# class A(Point):
#     pass
# a = A(2, 3)
# print(a.__dict__)
# pt = Point(5, 7)
# # pt._x = 'hello'
# pt._Point__x = 'hello'
# print(pt.__dict__)

# getter, setter -> методы через которые предполагается работа с приватами  и защищенными атрибутами и методами. Чтобы избежать прямого обращения
# setter -> метод , для задания (установки) нового значения атрибутам (в нем реализовывается доролнительная проверка присваиваемых значений)
# getter -> метод для получения защищенных и приватных атрибутов



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
   
#     def set_age(self, new_age):
#         if type(new_age) != int:
#             raise ValueError('Введите возраст в числовом формате')
#         if new_age < self.__age:
#             raise ValueError('Вы не могли помолодеть')
#         if 0 < new_age < 110:
#             self.__age = new_age   
#         else: print('Invalid age')
            
    
#     def get_age(self):
#         return self.__age

# person = Person('Alina', 22)   
# person.set_age(23)
# print(person.get_age())


'''ЗАДАЧА С ДЕКОРАТОРОМ'''

   

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age

#     @property
#     def age(self):
#         return self.__age 
    

#     @age.setter
#     def age(self, new_age):
#         if type(new_age) != int:
#             raise ValueError('Введите возраст в числовом формате')
#         if new_age < self.__age:
#             raise ValueError('Вы не могли помолодеть')
#         if 0 < new_age < 110:
#             self.__age = new_age   
#         else: print('Invalid age')
            
#     @age.getter
#     def age(self):
#         return self.__age

# person = Person('Alina', 22)   
# person.age = 23
# print(person.age)


# class Russia:
#     __name = 'Russian Federation'
#     __population = 0

#     @property
#     def population(self):
#         return self.__population
    

#     @population.setter
#     def population(self, new_population):
#         if not isinstance(new_population, (int, float)) or not new_population > 0:
#             raise ValueError('Invalid values')
#         self.__population  = new_population

# rus = Russia()
# rus.population = 2000
# print(rus.population)


# class Person:
#   def __init__(self, name, age, password):
#     self.name = name
#     self._age = age
#     self.__password = password

#   def name(self):
#     return self.name
  

#   @property
#   def age_password(self):
#     return self._age and self.__password

#   @age_password.setter
#   def age(self, new_age, new_password):
#     if type(new_age) != int:
#       raise ValueError('Введите свой возраст в числовом формате')
    
#     if len(new_password) < 8:
#       raise Exception('Должно быть больше 8 символов')
    
#     else:
#       self._age = new_age
#       self.__password = new_password

# a = Person('Alina', 22, 12345678)
# a.age_password = 78
# print(a.age_password)


