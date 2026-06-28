"""
Inheritance in Python

Definition:
Inheritance is the process of creating a new class from an existing class.
It allows code reusability by inheriting attributes and methods from the parent class.
"""

class Animal:
    def eat(self):
        print("Animal is eating.")
    
class Dog(Animal):
    def  bark(self):
        print("Dog is barking.")

dog = Dog() 

dog.eat()   # Inherited from Animal
dog.bark()  # Defined in Dog