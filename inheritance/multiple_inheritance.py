class A:
    def method_a(self):
        print("Method A")

class B:
    def method_b(self):
        print("Method B")

class C(A, B):
    pass

c = C()
c.method_a()
c.method_b()


class Flyer:
    def fly(self):
        print("Flying")

class Swimmer:
    def swim(self):
        print("Swimming")

class Duck(Flyer, Swimmer):
    pass

d = Duck()
d.fly()
d.swim()


class Writer:
    def write(self):
        print("Writing")

class Speaker:
    def speak(self):
        print("Speaking")

class Author(Writer, Speaker):
    pass

a = Author()
a.write()
a.speak()


class X:
    def x(self):
        print("X")

class Y:
    def y(self):
        print("Y")

class Z(X, Y):
    pass

z = Z()
z.x()
z.y()


class Cook:
    def cook(self):
        print("Cooking")

class Driver:
    def drive(self):
        print("Driving")

class Person(Cook, Driver):
    pass

p = Person()
p.cook()
p.drive()