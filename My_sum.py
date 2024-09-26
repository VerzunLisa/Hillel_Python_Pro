import builtins
suma = 0


def my_sum(*args):
    global suma

    def sum():
        return "This is my custom sum function!"
    return sum()


numbers = (12, 8, 15, 23)
print(sum(numbers))
my_sum()
print(sum(numbers))
print(builtins.sum(numbers))
