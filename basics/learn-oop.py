"""
Object-Oriented Programming (OOP) in Python
===========================================

This file elaborates on the core concepts of OOP in Python:
1. Classes and Objects
2. The __init__ method
3. Inheritance
4. Encapsulation
5. Polymorphism
"""

# 1. Classes and Objects
# ----------------------
# A Class is a blueprint for creating objects.
# An Object is an instance of a class.

class Dog:
    # Class Attribute (Shared by all instances)
    species = "Canis familiaris"

    # The __init__ method is the initializer (constructor).
    # It is called when a new object is created.
    def __init__(self, name, age):
        # Instance Attributes (Unique to each instance)
        self.name = name
        self.age = age

    # Instance Method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another Instance Method
    def speak(self, sound):
        return f"{self.name} says {sound}"

# Creating Objects (Instances)
buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)

print("--- Classes and Objects ---")
print(buddy.description())  # Output: Buddy is 9 years old
print(miles.speak("Woof"))  # Output: Miles says Woof
print(f"Species: {buddy.species}") # Accessing class attribute


# 2. Inheritance
# --------------
# Inheritance allows a class (Child) to derive attributes and methods from another class (Parent).

class BullDog(Dog): # Inherits from Dog
    def speak(self, sound="Arf"): # Overriding the speak method
        return f"{self.name} says {sound} in a deep voice"

print("\n--- Inheritance ---")
jimbo = BullDog("Jimbo", 5)
print(jimbo.description()) # Uses parent's method
print(jimbo.speak())       # Uses child's overridden method


# 3. Encapsulation
# ----------------
# Encapsulation bundles data and methods that work on that data within one unit.
# It also restricts direct access to some of an object's components.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner       # Public attribute
        self._account_type = "Savings" # Protected attribute (convention only)
        self.__balance = balance # Private attribute (name mangled)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ")

    def get_balance(self): # Getter method to access private attribute
        return self.__balance

print("\n--- Encapsulation ---")
account = BankAccount("Alice", 1000)
account.deposit(500)
print(f"User: {account.owner}")
# print(account.__balance) # This would raise an AttributeError
print(f"Balance: ")


# 4. Polymorphism
# ---------------
# Polymorphism allows methods to do different things based on the object it is acting upon.

class Cat:
    def speak(self):
        return "Meow"

class Duck:
    def speak(self):
        return "Quack"

def animal_sound(animal):
    print(animal.speak())

print("\n--- Polymorphism ---")
my_dog = Dog("Rex", 2)
my_cat = Cat()
my_duck = Duck()

# The same function treats different objects differently based on their speak method
# Note: Dog.speak requires an argument, so we'll just use Cat and Duck for this simple demo
# or we could adapt Dog.
animal_sound(my_cat)
animal_sound(my_duck)

# Better Polymorphism Example with consistent interface:
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

shapes = [Rectangle(3, 4), Circle(5)]
for shape in shapes:
    print(f"Area: {shape.area()}")
