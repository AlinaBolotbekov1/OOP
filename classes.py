# ''' Введение в ООП '''
# ''' ООП -> парадигма программирования, в которой все основывается на двух понятиях: Class и Object'''

# #  Парадигма -> набор правил , идей, понятий которые определяют стиль написания кода

# '''
# Классы -> чертеж , описание того, какими свойствами и поведением будет обладать объект 
# '''

# # Свойства -> обычные переменные 
# # Поведение -> обычные функции (их называют методами)

# '''
# Объект = Экземпляр класса = Инстанция -> это экземпляр класса с собственным состоянием этих свойств. Каждый объект является экземпляром определенного класса
# '''

# # '''Синтаксис'''

# # class A: #-> Обьявили класс
# #     string = 'объект от класса A' #-> Создали переменную класса (атрибут класса)

# #     def some_method(self): #-> Создали метод (функция, которая определенна внутри класса) self -> ссылка на объект 
# #         pass
        

# #     def __str__(self): # строковое представление объекта (можно указать что будет выводится при попытке распечатать объект) (без этого метода выводится ссылка на объект)
# #         return self.string

# # a = A()
# # print(a)

# class Person:
#     legs = 2
#     arms = 2

#     def __init__(self, name, age):

#         '''
#         отвечает за инициализацию объекта  вызывается, когда мы создаем объект self -> ссылка на созданный объект. Здесь определяются атрибуты объекта
#         '''
#         self.name = name
#         self.age = age

# # print(dir(Person))
# sam = Person('Sam', 24)
# # sam.last_name = 'Lee'
# print(sam.name)
# # print(sam.last_name)
# # print(dir(sam))


'''
Атрибуты класса -> переменные внутри класса (атрибуты на уровне класса -> используется чтобы создать константу, которая не предполагается быть измененной)
К ним можно обращаться через класс и через объект
'''
'''
Методы и атрибуты объекта (экземпляры класса)
это методы и атрибуты, которые есть у объекта, но возможно их нет у класса
Атрибуты уровня объекта/инстанции класса/экземпляра класса -> определяются в методе __init__ (к атрибутам объекта нельзя обратиться через класс)
'''

'''
 Объекты класса -> объекты созданные по шаблону/чертежу класса
'''

# class A:
#     var1 = 'Переменная класса'

#     def __init__(self):
#         self.var2 = 'Переменная объекта'

# print(dir(A))
# a = A()
# print(dir(a))




# class Salary:
#     nalog = 15

#     def __init__(self, zp, staj):
#         self.zp = zp
#         self.staj = staj

#     def sum_nalog(self):
#         return self.zp * self.staj * self.nalog / 100
    
# a = Salary(10000, 9)
# print(a.sum_nalog())

        
# class Circle:
#     color = 'Синий'
#     pi = 3.14
#     def __init__(self,radius=int):
#         self.radius = radius

#     def get_area(self):
#         return self.pi * self.radius ** 2

# circle = Circle(radius = 2)
# circle.color = 'yellow'
# print(circle.color)
# print(circle.get_area())

# class BankAccount:
#     def __init__(self):
#         self.balance = 0
    
#     def withdraw(self, amount):
#         self.balance -= amount 
#         return f'Ваш баланс: {self.balance}'

#     def deposit(self, amount):
#         self.balance += amount
#         return f'Ваш баланс: {self.balance}' 

# account = BankAccount()
# print(account.deposit(1000))
# print(account.withdraw(500))

# class BankAccount: 
#     def __init__(self): 
#         self.balance = 0 
#     def withdraw(self, amount): 
#         self.balance -= amount 
#         print(f'Ваш баланс: {self.balance} сом') 
#     def deposit(self, amount): 
#         self.balance += amount 
#         print(f'Ваш баланс: {self.balance} сом') 
# account = BankAccount() 
# account.deposit(1000) 
# account.withdraw(500)

# class Taxi:
#     def __init__(self, name, cost, cost_km):
#         self.name = name
#         self.cost = cost
#         self.cost_km = cost_km

#     def get_total_cost(self, km):
#         self.cost  = self.cost_km * km + self.cost
#         return f' Такси {self.name}, стоимость поездки:{self.cost} сом'

# taxi1 = Taxi(name='Namba',cost=29, cost_km=15)
# taxi2 = Taxi(name='Yandex',cost=25, cost_km=17)
# taxi3 = Taxi(name='Jorgo',cost=28, cost_km=15)

