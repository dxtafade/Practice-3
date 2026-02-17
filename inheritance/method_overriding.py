class Animal:
    def speak(self):
        print("Animal sound")

class Cat(Animal):
    def speak(self):
        print("Meow")

c = Cat()
c.speak()


class Shape:
    def draw(self):
        print("Drawing shape")

class Circle(Shape):
    def draw(self):
        print("Drawing circle")

circle = Circle()
circle.draw()


class Vehicle:
    def move(self):
        print("Vehicle moving")

class Bike(Vehicle):
    def move(self):
        print("Bike moving")

b = Bike()
b.move()


class Person:
    def role(self):
        print("Person")

class Student(Person):
    def role(self):
        print("Student")

s = Student()
s.role()


class Device:
    def status(self):
        print("Device on")

class Laptop(Device):
    def status(self):
        print("Laptop on")

l = Laptop()
l.status()