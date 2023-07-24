# class Person:
#     def __init__(self, name, age, last_name):
#         self.name = name
#         self.age = age
#         self.last_name = last_name


#     def display_info(self):
#         print(f'Name: {self.name}\nLast_name: {self.last_name}\nAge: {self.age}\nClass_: {self.class_}\nFaculty: {self.faculty}')

# class Employee(Person):
#     def work(self):
#         print(f'{self.name} works')

# class Students(Person):
#     # def __init__(self, name, age, last_name, class_, faculty):
#     #     self.name = name
#     #     self.age = age
#     #     self.last_name = last_name
#     #     self.class_ = class_
#     #     self.faculty = faculty

#     # def __init__(self, name, age, last_name, class_, faculty):
#     #     Person.__init__(self, name, age, last_name)
#     #     self.class_ = class_
#     #     self.faculty = faculty

#     def __init__(self, name, age, last_name, class_, faculty):
#         super().__init__(name, age, last_name)
#         self.class_ = class_
#         self.faculty = faculty

# # worker = Employee('Ben', 34, 'Snow')
# # worker.display_info()

# student = Students('Ben', 24, 'Snow', 4, 'IT')
# student.display_info()



# class A:
#     def my_range(self, num):
#         print(list(range(num + 1)))
#         # list_ =[i for i in range(num + 1)]
#         # print(list_ )

# a = A()
# a.my_range(10)


# class A:
#     def my_range(self, start, end, step):
#         i = start
#         while i < end:
#             yield i
#             i += step


# class Mylist(list):
#     def insert(self, arg1, arg2):
#         print('First arg - element, second arg - index')
#         super().insert(arg2, arg1)

# list1 = Mylist([1, 2, 3, 4, 5])
# list1.insert('Hello', 4)
# print(list1)


# import random

# class Languages:
#     students_count = 0
    
#     def __init__(self):
#         Languages.students_count += 1

#     def coding(self):
#         raise NotImplementedError


# class Python(Languages):
#     students_count = 0

#     def __init__(self):
#         super().__init__()

#     def coding(self):
#         print('I am Python student. I am coding now.')

#     def __str__(self):
#         return 'Python'

# class JavaScript(Languages):
#     students_count = 0

#     def __init__(self):
#         super().__init__()

#     def coding(self):
#         print('I am JavaScript student. I am coding now.')

#     def __str__(self):
#         return 'JavaScript'


# student1 = Python()
# student2 = JavaScript()

# my_choice = input('Угадай студента\n')
# computer_choice = random.choice([student1, student2])
# computer_choice.coding()


# if computer_choice.__str__() == my_choice:
#     print('Good job!!!')
# else:
#     print('No bueno ;/')


# class MyDict(dict): 
#     def get(self,key,default = 'Are you kidding?'): 
#         return dict.get(self,key,default) 
# obj_dict = MyDict({'some_title': 2}) 
# print(obj_dict.get('some'))

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print(f'name:{self.name} age:{self.age}')

# class Student(Person):
#     def __init__(self, name, age, faculty):
#         super().__init__(name, age)
#         self.faculty = faculty

#     def display_student(self):
#         print(f'name:{self.name} age:{self.age} faculty:{self.faculty}')

# obj_student = Student('Rick', 21, 'science')
# obj_student.display() 
# obj_student.display_student() 


# class SmartPhones: 
#     def __init__(self, name, color, memory): 
#         self.name = name 
#         self.color = color 
#         self.memory = memory 
#         self.battery = 0 
#     def __str__(self): 
#         return f"{self.name} {self.memory}" 
#     def charge(self, number): 
#         self.battery += number 
# class Iphone(SmartPhones): 
#     def __init__(self, name, color, memory, ios): 
#         super().__init__(name, color, memory) 
#         self.ios = ios 
#     def send_imessage(self, string): 
#         return f"sending {string} from {self.name} {self.memory}" 
# class Samsung(SmartPhones): 
#     def __init__(self, name, color, memory, android): 
#         super().__init__(name, color, memory) 
#         self.android = android 
#     def show_time(self): 
#         import datetime 
#         return datetime.datetime.now().time() 
# phone = SmartPhones('generic', 'blue', '128GB') 
# print(phone) 
# print(phone.battery) 
# phone.charge(20) 
# print(phone.battery) 
# iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
# print(iphone7) 
# print(iphone7.send_imessage('hello')) 
# samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo') 
# print(samsung21.show_time())

