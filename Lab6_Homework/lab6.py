import math
from abc import ABC, abstractmethod

# Exercițiul 1

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c):
        self.a = side_a
        self.b = side_b
        self.c = side_c

    def calculate_perimeter(self):
        return self.a + self.b + self.c

    def calculate_area(self):
        s = self.calculate_perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

print("--- Exercițiul 1 ---")
c = Circle(5)
r = Rectangle(4, 6)
t = Triangle(3, 4, 5)
print(f"Circle Area: {c.calculate_area():.2f}, Perimeter: {c.calculate_perimeter():.2f}")
print(f"Rectangle Area: {r.calculate_area()}, Perimeter: {r.calculate_perimeter()}")
print(f"Triangle Area: {t.calculate_area()}, Perimeter: {t.calculate_perimeter()}")
print("\n" + "="*30 + "\n")


# Exercițiul 2

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New Balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New Balance: ${self.balance}")
        else:
            print("Insufficient funds.")

class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest applied: ${interest:.2f}. New Balance: ${self.balance:.2f}")

class CheckingAccount(Account):
    def __init__(self, owner, balance=0, overdraft_limit=100):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew ${amount} (Checking). New Balance: ${self.balance}")
        else:
            print("Transaction declined: Overdraft limit exceeded.")

print("--- Exercițiul 2 ---")
sav_acc = SavingsAccount("Ion Popescu", 1000)
sav_acc.deposit(500)
sav_acc.apply_interest()
chk_acc = CheckingAccount("Maria Ionescu", 200)
chk_acc.withdraw(250)
print("\n" + "="*30 + "\n")


# Exercițiul 3

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def calculate_mileage(self, miles, gallons):
        if gallons > 0:
            return f"MPG: {miles / gallons:.1f}"
        return "Cannot calculate mileage with zero gallons."

class Motorcycle(Vehicle):
    def pop_wheelie(self):
        return f"The {self.model} is popping a wheelie!"

class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity_lbs):
        super().__init__(make, model, year)
        self.towing_capacity_lbs = towing_capacity_lbs

    def get_towing_capacity(self):
        return f"Towing Capacity: {self.towing_capacity_lbs} lbs"

print("--- Exercițiul 3 ---")
my_car = Car("Toyota", "Camry", 2022)
print(my_car.display_info())
print(my_car.calculate_mileage(300, 10))
my_truck = Truck("Ford", "F-150", 2023, 13000)
print(my_truck.display_info())
print(my_truck.get_towing_capacity())
print("\n" + "="*30 + "\n")


# Exercițiul 4

class Employee:
    def __init__(self, name, id_number, base_salary):
        self.name = name
        self.id_number = id_number
        self.base_salary = base_salary

    def calculate_pay(self):
        return self.base_salary

    def get_role_description(self):
        return "General Employee"

class Manager(Employee):
    def __init__(self, name, id_number, base_salary, bonus):
        super().__init__(name, id_number, base_salary)
        self.bonus = bonus

    def calculate_pay(self):
        return self.base_salary + self.bonus

    def conduct_meeting(self):
        return f"Manager {self.name} is conducting a meeting."
    
    def get_role_description(self):
        return "Manager"

class Engineer(Employee):
    def write_code(self):
        return f"Engineer {self.name} is writing code."

    def get_role_description(self):
        return "Engineer"

class Salesperson(Employee):
    def __init__(self, name, id_number, base_salary, commission):
        super().__init__(name, id_number, base_salary)
        self.commission = commission

    def calculate_pay(self):
        return self.base_salary + self.commission

    def get_role_description(self):
        return "Salesperson"

print("--- Exercițiul 4 ---")
mgr = Manager("Alice", "M01", 80000, 15000)
eng = Engineer("Bob", "E01", 70000)
print(f"{mgr.get_role_description()} {mgr.name} Pay: ${mgr.calculate_pay()}")
print(eng.write_code())
print("\n" + "="*30 + "\n")


# Exercițiul 5

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "Some generic animal sound"

class Mammal(Animal):
    def __init__(self, name, species, fur_color):
        super().__init__(name, species)
        self.fur_color = fur_color

    def give_birth(self):
        return f"{self.name} the {self.species} is giving birth to live young."

class Bird(Animal):
    def __init__(self, name, species, wing_span):
        super().__init__(name, species)
        self.wing_span = wing_span

    def fly(self):
        return f"{self.name} the {self.species} is flying with a {self.wing_span} wingspan."

    def make_sound(self):
        return "Chirp/Tweet"

class Fish(Animal):
    def __init__(self, name, species, water_type):
        super().__init__(name, species)
        self.water_type = water_type

    def swim(self):
        return f"{self.name} is swimming in {self.water_type}."

print("--- Exercițiul 5 ---")
lion = Mammal("Leo", "Lion", "Golden")
eagle = Bird("Eddie", "Eagle", "6ft")
clownfish = Fish("Nemo", "Clownfish", "saltwater")
print(lion.give_birth())
print(eagle.fly())
print(eagle.make_sound())
print(clownfish.swim())
print("\n" + "="*30 + "\n")


# Exercițiul 6

class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"'{self.title}' has been checked out.")
        else:
            print(f"'{self.title}' is already checked out.")

    def return_item(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' was not checked out.")

    def display_info(self):
        status = "Checked Out" if self.is_checked_out else "Available"
        return f"[ID: {self.item_id}] {self.title} - Status: {status}"

class Book(LibraryItem):
    def __init__(self, title, item_id, author, isbn):
        super().__init__(title, item_id)
        self.author = author
        self.isbn = isbn

    def display_info(self):
        return f"{super().display_info()} (Book by {self.author}, ISBN: {self.isbn})"

class DVD(LibraryItem):
    def __init__(self, title, item_id, director, duration_min):
        super().__init__(title, item_id)
        self.director = director
        self.duration = duration_min

    def display_info(self):
        return f"{super().display_info()} (DVD directed by {self.director}, {self.duration} mins)"

class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_number, publication_date):
        super().__init__(title, item_id)
        self.issue_number = issue_number
        self.publication_date = publication_date

    def display_info(self):
        return f"{super().display_info()} (Magazine Issue #{self.issue_number}, Date: {self.publication_date})"

print("--- Exercițiul 6 ---")
book = Book("The Great Gatsby", "B101", "F. Scott Fitzgerald", "978-0743273565")
dvd = DVD("Inception", "D202", "Christopher Nolan", 148)

print(book.display_info())
book.check_out()
print(book.display_info())
book.return_item()
print(book.display_info())
print("\n" + "="*30 + "\n")
