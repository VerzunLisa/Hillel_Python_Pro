subscribers = []


def subscribe(name: str):
    subscribers.append(name)

    def confirm_subscribe():
        return f"Підписка підтверджена для {name}"
    return confirm_subscribe()


def unsubscribe(name: str):
    if subscribers.count(name) >= 1:
        subscribers.remove(name)
        return f"{name}, успішна відписка!"
    else:
        return "Дане ім'я не знайдено!"


subscribe("Olena")
subscribe("Ihor")
print(subscribers)
print(unsubscribe("Ihor"))
print(subscribers)