# class MyString(str): 
#     def __init__(self, stroka1): 
#         self.stroka1 = stroka1 
#     def append(self, stroka2): 
#         self.stroka2 = stroka2 
#         self.stroka1 = self.stroka1 + self.stroka2 
#         return self.stroka1 
#     def pop(self): 
#         last_w = self.stroka1[-1] 
#         self.stroka1 = self.stroka1[:-1] 
#         return last_w 
#     def __str__(self) -> str: 
#         return self.stroka1 
# example = MyString('String') 
# example.append('hello') 
# print(example.pop()) 
# print(example) 

# class ContactList:
#     def __init__(self, list_):
#         self.list_ = list_
    
#     def search_by_name(self, name):
#         a = []
#         for i in self.list_: 
#             if name in i: a.append(i)
#         return a

# all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
# print(all_contacts.search_by_name('Olya'))


'''==============МНОЖЕСТВЕННОЕ НАСЛЕДОВАНИЕ И МИКСИНЫ======================'''
# class Auto:
#     def ride(self):
#         print('Riding on a ground')

# class Boat:
#     def swim(self):
#         print('Floating on water')

# class  Amphibian(Auto, Boat):
#     pass

# obj =  Amphibian()
# obj.ride() 
# obj.swim()

# class RadioMixin:
#     def play_music(self):
#         title = 'title'
#         print(f'Песня называется {title}')

# class Auto:
#     pass

# class Boat(RadioMixin):
#     pass

# class Amphibian(Auto, Boat, RadioMixin):
#     pass
# auto = Auto()
# boat = Boat()
# obj = Amphibian()
# obj.play_music         

# class Clock:
#     def current_time(self):
#         import datetime
#         datetime.now()


# class Clock:
#     def current_time(self):
#         print('17:10:41')

# class Alarm: 
#     def on(self): 
#         print('08:00:00') 
#     def off(self): 
#         print('09:00:00') 
        
# class AlarmClock(Clock, Alarm): 
#     def alarm_on(self): 
#         print('Будильник включён') 
        
# clock = AlarmClock() 
# clock.current_time()
# clock.alarm_on()

# class Watch:
#     def see_time(self):
#         from datetime import datetime
#         print(datetime.now().time())
    
#     def where_to_wear(self):
#         print('You should wear me on your hand')

# class SmartPhone:
#     def call(self, num):
#         self.num = num
#         return num
        

#     def where_to_wear1(self):
#         print('You can keep me anywhere')

# class SmartWatch(Watch, SmartPhone):
#     pass

# smart = SmartWatch()
# smart.see_time()
# print(smart.call())
# smart.where_to_wear()
# smart.where_to_wear1()






# class Smartphone:
#     def call(self, num):
#         return self.num


# class Watch:
#     def see_time(self,time):
        

# class Smartwatch(Smartphone, Watch):


# class A:
#   def method1(self):
#     print('Hello World')

# class B(A):
#   pass

# b = B()
# b.method1()


# class A:
#   def public(self):
#     return 'Публичный'

#   def _protected(self):
#     return 'Защищенный'

#   def __private(self):
#     return 'Приватный'


# a = A()
# print(a.public())
# print(a._protected())
# print(a._A__private())

# class Car:
#     __speed = 0

#     def set_speed(self, new_speed):
#         self.__speed = new_speed

#     def show_speed(self):
#         return self.__speed

# car1 = Car()
# print(car1.show_speed()) 
# car1.set_speed(20) 
# print(car1.show_speed())

# class Car:
#     __speed = 0

#     @property
#     def speed(self):
#         return self.__speed

