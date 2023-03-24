# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# სავარჯიშო - 1
# class People:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#
#     def get_email(self):
#         return f'{self.firstname}.{self.lastname}.uni@btu.edu.ge'
#
# class Lecturer(People):
#     def __init__(self, firstname, lastname, salary):
#         super().__init__(firstname, lastname)
#         self.salary = salary
#
#     def get_email(self):
#         return f'{self.firstname}.{self.lastname}@btu.edu.ge'
#
# class Student(People):
#     def __init__(self, firstname, lastname, courses=['Information Technologies', 'Business']):
#         super().__init__(firstname, lastname)
#         self.courses = courses
#
#     def get_email(self):
#         return f'{self.firstname}.{self.lastname}.1@btu.edu.ge'
#
# P1 = People('Gela', 'Gelashvili')
# print('P1:', P1.get_email())
#
# L1 = Lecturer('John', 'Smith', '100')
# print('L1:', L1.get_email())
#
# S1 = Student('Vaniko', 'Nozadze', 'Information Technologies')
# print('S1:', S1.get_email())
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# სავარჯიშო - 2
#
# class LibraryItem:
#     def __init__(self, title, subject, status):
#         self.title = title
#         self.subject = subject
#         self.status = status
#
#     def booking(self):
#         if self.status == 'Available'.lower():
#             return f'You booked an item!'
#         elif self.status == 'Occupied'.lower():
#             return f'You can not book right now, please try it next time.'
#
# class Book(LibraryItem):
#     def __init__(self, ISBN, authors, title, subject, status):
#         super().__init__(title, subject, status)
#         self.ISBN = ISBN
#         self.authors = authors
#
#     def booking(self):
#         if self.status == 'Available'.lower():
#             return f'You booked a Book about {self.subject}!, Enjoy!'
#         elif self.status == 'Occupied'.lower():
#             return f'You can not book a book right now, please try it next time.'
#
#
# class Magazine(LibraryItem):
#     def __init__(self, journalName, volume, status):
#         self.journalName = journalName
#         self.volume = volume
#         self.status = status
#
#     def booking(self):
#         if self.status == 'Available'.lower():
#             return f'You booked a Magazine called {self.journalName}, have fun while reding it!'
#         elif self.status == 'Occupied'.lower():
#             return f'You can not book a book right now, please try it next time.'
#
#
# class CD(LibraryItem):
#     def __init__(self, title, status):
#         self.title = title
#         self.status = status
#
#     def booking(self):
#         return "You can't book a CD at library..."
#
#
#
# L1 = LibraryItem('Main', 'Math', 'occupied')
# print('L1 Status: ', L1.status)
# print('L1 Booking: ', L1.booking())
#
# print(' ')
#
# B1 = Book('ISBN', 'London', 'Legendary', 'Drama', 'available')
# print('B1 Status: ', B1.status)
# print('B1 Booking: ', B1.booking())
#
# print(' ')
#
# M1 = Magazine('Modern Fashion', 2, 'available')
# print('M1 Status: ', M1.status)
# print('M1 Booking: ', M1.booking())
#
# print(' ')
#
# CD1 = CD('Messi', 'occupied')
# print('CD1 Status: ', CD1.status)
# print('CD1 Booking: ', CD1.booking())
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# სავარჯიშო - 3
#
# class Contacts:
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone
#
#
# class MailSender:
#     def send_email(self):
#         return f'თქვენი მეილი გაიგზავნა ამ მისამართზე: giorgi.giorgadze@gmail.com'
#
#
# class Friend(Contacts, MailSender):
#     def __init__(self, name, phone, email):
#         super().__init__(name, phone)
#         self.email = email
#
#     def send_email(self):
#         return f'თქვენი მეილი გაიგზავნა ამ მისამართზე: {self.email}'
#
#
# class Family(Contacts, MailSender):
#     def __init__(self, name, email, phone, birthdate):
#         super().__init__(name, phone)
#         self.email = email
#         self.birthdate = birthdate
#
#     def send_email(self):
#         return f'თქვენი მეილი გაიგზავნა ამ მისამართზე: {self.email}'
#
#
# C1 = Contacts('Vaniko', 557123456)
# print('C1 name:', C1.name)
# print('C1 phone:', C1.phone)
#
# print(' ')
#
# Fr1 = Friend('Giorgi', 559975432, 'giorgi.giorgadze@gmail.com')
# print('Fr1 name:', Fr1.name)
# print('Fr1 phone:', Fr1.phone)
# print('Fr1 email:', Fr1.email)
# print(Fr1.send_email())
#
# print(' ')
#
# F1 = Family('Salome', 'Salome.elbaqidze@gmail.com', 599987543, '02/11/2001')
# print('F1 name:', F1.name)
# print('F1 name:', F1.email)
# print('F1 name:', F1.phone)
# print('F1 name:', F1.birthdate)
# print(F1.send_email())
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# სავარჯიშო - 4
#
# class People:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#
#     def get_email(self):
#         return f'{self.firstname}.{self.lastname}.uni@btu.edu.ge'
#
#
# class Lecturer(People):
#     def __init__(self, firstname, lastname, salary):
#         super().__init__(firstname, lastname)
#         self.salary = salary
#
#     def get_email(self):
#         return f'{self.firstname}.{self.lastname}@btu.edu.ge'
#
#
# class Student(People):
#     def __init__(self, firstname, lastname, courses):
#         super().__init__(firstname, lastname)
#         self.courses = courses
#
#     def get_email(self):
#         return f'{self.firstname}.{self.lastname}.1@btu.edu.ge'
#
#
# class Doctoral_student(Lecturer, Student):
#     def __init__(self, firstname, lastname, salary, courses):
#         # Lecturer.__init__(self, firstname, lastname, salary)
#         self.firstname = firstname
#         self.lastname = lastname
#         self.salary = salary
#         self.courses = courses
#
#     def get_email(self):
#         return f'{self.firstname}.{self.lastname}.1@btu.edu.ge'
#
#
# P1 = People('Gela', 'Gelashvili')
# print('P1:', P1.get_email())
#
# L1 = Lecturer('John', 'Smith', '100')
# print('L1:', L1.get_email())
#
# S1 = Student('Vaniko', 'Nozadze', 'Information Technologies')
# print('S1:', S1.get_email())
#
# D1 = Doctoral_student('Jane', 'Jonas', '1000', 'Business')
# print('D1:', D1.get_email())
# print(getattr(D1, 'firstname'))

