# task 2
class Car:
    def __init__(self, colour, model, make_year, fuel_type, price):
        self.colour = colour
        self.model = model
        self.make_year = make_year
        self.fuel_type = fuel_type
        self.price = price

    def sell(self):
        return 'sell your car on {} $'.format(self.price)

    def buy(self):
        return 'buy a car on {} dollar'.format(self.price)

    def rent(self):
        return 'rent a car on ' + str(int(self.price * 10 / 100)) + ' $'

    def __str__(self):
        return f'colour: {self.colour} ,model: {self.model}, make year: {self.make_year}, ' \
               f'fuel type: {self.fuel_type}, price: {self.price}'


Mercedes = Car('red', 'mercedes', 2015, 'gas', 30000)
print(Mercedes.buy())
print(Mercedes.rent())

BMW = Car('blue', 'mercedes', 2013, 'gas', 27000)
Audi = Car('orange', 'audi', 2009, 'diesel', 20000)


# task 3
class Dog:
    def __init__(self, breed, size, age, colour):
        self.breed = breed
        self.size = size
        self.age = age
        self.colour = colour

    def eat(self):
        return 'eat food'

    def run(self):
        return 'runs with four leg:))'


neapolitan_mastiff = Dog('Neapolitan Mastiff', 'large', '5 years', 'black')
maltese = Dog('Maltese', 'small', '2 years', 'white')
chow_chow = Dog('Chow Chow', 'medium', '3 years', 'brown')


# task 4
class Celsius:
    def __init__(self, __temperature):
        self.__temperature = __temperature

    def get_temp(self):
        return self.__temperature

    def set_temp(self, text):
        self.__temperature = text

    def del_temp(self):
        del self.__temperature

    temperature = property(get_temp, set_temp, del_temp)


obj1 = Celsius(20)
obj2 = Celsius(30)
print(obj2.temperature)
print(obj1.temperature)
obj1.temperature = 18
print(obj1.temperature)
del obj2.temperature


# task 5
class Bank_Account:
    def __init__(self, __account_name, __balance=0):
        self.__account_name = __account_name
        self.__balance = __balance

    def getter_account_name(self):
        return self.__account_name

    def setter_account_name(self, text):
        self.__account_name = text
        return self.__account_name

    def deposit(self):
        amount_of_money = int(input('how much money would you like to depose?:'))
        self.__balance += amount_of_money
        print("the deposit is done. now your balance is {} Gel".format(self.__balance))

    def withdraw(self):
        amount_of_money2 = int(input('how much money would you like to withdraw?:'))
        if self.__balance >= amount_of_money2:
            self.__balance -= amount_of_money2
            print("withdrawal is done. now your balance  {} Gel".format(self.__balance))
        else:
            print('you don\'t have enough money on your balance:(')


balance = int(input('what is your balance now?:'))
user = Bank_Account('irinka datoshvili', balance)
operation = input(f'which operation would you like? deposit: {1}, withdraw: {2} :')

if operation == '1':
    user.deposit()

elif operation == '2':
    user.withdraw()


# task 6 Fraction class
class Fraction:
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom

    def __str__(self):
        return f'{self.top} / {self.bottom}'

    def __add__(self, other):
        n_top = self.top * other.bottom + other.top * self.bottom
        n_bottom = self.bottom * other.bottom
        return Fraction(n_top, n_bottom)

    def inverse(self):
        return Fraction(self.bottom, self.top)


fraction1 = Fraction(2, 3)
fraction2 = Fraction(3, 6)
fraction3 = fraction1 + fraction2
print(fraction3)
print(fraction1)

# task 7 find the distance between center of coordinate to any point
from math import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length_from_center_to_point(self):
        return sqrt(self.x ** 2 + self.y ** 2)


center = Point(0, 0)
point1 = Point(3, 5)
point2 = Point(6, 9)
print(point1.length_from_center_to_point())


# task 8
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def length_between_points(self, other):
        length = sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)
        return length


x = int(input('enter the x coordinate:'))
y = int(input('enter the y coordinate:'))
a = Point(x, y)

x1 = int(input('enter the x2 coordinate:'))
y1 = int(input('enter the y2 coordinate:'))
b = Point(x, y)
print(a)
print(a.length_between_points(b))