#     @speed.setter
#     def speed(self, new_speed):
#         self.__speed = new_speed

    
# car1 = Car() 
# print(car1.speed) 
# car1.speed = 20 
# print(car1.speed)

# class Person: 
#     name = "John" 
#     _phone_number = "+996 557 55 17 57" 
#     __card_number = "9999 9999 9999 9999" 
    
#     @property 
#     def number(self): 
#         return self.__card_number 
        
# john = Person() 
# print(john.name) 
# print(john._phone_number) 
# print(john.number)

# class Person:
#     def __init__(self, name, phone_number, card_number):
#         self.name = name
#         self._phone_number = phone_number
#         self.__card_number = card_number
#     @property 
#     def number(self): 
#         return self.__card_number
# john = Person("John", "+996 557 55 17 57","9999 9999 9999 9999")  
# print(john.name) 
# print(john._phone_number) 
# print(john.number)


# class Person: 
#     name = "John" 
#     _phone_number = "+996 557 55 17 57" 
#     __card_number = "9999 9999 9999 9999" 

#     def get_number(self): 
#         return self.__card_number 
#     def set_number(self): 
#         self.__card_number = None 
#         return self.__card_number 
        
# john = Person() 
# john.name = None 
# john._phone_number = None 
# print(john.name) 
# print(john._phone_number) 
# print(john.set_number())

# class Person: 
#     def __init__(self, name, phone_number, card_number): 
#         self.name = self.__validate_name(name) 
#         self._phone_number = phone_number 
#         self.__card_number = card_number 
#     def __validate_name(self, name): 
#         if len(name) < 2: 
#             return "John" 
#         else: 
#             return name.title() 
#     def get_card_number(self): 
#         return self.__card_number 
#     def set_card_number(self, card_number): 
#         self.__card_number = card_number 
        
# sam = Person("SAM", "+996 557 55 17 57", "9999 9999 9999 9999") 
# print(sam.name) 
# print(sam._phone_number) 
# print(sam.get_card_number())


# a = 'makers'
# b = [1, 2, 3]
# c = {'alice': 24}
# d = [a, b, c]
# for i in d:
#     print(len(i))


# class Dog:
#     def voice(self):
#         print('Гав')

# class Cat:
#     def voice(self):
#         print('Мяу')


# def to_pet(name1):
#     name1.voice()
   


# barsik = Cat()
# rex = Dog()
# for i in (barsik, rex):
#     i.voice()



# class Person: 
#     def __init__(self, name, last_name): 
#         self.name = name 
#         self.last_name = last_name 
#     def get_info(self): 
#         return f"Привет, меня зовут {self.name} {self.last_name}" 
# class Employee(Person): 
#     def __init__(self, name, last_name, work, status): 
        
#         super().__init__(name, last_name) 
#         self.work = work 
#         self.status = status 
#     def get_info(self): 
#         return f"{super().get_info()}, я работаю в компании {self.work} на должности {self.status}" 
        
# class Student(Person): 
#     def __init__(self, name, last_name, university, course): 
#         super().__init__(name, last_name) 
#         self.university = university 
#         self.course = course 
#     def get_info(self): 
#         return f"{super().get_info()}, я учусь в {self.university} на {self.course} курсе" 
        
# def get_human_info(human): 
#     print(human.get_info()) 
# person = Person("Иван", "Иванов") 
# employee = Employee("Иван", "Петров", "Рога и Копыта", "директор") 
# student = Student("Иван", "Петров", "КГТУ", 3) 
# get_human_info(employee) 
# get_human_info(student) 
# get_human_info(person)


# 1)Создайте класс MathUtils с staticmethod под названием multiply, который принимает два аргумента и возвращает их произведение.

# class MathUtils:
#     @staticmethod
#     def multiply(x, y):
#         return x * y
    
# m = MathUtils()
# print(m.multiply(2, 4))

# 2)Создайте класс DateUtils с classmethod под названием is_valid_date, который принимает строку в формате даты (например, "2023-07-18") и проверяет, является ли эта дата действительной. Метод должен возвращать True, если дата действительна, и False в противном случае.
# class DateUtils:
#     @classmethod
#     def is_valid_date(cls, data: str):
#         from datetime import datetime
#         a = datetime.now().strftime('%Y-%m-%d')
#         if a == data:
#             return 'True'
#         else:
#             return 'False'
        
