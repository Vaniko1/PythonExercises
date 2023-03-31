# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# სავარჯიშო 1
# class Cat:
#     def eat(self):
#         print('Cat eats a milk')
#
#     def talk(self):
#         print('Cat sats miaww')
#
#     def walk(self):
#         print('Cat can run 20km/h')
#
#
# class Dog:
#     def eat(self):
#         print('Dog eats a bone')
#
#     def talk(self):
#         print('Dog sats Aww')
#
#     def walk(self):
#         print('Dog can run 40km/h')
#
#
# def methods(obj):
#     obj.eat()
#     obj.talk()
#     obj.walk()
#
#
# C1 = Cat()
# methods(C1)
#
# print('')
#
# D1 = Dog()
# methods(D1)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# სავარჯიშო 2
# class Currency:
#     valuta = {'USD': 2.7, 'EUR': 3}
#
#     def __init__(self, value, unit='GEL'):
#         self.value = value
#         self.unit = unit
#
#     def __str__(self):
#         return f'{float(self.value)} {self.unit}'
#
#     def changeTo(self, unit_):
#         if unit_ == 'USD':
#             print(f"{float(self.value) / self.valuta['USD']} {self.unit}")
#             result = self.value / self.valuta['USD']
#             return Currency(result, unit_)
#         elif unit_ == 'EUR':
#             print(f"{float(self.value) / self.valuta['EUR']} {self.unit}")
#             result = self.value / self.valuta['EUR']
#             return Currency(result, unit_)
#         elif unit_ == 'GEL':
#             return Currency(self.value, unit_)
#
#     def __add__(self, other):
#         if self.unit == other.unit:
#             return f'{float(self.value + other.value)} {self.unit}'
#         elif other.unit != self.unit:
#             if self.unit == 'USD':
#                 if other.unit == 'EUR':
#                     return f'{self.value + other.value * 1.09} {self.unit}'
#                 elif other.unit == 'GEL':
#                     return f'{self.value + other.value * 0.39} {self.unit}'
#             elif self.unit == 'EUR':
#                 if other.unit == 'USD':
#                     return f'{self.value + other.value * 0.92} {self.unit}'
#                 elif other.unit == 'GEL':
#                     return f'{self.value + other.value * 0.36} {self.unit}'
#             elif self.unit == 'GEL':
#                 if other.unit == 'USD':
#                     return f'{self.value + other.value * 2.55} {self.unit}'
#                 elif other.unit == 'EUR':
#                     return f'{self.value + other.value * 2.78} {self.unit}'
#
#     def __radd__(self, other):
#         if isinstance(other, int) or isinstance(other, float):
#             return self.value * other
#         else:
#             return TypeError('გამრავლების ოპერაცია უნდა შესრულდეს მხოლოდ მთელ ან ათწილად რიცხვზე')
#
#     def __mul__(self, other):
#         if isinstance(other, int) or isinstance(other, float):
#             return self.value * other
#         else:
#             return TypeError('გამრავლების ოპერაცია უნდა შესრულდეს მხოლოდ მთელ ან ათწილად რიცხვზე')
#
#     def __rmul__(self, other):
#         if isinstance(other, int) or isinstance(other, float):
#             return self.value * other
#         else:
#             return TypeError('გამრავლების ოპერაცია უნდა შესრულდეს მხოლოდ მთელ ან ათწილად რიცხვზე')
#
#     def __gt__(self, other):
#         if self.value > other.changeTo(self.unit).value:
#             return True
#         else:
#             return False
#
#
# C1 = Currency(400)
# print('C1 =', C1.__str__())
#
# C2 = Currency(300, 'GEL')
# print('C2 =', C2.__str__())
#
#
# C3 = Currency(300, 'USD')
# print('C3 =', C3.__str__())
#
# print(C1 > C3)


# print('C2 + C3 =', C2 + C3)
#
# print('100 + C3 =', 100 + C3)
#
# print('C2 * 2 =', C2 * 2)
#
# print('2 * C2 =', 2 * C2)
