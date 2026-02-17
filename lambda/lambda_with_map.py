numbers = [1, 2, 3]
squared = list(map(lambda x: x**2, numbers))
print(squared)

names = ["anna", "john"]
upper = list(map(lambda x: x.upper(), names))
print(upper)

doubled = list(map(lambda x: x*2, numbers))
print(doubled)

lengths = list(map(lambda x: len(x), names))
print(lengths)

plus_one = list(map(lambda x: x+1, numbers))
print(plus_one)