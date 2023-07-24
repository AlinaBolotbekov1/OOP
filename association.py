'''
Абстракция -> Принцип ООП , в котором создается класс-пустышка, где задаются названия атрибутов и методов, чтобы не забыть их переопределить в дочерних классах
'''
# from abc import ABC, abstractmethod, abstractproperty

# class Abstract(ABC):
#     # a = 10

#     def method1(self):
#         print('method1')

#     @abstractmethod
#     def method2(self):
#         pass

#     @abstractproperty
#     def method3(self):
#         pass

# class A(Abstract):
#     def method2(self):
#         print('Переопределили абстрактный метод')
#     method3 = 9


# a = A()
# a.method1()


# Абстрактный класс - не предназначен для создания от него объектов. Он предоставляет общие атрибуты и методы для всех дочерних классов, чтобы уменьшить дублирование кода

# Абстрактный метод - это метод обязателен для переопределения в дочернем классе ( есть объявление, но нет реализации) для создания такого метода используется декоратор abstractmethod


# class Abst(ABC):

#     @abstractmethod
#     def get_info(self):
#         pass

#     @abstractmethod
#     def set_info(self):
#         ...

# class IdenticateMixin:
#     def identicate(self, year):
#         if int(year) < 2015:
#             return 'This is not new car'
#         return 'This is a new car'
    
# class BaseAuto(IdenticateMixin, Abst):

#     def __init__(self, model, year, owner):
#         self.model = model
#         self.year = year
#         self.__owner = owner


#     def get_info(self):
#         return f'Model: {self.model}\nYear: {self.year}'
    
#     def set_info(self, owner):
#         self.__owner = owner

#     def get_owner(self):
#         return self.__owner
    
# # auto = BaseAuto('Kia', 2014, 'Sam')
# # print(auto.identicate(auto.year))
# # auto.set_info('Alice')
# # print(auto.get_owner())

# class Auto(BaseAuto):
#     def __init__(self, model, year, owner, brand, color):
#         super().__init__(self, model, year, owner)
#         self.brand = brand
#         self.color = color

#     def get_info(self):
#         return f'Model: {self.model}\nYear: {self.year}\nBrand: {self.brand}\nColor: {self.color}'

#     @property
#     def owner(self):
#         return self.__owner

#     @owner.setter
#     def owner(self, owner):
#         self._BaseAuto__owner = owner

#     @owner.getter
#     def owner(self):
#         return self._BaseAuto__owner
    
#     @owner.deleter
#     def get_owner(self):
#         self._BaseAuto__owner = 'Nobody'

# a = Auto('X6', 2022, 'BMW','green')
# print(a.get_info())
# a.owner  = 'Peter'
# del a.owner
# print(a.owner)
        

'''
Ассоциация -> принцип ООП , в котором два класса связаны друг с другом
'''

# Агрегация -> слабая связь
# Композиция -> сильная связь

'''
Композиция 
'''
# A - компонент
# |
# |
# V
# B - составной

# class Wheel:
#     pass

# class Engine:
#     pass

# class Freshener:
#     pass

# class Car:
#     def __init__(self, freshener):
#         self.engine = Engine()
#         self.wheels = [Wheel(), Wheel(), Wheel(), Wheel()] # композиция
#         self.freshener = freshener # агрегация

# elochka = Freshener() # агрегация

# car = Car(elochka)
# del car
# print(elochka)
# print(car.__dict__)

# class Salary:
#     def __init__(self, pay):
#         self.pay = pay
    
#     def getTotal(self):
#         return (self.pay * 12)
    
# class Employee:
#     def __init__(self, pay,bonus):
#         self.pay = pay
#         self.bonus = bonus
#         self.salary = Salary(self.pay)

#     def annualSalary(self):
#         return f'Total: {self.salary.getTotal() + self.bonus}'
    
# emp = Employee(10000, 2000)
# print(emp.annualSalary())


# class Salary:
#     def __init__(self, pay):
#         self.pay = pay
    
#     def getTotal(self):
#         return (self.pay * 12)
    
# class Employee:
#     def __init__(self, salary, bonus):
#         self.bonus = bonus
#         self.salary = salary

#     def annualSalary(self):
#         return f'Total: {self.salary.getTotal() + self.bonus}'

# salary = Salary(10000)   
# emp = Employee(salary, 2000)
# print(emp.annualSalary())


# class Battery:
#     _power = 100


#     def charge(self):
#         if self._power < 100:
#             self._power = 100

# class IPhone:
#     def __init__(self, color):
#         self.color = color
#         self.battery = Battery()


# class Nokia:
#     def __init__(self, battery:Battery, color:str='black') -> None:
#         self.color = color
#         self.battery = battery

# battery = Battery()

# nokia = Nokia(battery, 'dark blue')
# iphone = IPhone('red')
# # iphone.battery._power = 50
# # iphone.battery.charge()
# # print(iphone.battery._power)
# # print(nokia.battery._power)


# del iphone
# # del nokia
# print(battery)
