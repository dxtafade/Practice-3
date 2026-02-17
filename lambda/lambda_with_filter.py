numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

positives = list(filter(lambda x: x > 0, [-2, 3, -1, 5]))
print(positives)

long_words = list(filter(lambda x: len(x) > 4, ["apple", "car", "banana"]))
print(long_words)

greater_than_three = list(filter(lambda x: x > 3, numbers))
print(greater_than_three)

non_empty = list(filter(lambda x: x != "", ["a", "", "b"]))
print(non_empty)