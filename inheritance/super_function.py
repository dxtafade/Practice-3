class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

s = Student("Anna", "A")
print(s.name, s.grade)


class Animal:
    def speak(self):
        print("Sound")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof")

d = Dog()
d.speak()


class Car:
    def __init__(self, brand):
        self.brand = brand

class ElectricCar(Car):
    def __init__(self, brand, battery):
        super().__init__(brand)
        self.battery = battery

ec = ElectricCar("Tesla", "100kWh")
print(ec.brand, ec.battery)


class Shape:
    def area(self):
        return 0

class Square(Shape):
    def area(self):
        return super().area() + 4

sq = Square()
print(sq.area())


class Person:
    def greet(self):
        print("Hello")

class Teacher(Person):
    def greet(self):
        super().greet()
        print("I am a teacher")

t = Teacher()
t.greet()