# a = DateUtils()
# print(a.is_valid_date('2023-07-18'))

    


# Создайте класс StringUtils с staticmethod под названием is_palindrome, который принимает строку и проверяет, является ли она палиндромом (читается одинаково слева направо и справа налево). Метод должен возвращать True, если строка является палиндромом, и False в противном случае.
        
# class StringUtils:
#     @staticmethod
#     def is_palindrome(string_: str):
#         if string_ == string_[::-1]:
#             return 'True'
#         else:
#             return 'False'
        
# a = StringUtils()
# print(a.is_palindrome('mom'))


# 4)Создайте класс Shape с staticmethod под названием get_circle_area, который принимает радиус и возвращает площадь круга. Площадь круга вычисляется по формуле πr^2, где π примерно равно 3.14159.
# from math import pi
# class Shape:
#     @staticmethod
#     def get_circle_area(radius):
#         s = pi * radius ** 2
#         return s

# s = Shape()
# print(s.get_circle_area(8))


# 5)Создайте класс FileUtils с classmethod под названием get_file_extension, который принимает имя файла в виде строки и возвращает его расширение. Если файл не имеет расширения, метод должен возвращать пустую строку. Например, для файла "document.txt" метод должен вернуть ".txt".

# class FileUtils:
#     @classmethod
#     def get_file_extension(cls,name_file: str):
#         if name_file[-4:] != '.txt':
#             return ''
#         else:
#             return name_file[-4:]
        
# f = FileUtils()
# print(f.get_file_extension('document.txt'))


# class OS:
#     def __init__(self, version):
#         self.version = version

# class Windows(OS):
#     def copy(self, text):
#         self.text = text
#         return f'скопирован текст {self.text} горячими клавишами CTRL + C'

# class MacOS(OS):
#     def copy(self, text):
#         self.text = text
#         return f'скопирован текст {self.text} горячими клавишами COMMAND + C'


# class Linux(OS):
#     def copy(self, text):
#         self.text = text
#         return f'скопирован текст {self.text} горячими клавишами CTRL + SHIFT + C'

# win = Windows('10')
# mac = MacOS('Big Sur')
# lin = Linux('Ubuntu')
# print(win.copy('Полиморфизм — одна из основных парадигм ООП'))
 
# print(mac.copy('Полиморфизм - разное поведение одного и того же метода в разных классах')) 
 
# print(lin.copy('На самом деле одинаковым является только имя метода, его исходный код зависит от класса'))

# class Language:
#     def __init__(self, level, type):
#         self.level = level
#         self.type = type

# class Python(Language):
#     def write_function(self, func_name, arg):
#         return f'def {func_name}({arg}):'

    
#     def create_variable(self, var_name, value):
#         if isinstance(value, str):
#             return f"{var_name} = '{value}'"

#         else:
#             return f"{var_name} = {value}"

# class JavaScript(Language):
#     def write_function(self, func_name, arg):
#         return f'function {func_name}({arg}) {{     }};'


#     def create_variable(self, var_name, value):
#         if isinstance(value, str):
#             return f"let {var_name} = '{value}';"

#         else:
#             return f"let {var_name} = {value};"

# py = Python('advanced', 'backend')
# js = JavaScript('advanced', 'frontend')
# print(py.write_function('get_code', 'a')) 
# print(py.create_variable('name', 'John'))
# print(js.write_function('validate', 'form')) 
# print(js.create_variable('password', 'john@123'))


# class Money:
#     def __init__(self, country, symbol):
#         self.country = country
#         self.symbol = symbol
    

# class Dollar(Money):
#     rate = 84.80
#     def exchange(self, amount):
#         return f'$ {amount} равен {Dollar.rate * amount} сомам'



# class Euro(Money):
#     rate = 98.40
#     def exchange(self, amount):
#         return f'€ {amount} равен {Euro.rate * amount} сомам'

