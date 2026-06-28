"""
Polymorphism in Python

Definition:
Polymorphism allows the same method name to have different behaviors
depending on the object that calls it.
"""

class Dog:
    def sound(self):
        print("Dog barks.") 
    
class Cat:
    def sound(self):
        print("Cat meows.")

def animal_sound(animal):
    animal.sound()

dog = Dog() 
cat = Cat() 

animal_sound(dog)
animal_sound(cat)