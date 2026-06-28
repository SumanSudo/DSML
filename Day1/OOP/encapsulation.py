"""
Encapsulation in Python

Defination:
Encapsulation is the process of wrapping data (attributes) and methods
into a single unit (class) while restricting direct access to the data.

In Python, encapsulation is achieved using:
1. Public Members
2. Protected Members (_)
3. Private Members (__)
"""

class Student:
    def __init__(self, name, age):
        self.name = name   # Public
        self._age = age     # Protected
        self.__grade = "A"  #Private
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self._age}")
        print(f"Grade: {self.__grade}")

student = Student("Suman", 20)

# Public mumber
print(student.name)

# Protected member (accessible, but should be treated as internal)
print(student._age)

# Private menber (Not accessbile directly) 
# print(student.__grade) # AttributeError

student.display()