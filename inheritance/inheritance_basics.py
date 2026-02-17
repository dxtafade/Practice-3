class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    pass

dog = Dog()
dog.speak()


class Vehicle:
    def move(self):
        print("Moving")

class Car(Vehicle):
    pass

c = Car()
c.move()


class Person:
    def walk(self):
        print("Walking")

class Student(Person):
    pass

s = Student()
s.walk()


class Shape:
    def draw(self):
        print("Drawing")

class Circle(Shape):
    pass

circle = Circle()
circle.draw()


class Device:
    def turn_on(self):
        print("On")

class Phone(Device):
    pass

phone = Phone()
phone.turn_on()