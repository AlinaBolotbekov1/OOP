'''
Основные принципы ООП: Наследование
'''

# Основные принципы: Наследование, Полиморфизм, Инкапсуляция

# Остальные принципы: Ассоциация (Агрегации, Композиции), Абстракция

'''Синтаксис для наследования'''
# class Родительский_класс:
#       методы_и_атрибуты_родительского_класса

# class Дочерний_класс(Родительский_класс):
#       методы_и_атрибуты_дочернего_класса

'''
Наследование - принцип ООП , в котором мы можем унаследовать, переопределить и использовать методы и атрибуты родительского класса в дочернем классе. Создаем новый класс на основе уже существующего
'''



# class A:
#     def func1(self, a):
#         print(self, a)

# class B(A):
#     def __str__(self):
#         return 'Это объект класса B'

# b = B()
# b.func1(10)



# class A:
#     def func(self):
#         print('Я метод в классе A')

# class C(A):
#     '''
# Наследовали все методы и атрибуты класса А и полностью переопределили метод func
# '''
#     def func(self):
#         print('Я метод в классе C')

# c = C()
# a = A()
# # c.func()
# a.func()


'''
MRO -> method resolution order
порядок поиска атрибутов
'''

# class A:
#     x = 'x in A'
#     y = 'y in A'

# class B(A):
#     x = 'x in B'

# a = A()
# b = B()
# print(B.mro()) # [<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
# print(B.__mro__) # (<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
# print(b.x)
# print(b.y)
# print(a.x)
# print(a.y)

'''
Виды наследования
'''
# Одиночное наследование -> когда дочерний класс наследуется только одного родителя
# Иерархическое наследование -> когда у одного родительского  класса много дочерних классов
# Многоуровневое наследование -> когда дочерний класс наследуется от класса у которого есть родитель
# Множественное наследование -> когда дочерний класс наследуется от нескольких родительских классов
# Гибридное наследование -> когда используется несколько видов наследований

'''
Множественное наследование
'''

# isinstance() -> проверка является ли объект экземпляром класса
# issubclass() -> проверяет является ли класс подклассом второго аргумента

# class A:
#     pass

# class B(A):
#     pass

# class C(B):
#     pass

# a = A()
# b = B()
# c = C()
# print(issubclass(C, A))
# print(issubclass(B, A))
# print(isinstance(a, object))
# print(isinstance(c, A))

# class User:
#     def __init__(self, username, age, city, password):
#         self.username = username
#         self.age = age
#         self.city = city
#         self.password = password

#     def get_profile_info(self):
#         print(f'Имя пользователя: {self.username}\nВозраст: {self.age}\nГород проживания: {self.city}')

#     def great_user(self):
#         print(f'Добро пожаловать {self.username}')

# class Admin(User):
#     def __init__(self, username, age, city, password):
#         super().__init__(username, age, city, password)
#         self.privileges = []

#     def __str__(self):
#         # return super().__str__()
#         return self.username
    
#     def set_privileges(self, privileges):
#         self.privileges.append(privileges)
        
#     def show_privieges(self):
#         return self.privileges
    

    
# admin = Admin('admin', 34, 'Bishkek', 12345678)
# # print(admin)
# admin.set_privileges('delete posts')
# admin.set_privileges('delete users')
# print(admin.show_privieges())
# admin.get_profile_info()
# admin.great_user()


# class Lion:
#     color = 'black'

# class Lioness:
#     color = 'brown'

# class Child(Lion, Lioness):
#     pass

# obj = Child()
# print(obj.color)
# print(Child.__mro__)


'''
Проблемы множественного наследования

'''

# 1. Проблема ромба -> решена с помощью mro

# class A:
#     pass

# class B(A):
#     pass

# class C(A):
#     pass

# class D(B, C):
#     pass

# print(D.__mro__)


# class X:
#     pass

# class Y:
#     pass

# class Z:
#     pass

# class A(X, Y):
#     pass

# class B(Y, Z):
#     pass

# class M(B, A, Z):
#     pass

# print(M.__mro__)


# Проблема перекрестного наследования (не решена)

# class A:
#     pass

# class B:
#     pass

# class C(A, B):
#     pass

# class D(B, A):
#     pass

# class M(C, D):
#     pass

# не решенная проблема скрещенного наследования

'''
Миксины -> классы которые используются для наследования, но от них не создаются объекты
'''

#используются для добавления одних и тех же методов в разные классы

# Работа с Mixin
# 1. принято давать имена заканчивающиеся на Mixin: CreateMixin, GetListMixin ...
# 2. он не предназначен для создания от него объектов.
# 3. нужны для расширения функционала другого класса

# class MoveMixin:
#     def move(self):
#         print(f'{self} и я двигаюсь')

# class StopMixin:
#     def stop(self):
#         print('я стою')
# class Car(MoveMixin, StopMixin):
#     def __str__(self):
#         return 'Я красная машина'

# class Person(MoveMixin, StopMixin):
#     def __str__(self):
#         return 'Я человек'
    
# objs = [Car(), Car(), Person()]
# for i in objs:
#     i.move()

# class CreateMixin:
#     def create(self, todo, key):
#         if key in self.todos:
#             return 'Задача под таким номером уже существует'
#         else:
#             self.todos[key] = todo
#             return self.todos

# class DeleteMixin:
#     def delete(self, key):
#         deleted = self.todos.pop(key)
#         return deleted
    
# class UpdateMixin:
#     def update(self, key, new_value):
#         if key in self.todos.keys():
#             self.todos[key] = new_value
#             return self.todos
        
# class ReadMixin:
#     def read(self):
#         return sorted(self.todos.items())

# class Note(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
#     todos = {}

# task = Note()
# task.create('h/w', 8)
# task.create('h/w', 9)
# task.create('h/w', 5)
# task.update(8, 'homework')
# task.update(5, 'shopping')
# task.delete(9)
# print(task.read())
# print(task.todos)

# class Parent1:
#     pass
# class Parent2:
#     pass
# class Child(Parent1, Parent2):
#     pass

# # c = Child()
# print(Child.__mro__)


# class A:
#     def hello(self):
#         print('hello world')

# class B:
#     def hello(self):
#         print('HELLO WORLD')

# class C(B, A):
#     pass
# obj = C()
# # obj.hello()

# class GraphicalEntity:
#     def __init__(self, pos_x, pos_y, size_x, size_y):
#         self.pos_x = pos_x
#         self.pos_y = pos_y

#         self.size_x = size_x
#         self.size_y = size_y
# class Button(GraphicalEntity):
#     def __init__(self, pos_x, pos_y, size_x, size_y):
#         super().__init__(pos_x, pos_y, size_x, size_y)
#         self.status = False
#     def toggle(self):
#         self.status = not self.status

# class LimitSizeMixin:
#     def __init__(self, pos_x, pos_y, size):
#         size_x = min(size_x, 500)
#         size_y = min(size_y, 400)
#         super().__init__(pos_x, pos_y, size_x, size_y)

# class LimitSizeButton(Button, LimitSizeMixin):
#     pass
# b = LimitSizeButton(10, 20, 200, 100)