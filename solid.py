# SRP
# как не стоит делать

# class ExportCSV:
#     def __init__(self, data):
#         self.data = self.prepare(data)


#     def prepare(self, data):
#         result = ''
#         for item in data:
#             new_line = ', '.join(
#                 [
#                 item['name'],
#                 item['surname'],
#                 item['proffesion']
#                 ]
#             )
#             result += f'{new_line}\n'
#         return result

#     def write_file(self, filename):
#         with open(filename, 'w') as file:
#             file.write(self.data)

# data = [
#     {
#         'name': 'Sam',
#         'surname': 'Grey',
#         'proffesion': 'detective'

#     },
#     {
#         'name': 'John',
#         'surname': 'Black',
#         'proffesion': 'doctor'

#     }
# ]
# export = ExportCSV(data)
# export.write_file('data.csv')


# соблюдение принципа
# class FormatData:
#     def __init__(self, data):
#         self.data = data

#     def prepare(self, ):
#         result = ''
#         for item in self.data:
#             new_line = ', '.join(
#                 [
#                 item['name'],
#                 item['surname'],
#                 item['proffesion']
#                 ]
#             )
#             result += f'{new_line}\n'
#         return result

    
# class ExportCSV:
#     def __init__(self, filename):
#         self.filename = filename
        


#     def write(self, data):
#         with open(self.filename, 'w') as file:
#             file.write(data)

# data = [
#     {
#         'name': 'Sam',
#         'surname': 'Grey',
#         'proffesion': 'detective'

#     },
#     {
#         'name': 'John',
#         'surname': 'Black',
#         'proffesion': 'doctor'

#     }
# ]
# export = ExportCSV(data)
# export.write_file('data.csv')
# format = FormatData(data)
# formated = format.prepare()
# # print(formated)
# writer = ExportCSV('data.csv')
# writer.write(formated)

# Принцип open/close -> OCP
# как не стоит делать
# import time
# class Logger:
#     def log(self, message):
#         current_time = time.localtime()
#         print(time.strftime('%Y-%m-%d %H:%M:%S', current_time), message)

# l = Logger()
# l.log('Error')

# желательно делать так
# import time
# class Logger:
#     def __init__(self):
#         self.format = '%Y-%m-%d %H:%M:%S'


#     def log(self, message):
#         current_time = time.localtime()
#         print(time.strftime(self.format, current_time), message)

# class CustomLogger(Logger):
#     def __init__(self):
#         self.format = '%Y-%m-%d'

# class Custom1(Logger):
#     def __init__(self):
#         self.format = '%H:%M:%S'

# l = Logger()
# l.log('Error')
# custom = CustomLogger()
# custom.log('Error')
# cust = Custom1()
# cust.log('Error')


# from enum import Enum
# не правильный вариант OCP
# class Product(Enum):
#     SHIRT = 1
#     PANT = 2
#     TSHIRT = 3

# class DiscountCalculator:
#     def __init__(self, product_type, cost):
#         self.product_type = product_type
#         self.cost = cost

#     def get_discount_price(self):
#         if self.product_type == Product.SHIRT:
#             return self.cost - (self.cost * 0.10)
#         elif self.product_type == Product.PANT:
#             return self.cost - (self.cost * 0.15)
#         elif self.product_type == Product.TSHIRT:
#             return self.cost - (self.cost * 0.25)


# Правильный вариант OCP    
# from abc import ABC, abstractmethod

# class DiscountCalculator(ABC):

#     @abstractmethod
#     def get_discount_price(self):
#         pass

   
# class DiscountCalcShirt(DiscountCalculator):
#     def __init__(self, cost: int):
#         self.cost = cost

#     def get_discount_price(self):
#         return self.cost - (self.cost * 0.10)
    
# class DiscountCalcTShirt(DiscountCalculator):
#     def __init__(self, cost: int):
#         self.cost = cost

#     def get_discount_price(self):
#         return self.cost - (self.cost * 0.25)

# class DiscountCalcPant(DiscountCalculator):
#     def __init__(self, cost: int):
#         self.cost = cost

#     def get_discount_price(self):
#         return self.cost - (self.cost * 0.15)


# LSP

# class Animal:
#     def __init__(self, attrs):
#         self.attributes = attrs

#     def eat(self):
#         print('Ate some food')

# class Cat(Animal):
#     def eat(self, amount = 100):
#         if amount > 300:
#             print('Too much')
#         else:
#             print('Ate some cat food')

# class Dog(Animal):
#     def eat(self):
#         print('Ate some dog food')

# cat1 = Cat({'name': 'Murka', 'age': 2})
# dog = Dog({'name': 'Rex', 'age': 4})
# # cat2 = Cat(('Barsik',3))

# animal = [cat1, dog]
# for i in animal: 
#     print(i.attributes['age'])

# class Animal:
#     def __init__(self, name, age):
#         self.attributes = {'name': name, 'age': age}

#     def eat(self, _amout=0):
#         print('Eat')

# class Cat(Animal):
#     def __init__(self, name, age):
#         super().__init__(name, age)


#     def eat(self, amount = 100):
#         if amount > 300:
#             print('Too much')
#         else:
#             print('Ate some cat food')

# class Dog(Animal):
#     def __init__(self, name, age):
#         super().__init__(name, age)

#     def eat(self, _amount = 0):
#         print('dogs food')

# cat = Cat('Murka', 4)
# dog = Dog('Rex', 5)

# animals = [cat, dog]
# for animal in animals:
#     print(animal.attributes['age'])


# ISP

# class Creature:
#     def __init__(self, name):
#         self.name = name

#     def swim(self):
#         pass

#     def walk(self):
#         pass

#     def fly(self):
#         pass

#     def talk(self):
#         pass

# class Human(Creature):
#     def swim(self):
#         print('Я могу плавать')

#     def walk(self):
#         print('Я могу ходить')

#     def talk(self):
#         print('Я могу говорить')

# class Fish(Creature):
#     def swim(self):
#         print('Я могу плавать')

#     def fly(self):
#         print('Я могу летать')

# fish = Fish('ll')
# fish.talk()
# human = Human('Sam')
# human.fly()


# class Creature:
#     def __init__(self, name):
#         self.name = name

# class Swimmer:
#     def swim(self):
#         pass

# class Walker:
#     def walk(self):
#         pass
#     def run(self):
#         pass
        

# class Talker:
#     def talk(self):
#         pass

#     def skrim(self):
#         pass

# class Human(Creature, Walker, Swimmer, Talker):
#     pass



# DIP

# class Terminal:
#     def write(self, message):
#         print(message)

# class FileWriter:
#     def write(self, message):
#         with open('log.txt', 'w') as file:
#             file.write(message)
# import time
# class Logger:
#     def __init__(self):
#         self.prefix = time.strftime('%Y-%m-%d:%H:%M:%S', time.localtime())

#     def log_str(self, msg):
#         Terminal().write(msg)

#     def log_file(self, msg):
#         FileWriter().write(msg)

# logger = Logger()


# class Terminal:
#     def write(self, message):
#         print(message)

# class FileWriter:
#     def write(self, message):
#         with open('log.txt', 'w') as file:
#             file.write(message)
# import time

# class Logger:
#     def __init__(self):
#         self.format = '%Y-%m-%d:%H:%M:%S'

#     def log(self, msg, class_):
#         prefix = time.strftime(self.format, time.localtime())
#         class_().write(msg)

# logger = Logger()
# logger.log('Error', FileWriter)
# logger.log('Error', Terminal)