# d = Dollar('USA', '$')
# e = Euro('Spain', '€')
# print(d.exchange(100))
# print(e.exchange(80))

# class Planet:
#     def __init__(self, orbit):
#         self.orbit = orbit

# class Mercury(Planet):
#     def get_age(self, earth_age):
#         return f'на Меркурии ваш возраст составляет {int(earth_age * 365 / self.orbit)} лет'

# class Venus(Planet):
#     def get_age(self, earth_age):
#         return f'на Венере ваш возраст составляет {round(earth_age * 365 / self.orbit * 365)} дней'

# class Jupiter(Planet):
#     def get_age(self, earth_age):
#         return f'на Юпитере ваш возраст составляет {round(earth_age * 365 // self.orbit * 365 * 24)} часов'

# mercury = Mercury(88) 
# venus = Venus(225) 
# jupiter = Jupiter(12) 
# print(venus.get_age(20)) 
# print(jupiter.get_age(20)) 
# print(mercury.get_age(20))


# import datetime 
# class Clock: 
#     def current_time(self): 
#         dt_new = datetime.datetime.today().strftime('%H:%M:%S') 
#         print(dt_new)
# class Alarm: 
#     def on(self):
#         print('8:00:00') 
#     def off(self):
#         print('9:00:00') 
        
# class AlarmClock(Clock, Alarm): 
#     def alarm_on(self): 
#         print('Будильник включён') 
# clock = AlarmClock() 
# clock.current_time() 
# clock.alarm_on()


# from abc import ABC, abstractmethod 
# class Coder(ABC): 
#     count_code_time = 0 
#     @abstractmethod 
#     def get_info(self): 
#         pass 
#     @abstractmethod 
#     def coding(self, hours): 
#         pass 
# class Backend(Coder): 
#     def __init__(self, experience, languages_backend): 
#         self.experience = experience 
#         self.languages_backend = languages_backend 
#     def get_info(self): 
#         return f"{self.languages_backend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование" 
#     def coding(self, hours): 
#         self.count_code_time += hours 
# class Frontend(Coder): 
#     def __init__(self, experience, languages_frontend): 
#         self.experience = experience 
#         self.languages_frontend = languages_frontend 
#     def get_info(self): 
#         return f"{self.languages_frontend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование" 
#     def coding(self, hours): 
#         self.count_code_time += hours 
# class Fullstack(Backend, Frontend): 
#     pass 
    
# a = Backend('Junior', 'Python') 
# b = Frontend('Middle', 'JavaScript') 
# c = Fullstack('Senior', 'Python and JS') 
# a.coding(12) 
# b.coding(45) 
# c.coding(17) 
# print(a.get_info()) 
# print(b.get_info()) 
# print(c.get_info())


# class Square:
#     def __init__(self, side):
#         self.side = side
#     def get_area(self):
#         return int(self.side * 2)


# class Triangle:
#     def __init__(self, height, base):
#         self.height = height
#         self.base = base

#     def get_area(self):
#         return int(self.base * self.height * 2)
    
# class Pyramid(Square, Triangle):
#     def __init__(self, height, base):
#         super().__init__(height, base)

#     def get_volume(self):
#         return int(1/3*self.base**2*self.height) 
    
# obj = Square(3) 
# print(obj.get_area()) 
# obj2 = Triangle(3,5) 
# print(obj2.get_area()) 
# obj3 = Pyramid(10,10) 
# print(obj3.get_volume())


# class Square: 
#     def __init__(self, side) -> None: 
#         self.side = side 
#     def get_area(self): 
#         return self.side * self.side 
# class Triangle: 
#     def __init__(self, height, base) -> None: 
#         self.height = height 
#         self.base = base 
#     def get_area(self): 
#         return int(0.5*self.base*self.height) 
# class Pyramid(Triangle, Square): 
#     def __init__(self, height, base) -> None: 
#         super().__init__(height, base) 
#     def get_volume(self): 
#         return int(1/3*self.base**2*self.height) 
    
