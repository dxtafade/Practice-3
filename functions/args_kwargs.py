def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3))


def print_args(*args):
    for item in args:
        print(item)

print_args("Apple", "Banana", "Orange")


def print_info(**info):
    for key, value in info.items():
        print(key, ":", value)

print_info(name="Dias", age=22)


def show_data(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

show_data(1, 2, 3, name="Anna")


def count_args(*args):
    return len(args)

print(count_args(1, 2, 3, 4))