total_expense = 0


def add_expense(price):
    global total_expense
    if price > 0:
        total_expense += price
        return total_expense


def see_expense():
    return f"Загальна сума витрат {total_expense}"


def consol_menu():
    while True:
        print("Добрий день. Ви хочете переглянути витрати? Або додати витрати?")
        print("Виберіть\n 1. Додати \n2. Переглянути\n")
        variant = input()
        if variant == '1':
            price = float(input("Введіть сумму: "))
            add_expense(price)
            print(f"Ви додали суму {price}")
        elif variant == "2":
            print(f"{see_expense()}")
        else:
            print("Помилка! Спробуйте ще раз!")


consol_menu()
