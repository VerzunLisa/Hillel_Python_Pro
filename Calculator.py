def create_calculator(meaning):
    def calcul(a, b):
        if meaning == "+":
            return a + b
        elif meaning == "-":
            return a - b
        elif meaning == "*":
            return a * b
        elif meaning == "/":
            return a / b
        else:
            print("Помилка!")
    return calcul


add = create_calculator("+")
multiply = create_calculator("*")
lifting = create_calculator("-")
division = create_calculator("/")
print(add(5, 3))
print(lifting(5, 3))
print(multiply(5, 3))
