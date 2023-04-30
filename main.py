# class Ticket:
#     def __init__(self, movieName, price, quantity, language='Geo'):
#         self.movieName = movieName
#         self.price = price
#         self.quantity = quantity
#         self.language = language
#
#     def __str__(self):
#         return f'ფილმის დასახელებაა {self.movieName}, ამ ფილმის ბილეთების რაოდენობა არის {self.quantity}, ხოლო თითო ბილეთის ფასია: {self.price}'
#
#     def __gt__(self, other):
#         if isinstance(other, Ticket):
#             return self.quantity > other.quantity
#         else:
#             return self.quantity > other.quantity
#
#
# class User:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#
#     def __str__(self):
#         return f'მყიდველის სახელია {self.name}, მყიდველის ბალანსი: {self.balance}'
#
#     def purchaseTicket(self, ticket, ticketQunatity):
#         self.ticket = ticket
#         self.ticketQunatity = ticketQunatity
#
#         if ticketQunatity * ticket.price <= self.balance and ticket.quantity >= ticketQunatity:
#             self.balance = self.balance - ticketQunatity * ticket.price
#             ticket.quantity = ticket.quantity - ticketQunatity
#             print(f'თქვენ შეისყიდეთ {ticketQunatity} ბილეთი')
#         elif ticketQunatity * ticket.price > self.balance:
#             print('თქვენ არ გაქვთ საკმარისი თანხა ბილეთების შესაძენად')
#         elif ticket.quantity < ticketQunatity:
#             print('საკმარისი ბილეთი არ აქვს კინოთეატრს')
#
#     def deposit(self, money):
#         self.money = money
#
#         self.balance = self.balance + money
#         print(self.balance)
#
#
# T1 = Ticket('spider-man', 100, 1000)
# T2 = Ticket('batman', 100, 1000)
#
# userName = input('შეიყვანეთ თქვენი სახელი: ')
# userBalance = int(input('შეიყვანეთ თქვენი ბალანსი: '))
# U1 = User(userName, userBalance)
#
# ticket = int(input('შეიყვანეთ რამდენი ბილეთის შეძენა გსურთ: '))
# U1.purchaseTicket(T1, 3)
# print(U1.balance)
# U1.deposit(100)
#
# print(T1 > T2)
# print(T2 > T1)
#
# class Health:
#     def __init__(self, age, sex, pulse):
#         self.age = age
#         self.sex = sex
#         self.pulse = pulse
#
#     def __str__(self):
#         return f'პაციენტის ასაკი არის {self.age}, სქესი: {self.sex}, ხოლო პულსია {self.pulse}'
#
#     def avarageLife(self):
#         print(2600000000 / (self.pulse * 60 * 24 * 365))
#
#     def maxPulse(self):
#
#         if self.sex == 'Male':
#             MAX_beats = 223 - 0.9 * self.age
#             print(MAX_beats)
#         elif self.sex == 'Female':
#             MAX_beats = 226 - 0.9 * self.age
#             print(MAX_beats)
#
#     def workoutMaxBeat(self, factor):
#         self.factor = factor
#
#         if self.sex == 'Male':
#             MAX_beats = 223 - 0.9 * self.age
#         elif self.sex == 'Female':
#             MAX_beats = 226 - 0.9 * self.age
#
#         NOR_beats = self.pulse
#
#         MAX_workout_pulse = (MAX_beats - NOR_beats)* factor + NOR_beats
#
#         print(MAX_workout_pulse)
#
#
# H1 = Health(20, 'Female', 100)
# print(H1)
#
# H1.maxPulse()
#
# H1.avarageLife()
#
# H1.workoutMaxBeat(0.8)


# class Bus:
#     def __init__(self, number, price, capacity, passengerInfo=[]):
#         self.number = number
#         self.price = price
#         self.capacity = capacity
#         self.passengerInfo = passengerInfo
#
#     def __str__(self):
#         return f"""ავტობუსის ნომერია: {self.number}, მისი ღირებულებაა {self.price},მასში ეტევა {self.capacity} ადამიანი. ამ ავტობუსში მგზავრების ინფორმაცია კი ასეთა: {self.passengerInfo}.
#         """
#
#
# class PassengerCard:
#     def __init__(self, ID, passengerName, balance, history=[]):
#         self.ID = ID
#         self.passengerName = passengerName
#         self.balance = balance
#         self.history = history
#
#     def __str__(self):
#         return f'მგზავრის სატრანსპორტო ბარათის ID არის {self.ID}, მგზავრის სახელია: {self.passengerName}, ბარათის ბალანსია {self.balance}, ხოლო ბარათის ისტორიაა: {self.history}'
#
#     def buyTicket(self, bus):
#         self.bus = bus
#
#         if bus.number in self.history:
#             print(f'თქვენ უკვე აღებული გაქვთ ამ ავტობუსზე ბილეთი')
#         else:
#             if self.balance >= bus.price:
#                 self.balance -= bus.price
#                 self.history.append(bus.number)
#                 bus.passengerInfo.append(self.ID)
#                 print(f'თქვენ წარმატებით შეიძინეთ ბილეთი')
#             else:
#                 print(f'თქვენ არ გაქვთ საკმარისი თანხა ბილეთს შესაძენათ')
#
#
# B1 = Bus(20, 10, 50)
#
# PC1 = PassengerCard(1234, 'Luka', 10)
#
# print('B1 str:', B1)
# print('PC1 str:', PC1)
#
# PC1.buyTicket(B1)
#
# print('B1 str:', B1)
# print('PC1 str:', PC1)


class Vaccine:
    def __init__(self, name, amount, minAge, dose, country):
        self.name = name
        self.amount = amount
        self.minAge = minAge
        self.dose = dose
        self.country = country

    def __str__(self):
        return f'ვაქცინის სახელწოდებაა {self.name}, მისი რაოდენობაა: {self.amount}, ვაქცინის გაკეთება დაშვებულია {self.minAge} წლიდან, ვაქცინის დოზა: {self.dose}, ეს ვაქცინა არის {self.country}-დან.'


class Citizen:
    def __init__(self, ID, name, age, vaccineType=None, vaccineAmount=0):
        self.ID = ID
        self.name = name
        self.age = age
        self.vaccineType = vaccineType
        self.vaccineAmount = vaccineAmount

    def __str__(self):
        if self.vaccineType == None:
            return f'მოქალაქის პირადი ნომერია: {self.ID}, მოქალაქის სახელია {self.name}, ხოლო ასაკი: {self.age} წელი, ვაქცინირებულია {self.vaccineAmount}-ჯერ.'
        else:
            return f'მოქალაქის პირადი ნომერია: {self.ID}, მოქალაქის სახელია {self.name}, ხოლო ასაკი: {self.age} წელი, ვაქცინირებულია {self.vaccineType}-ით, {self.vaccineAmount}-ჯერ.'

    def getVaccinated(self, vaccine):
        self.vaccine = vaccine

        if self.age >= vaccine.minAge and vaccine.amount > 0:
            self.vaccineType = vaccine.name
            if vaccine.dose > self.vaccineAmount:
                print('თქვენ წარმატებით გაიკეთეთ ვაქცინა')
                self.vaccineAmount += 1
                vaccine.amount -= 1
            else:
                print('შენ უკვე გაკეთბული გაქვს ეს ვაქცინა')


V1 = Vaccine('Pfizer', 10, 18, 1, 'Georgia')
print(V1)

C1 = Citizen(1234, 'Luka', 25)
print(C1)

C1.getVaccinated(V1)
