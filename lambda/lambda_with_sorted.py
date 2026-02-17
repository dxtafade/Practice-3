numbers = [5, 2, 8, 1]
sorted_numbers = sorted(numbers, key=lambda x: x)
print(sorted_numbers)

words = ["apple", "banana", "kiwi"]
sorted_by_length = sorted(words, key=lambda x: len(x))
print(sorted_by_length)

students = [("Anna", 85), ("John", 75)]
sorted_by_score = sorted(students, key=lambda x: x[1])
print(sorted_by_score)

reverse_sort = sorted(numbers, key=lambda x: x, reverse=True)
print(reverse_sort)

sorted_by_last_letter = sorted(words, key=lambda x: x[-1])
print(sorted_by_last_letter)