# obj = Square(3) 
# print(obj.get_area()) 
# obj2 = Triangle(3,5) 
# print(obj2.get_area()) 
# obj3 = Pyramid(10,10) 
# print(obj3.get_volume())

# class ExtensionMixin: 
#     def add_extension(self, extension_name): 
#         self.extensions.append(extension_name) 
#         return f'Добавлено новое расширение {extension_name} для игры {self.name}.' 
#     def remove_extension(self, extension_name): 
#         if extension_name in self.extensions: 
#             self.extensions.remove(extension_name) 
#             return f'{extension_name} был отключен от {self.name}.' 
#         else: 
#             return 'Такого расширения нет в списке.' 
# class Game(ExtensionMixin): 
#     def __init__(self, game_type, name): 
#         self.type = game_type 
#         self.name = name 
#         self.extensions = [] 
#     def get_description(self, description): 
#         return f"{self.name} это {description}." 
#     def get_extensions(self): 
#         if len(self.extensions) == 0: 
#             return "Нет подключенных расширений" 
#         else: return self.extensions 
# game = Game('CS_GO', 'Minencraft') 
# print(game.get_description('инди-игра в жанре песочницы с элементами выживания и открытым миром')) 
# print(game.add_extension('Multiverse-Core')) 
# print(game.add_extension('Multiverse-Core1')) 
# game.extensions 
# print(game.get_extensions()) 
# print(game.remove_extension('Multiverse-Core')) 
# print(game.get_extensions())

# class FlyMixin: 
#     def fly(self): 
#         print('я могу летать') 
# class WalkMixin: 
#     def walk(self): 
#         print('я могу ходить') 
# class SwimMixin: 
#     def swim(self): 
#         print('я могу плавать') 
# class Human(WalkMixin, SwimMixin): 
#     name = 'человек' 
#     def talk(self): 
#         print('я могу говорить') 
# class Fish(SwimMixin): 
#     name = 'рыба' 
# class Exocoetidae(SwimMixin, FlyMixin): 
#     name = 'летучая рыба' 
# class Duck(SwimMixin, WalkMixin, FlyMixin): 
#     name = 'утка'
# man = Human() 
# man.swim() 
# man.walk() 
# fish = Fish() 
# fish.swim() 
# dragon = Exocoetidae() 
# dragon.swim() 
# dragon.fly() 
# duck = Duck() 
# duck.swim() 
# duck.fly() 
# duck.walk()



# class Car:
#   def __init__(self, speed):
#     self.__speed = speed

#   def set_speed(self, new_speed):
#     self.__speed = new_speed
    
#   def show_speed(self):
#     return self.__speed

# a = Car(23)
# a.set_speed(24)
# print(a.show_speed())


# class Car:
#   def __init__(self, speed):
#     self.__speed = speed

#   @property
#   def speed(self):
#     return self.__speed

#   @speed.setter
#   def speed(self, new_speed):
#     self.__speed = new_speed

# car = Car(100)
# car.speed = 120
# print(car.speed)

# class MyNumber(int):
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other: int):
#         return f'Это сложение и результат равен: {self.value + other}'
    
#     def __sub__(self, other: int):
#         return f'Это вычитание и результат равен: {self.value - other}'
    
#     def __mul__(self, other: int):
#         return f'Это умножение и результат равен: {self.value * other}'
        
#     def __truediv__(self, other: int):
#         return f'Это деление и результат равен: {self.value / other}'


# obj = MyNumber(10)
# print(obj + 2)
# print(obj - 2)
# print(obj * 2)
# print(obj / 2)


# class MyList(list):
#     def __init__(self, list_):
#         self.list_ = list_

#     def __getitem__(self, index):
#         return (self.list_[index - 1])

# obj_list = MyList([1,2,3,4,5])  
# print(obj_list[1])



# class DateUtils:
#     @classmethod
#     def is_valid_date(cls, data: str):
#         from datetime import datetime
#         a = datetime.now().strftime('%Y-%m-%d')
#         if a == data:
#             return 'True'
#         else:
#             return 'False'

# a = DateUtils()
# print(a.is_valid_date('2023-07-24'))