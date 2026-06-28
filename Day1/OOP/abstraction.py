"""
Abstraction in Python

Definition:
Abstraction is the process of hiding implementation details
and showing only the essential features to the user.

Python provides abstraction using the abc (Abstract Base Class) module.
"""
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):

    def start(self):
        print("Car is starting...")

class Bike(Vehicle):

    def start(self):
        print("Bike is starting...")

car = Car()
bike = Bike()

car.start()
bike.start()