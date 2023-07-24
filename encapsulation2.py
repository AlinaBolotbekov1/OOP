# class Car:
#     def __init__(self, model):
#         self.__model = model

#     model = property(lambda self: self.__model)

#     @property
#     def model(self):
#         return self.__model

# bmw = Car('BMW')
# print(bmw.model)

# ВАРИАНТ 1
# class Circle:
#     def __init__(self, radius):
#         self.__radius = radius

#     def get_radius(self):
#         print('getter')
#         return self.__radius
    
#     def set_radius(self, new_radius):
#         print('setter')
#         if not isinstance(new_radius, (int, float)):
#             raise ValueError('Invalid radius')
#         self.__radius = new_radius

#     def delete_radius(self):
#         print('deleter')
#         del self.__radius


#     radius = property(get_radius, set_radius, delete_radius)

# circle = Circle(10)
# # circle.radius = 4
# # print(circle.radius)
# del circle.radius
# print(circle.radius)


# ВАРИАНТ 2
# class Circle:
#     def __init__(self, radius):
#         self.__radius = radius

#     @property
#     def radius(self):
#         print('getter')
#         return self.__radius
    

#     @radius.setter
#     def radius(self, new_radius):
#         print('setter')
#         if not isinstance(new_radius, (int, float)):
#             raise ValueError('Invalid radius')
#         self.__radius = new_radius


#     @radius.deleter
#     def radius(self):
#         print('deleter')
#         del self.__radius

# circle = Circle(10)
# circle.radius = 4
# print(circle.radius)
# del circle.radius
# print(circle.radius)

# /-\ /\ |/| |-| /-\        


# class PrivateProject:
#     __github_link = 'https://github.com/AlinaBolotbekov1/hackaton'
#     __developers = ['Alice','John', 'Ryan']

#     def __init__(self, username):
#         self.username = username
        

#     @property
#     def link(self):
#         if self.username in self.__developers:
#             print(self.__github_link)
#         else:
#             print('Forbidden')



# a = PrivateProject('Alice')
# # a.link


# class User:

#     def _create_user(self, email, password):
#         self.email = email
#         self.__password = password

#     def create_user(self, email, password):
#         self.is_superuser = False
#         self._create_user(email, password)

#     def create_superuser(self, email, password):
#         self.is_superuser = True
#         self._create_user(email, password)

#     def admin_login(self, password):
#         if self.is_superuser == True:
#             if password != self.__password:
#                 raise Exception('Invalid password')
#             print('Successfully logged in')
#         else:
#             print('Forbidden')

# user1 = User()
# user1.create_user('aaa@gmail.com', '1234')
# user2 = User()
# user2.create_superuser('admin@gmail.com', 1)
# # user1.admin_login('1234')
# user2.admin_login(1)