# print(taxi1.get_total_cost(10)) 
# print(taxi2.get_total_cost(6)) 
# print(taxi3.get_total_cost(14)) 

# import random
# class Sniper:

#     def __init__(self, name):
#         self.name = name
#         self.health = 100
#     def shoot(self,sniper):
#         sniper.health -= 20

# sniper1 = Sniper(name='Max')
# sniper2 = Sniper(name='Tom')

# choices = (sniper1, sniper2)

# while True:
#     shooter = random.choice(choices)
#     if shooter == sniper1:
#         shot = sniper2
#     else:
#         shot = sniper1

#     shooter.shoot(shot)
#     print(f'Снайпер {shooter.name} стреляет, у {shot.name} {shot.health} баллов здоровья')

#     if sniper1.health == 0:
#         print(f'{sniper1.name} убит, {sniper2.name} победил!')
#     elif sniper2.health == 0:
#         print(f'{sniper2.name} убит, {sniper1.name} победил!')
#         break
#     else:
#         continue


# class Hogwarts:

#     faculties_qualities = {'courage': 'Gryffindor',
#                            'intellegince': 'Ravenclaw',
#                            'justice': 'Hufflepuff',
#                            'ambition': 'Slytherin'}
#     def __init__(self, courage, intellegince, justice, ambition):
#         self.courage = courage
#         self.intellegince = intellegince 
#         self.justice = justice
#         self.ambition = ambition
#         self.qualities_dict = locals()
#         # print(self.qualities_dict)

#     def sorting_hat(self):
#         dict_ = {val: key for key, val in self.qualities_dict.items() if type(val) == int}
#         # print(dict_)
#         max_point = max(dict_.keys())
#         # print(max_point)
#         max_quality = dict_[max_point]
#         # print(max_quality)
#         self.faculty = Hogwarts.faculties_qualities[max_quality]
#         print(f'{self.faculty}!!!')

# student1 = Hogwarts(courage = 5, intellegince = 8, justice = 3, ambition = 9)
# student2 = Hogwarts(courage = 5, intellegince = 7, justice = 78, ambition = 0)
# student3 = Hogwarts(courage = 52, intellegince = 7, justice = 2, ambition = 0)
# student4 = Hogwarts(courage = 21, intellegince = 122, justice = 17, ambition = 8)


# student1.sorting_hat()
# student2.sorting_hat()
# student3.sorting_hat()
# student4.sorting_hat()
    

# class Salary:
#     percent = 8

#     def __init__(self, salary, experience):
#         self.salary = salary
#         self.experience = experience

#     def count_percent(self):
#         return self.salary * self.experience * self.percent / 100

# obj = Salary(salary=10000, experience=10)
# print(obj.count_percent())


# import datetime

# class Nobel:
#     def __init__(self, category, year, winner):
#         self.category = category
#         self.year = year
#         self.winner = winner

#     def get_year(self):
#         today = datetime.datetime.now()
#         res = today.year - self.year
#         return f'Выиграл {res} лет назад'

# winner1 = Nobel("Литература", 1971, "Пабло Неруда") 
# print(winner1.category, winner1.year, winner1.winner) 
# print(winner1.get_year())

  
# winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ") 
# print(winner2.category, winner2.year, winner2.winner) 
# print(winner2.get_year())

# class Password:
 
#     def __init__(self, password): 
#         self.password = password 
#     def __str__(self) -> str:
#         return '*' * len(self.password) 
        
#     def validate(self): 
#         if not len(self.password) == 8 and len(self.password) < 15: 
#             return f'Password should be longer than 8, and less than 15' 
#         if not any(map(lambda i: i.isdigit(), self.password)): 
#             return f'Password should contain numbers too' 
#             if not any(map(lambda i: i.isalpha(), self.password)): 
#                 return f'Password should contain letters as well' 
                
#                 if not any(map(lambda i: i in ['@', '#', '&', '$', '%', '!', '~', '*'], self.password)): 
#                     return f'Your password should have some symbols' 
#                     return f'Ваш пароль сохранен.' 
# password = Password('sanem23@') 
# print(password.validate()) 
# print(password)


# class Bag:
#     brand = 'GUCCHI'
#     def buy_bag(self, brand):
#         self.brand = brand
# bag1 = Bag()
# bag2 = Bag()
# bag1.buy_bag('CHANEL')
# print(bag1.brand)
# print(bag2.brand)

# class Lipstick:
#     color = 'red'
#     def set_color(self, color):
#         self.color = color
# Lipstick().set_color('pink')
# print(Lipstick().color)


