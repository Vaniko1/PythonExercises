# # # # # # # # # # # # # # # # # # # # # #
# სავარჯიშო - 1 (მარტივი)
# class Rectangle:
#
#     def __init__(self, width, length, color):
#         self.width = width
#         self.length = length
#         self.color = color
#
#     def area(self):
#         return self.width * self.length
#
#     def perimeter(self):
#         return 2*(self.width + self.length)
#
#
# obj1 = Rectangle(1, 2, 'green')
# print(obj1.area())
# print(obj1.perimeter())
#
# class Car:
#
#     def __init__(self, color, model, makeYear, fuelType, price):
#         self.color = color
#         self.model = model
#         self.makeYear = makeYear
#         self.fuelType = fuelType
#         self.price = price
#
#
#     def sell(self):
#         return f'You sold this car for {self.price} dollars'
# # # # # # # # # # # # # # # # # # # # # #
# სავარჯიშო - 2 (მარტივი)
# car1 = Car('red', 'Mercedes', 2015, 'Gas', 10000)
# print(car1.color)
# print(car1.model)
# print(car1.makeYear)
# print(car1.fuelType)
# print(car1.price)
# print(car1.sell())
#
# car2 = Car('blue', 'BMW', 2013, 'Gas', 20000)
# print(car2.color)
# print(car2.model)
# print(car2.makeYear)
# print(car2.fuelType)
# print(car2.price)
#
#
# car3 = Car('orange', 'Audi', 2009, 'Diesel', 30000)
# print(car3.color)
# print(car3.model)
# print(car3.makeYear)
# print(car3.fuelType)
# print(car3.price)
#
# # # # # # # # # # # # # # # # # # # # # #
# სავარჯიშო - 3 (მარტივი)
#
# class Dog:
#     def __init__(self, Breed, Size, Age, Color):
#         self.Breed = Breed
#         self.Size = Size
#         self.Age = Age
#         self.Color = Color
#
#     def eat(self):
#         return f"It's eating time Maki! lets eat your food, which is for {self.Size} Dogs."
#
#     def Sleep(self):
#         return f"Let's go to sleep and after that I'll let you play with other {self.Breed} Dogs."
#
#     def Sit(self):
#         return f"Sit! I said Sit! Why won't do it I've been trying to teach you this command for {self.Age}."
#
#     def Run(self):
#         return f"3, 2, 1... RUN! I said run you {self.Color} Pig!"
#
# print("Dog 1")
# print(" ")
#
# dog1 = Dog('Neapolitan Mastiff', 'Large', '5 years', 'Black')
# print("-", dog1.eat())
# print("-", dog1.Sleep())
# print("-", dog1.Sit())
# print("-", dog1.Run())
#
# print(" ")
# print("Dog 2")
# print(" ")
#
# dog2 = Dog('Maltese', 'Small', '2 years', 'White')
# print("-", dog2.eat())
# print("-", dog2.Sleep())
# print("-", dog2.Sit())
# print("-", dog2.Run())
#
# print(" ")
# print("Dog 3")
# print(" ")
#
# dog1 = Dog('Chow Chow', 'Midium', '3 years', 'Brown')
# print("-", dog1.eat())
# print("-", dog1.Sleep())
# print("-", dog1.Sit())
# print("-", dog1.Run())
# # # # # # # # # # # # # # # # # # # # # #
# სავარჯიშო - 4 (მარტივი)
#
# class Celsius:
#     def __init__(self, __temperature):
#         self.__temperature = __temperature
#
#     def get_temp(self):
#         return self.__temperature
#
#     def set_temp(self, t):
#         self.__temperature = t
#
#     def del_temp(self):
#         del self.__temperature
#
#
#     temp = property(get_temp, set_temp, del_temp)
#
#
# c1 = Celsius(10)
# print(c1.get_temp())
# c1.set_temp(20)
# print(c1.get_temp())
# print(c1.temp)
#
# c2 = Celsius(50)
# print(c2.get_temp())
# c2.temp = 30
# print(c2.get_temp())
# print(c2.temp)
# # # # # # # # # # # # # # # # # # # # # #
# სავარჯიშო - 4 ბანკინგის (საშუალო სირთულის)
#
# class Bank_Account:
#     def __init__(self, account_name, balance=100):
#         self.__account_name = account_name
#         self.__balance = balance
#
#     def account_name_getter(self):
#         return self.__account_name
#
#     def account_name_setter(self, text):
#         self.__account_name = text
#
#     def deposit(self, money):
#         self.__balance = self.__balance + money
#         return f'თანხის შეტანა შესრულებულია. ამჟამად თქვენ ანგარიშზე გაქვთ {self.__balance} ლარი'
#
#     def withdraw(self, money):
#         self.__balance = self.__balance - money
#         return f'თანხის გამოტანა შერულებულია. ამჟამად თქვენ ანგარიშზე გაქვთ {self.__balance} ლარი'
#
# name_surname = input('შეიტანეთ კლიენტის სახელი და გვარი: ')
# user1 = Bank_Account(name_surname)
#
# print("თანხის შეტანა: 1, თანხის გამოტანა: 2")
# user_code = input(f"""შეიტანეთ შესაბამისი კოდი რომელი ოპერაციის შესრულებაც გსურთ: """)
# if user_code == '1':
#     requested_money = int(input('რა თანხის შეტანა გსურთ? '))
#     print(user1.deposit(requested_money))
# elif user_code == '2':
#     requested_money = int(input('რა თანხის გამოტანა გსურთ? '))
#     print(user1.withdraw(requested_money))
# # # # # # # # # # # # # # # # # # # # #
# სავარჯიშო - 5 (საშუალო სირთულის)
#
# class Fraction:
#     def __init__(self, top, bottom):
#         self.top = top
#         self.bottom = bottom
#
#     def __str__(self):
#         return f"{self.top}/{self.bottom}"
#
#     def summary(self, other):
#         if self.bottom == other.bottom:
#             return (self.top + other.top) / self.bottom
#         else:
#             same_bottom = self.bottom * other.bottom
#             answer = (((same_bottom / self.bottom) * self.top) + ((same_bottom / other.bottom) * other.top)) / same_bottom
#             return answer
#
#     def inverse(self):
#         return f'{self.bottom}/{self.top}'
#
# fra1 = Fraction(1, 2)
# fra2 = Fraction(5, 10)
# print(fra1.__str__())
# print(fra2.__str__())
# print(fra1.summary(fra2))
# print(fra1.inverse())
# # # # # # # # # # # # # # # # # # # # #
# სავარჯიშო - 6 (საშუალო სირთულის)
# import math
#
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def length(self):
#         return math.sqrt(((self.x)**2 + (self.y)**2))
#
# point1 = Point(3, 5)
# point2 = Point(6, 9)
# print(point1.length())
# # # # # # # # # # # # # # # # # # # # #
# სავარჯიშო 6 - (რთული)
# import math
#
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x},{self.y})"
#
#     def length(self, other):
#         return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
#
# x1 = int(input(f'შეიყვანეთ თქვენთვის სასურველი x წერტილი: '))
# y1 = int(input(f'შეიყვანეთ თქვენთვის სასურველი y წერტილი: '))
# a = Point(x1, y1)
# print('a = ', a.__str__())
# x2 = int(input(f'შეიყვანეთ თქვენთვის სასურველი x წერტილი: '))
# y2 = int(input(f'შეიყვანეთ თქვენთვის სასურველი y წერტილი: '))
# b = Point(x2, y2)
# print('b = ', b.__str__())
# print('მანძილი წერტილებს შორის არის: ', a.length(b))