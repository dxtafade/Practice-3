def greet(name):
    print("Hello", name)

greet("Alex")


def add(a, b):
    print(a + b)

add(5, 7)


def power(base, exponent=2):
    print(base ** exponent)

power(3)
power(3, 3)


def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce("Alex", 22)


def is_even(number):
    print(number % 2 == 0)

is_even(4)