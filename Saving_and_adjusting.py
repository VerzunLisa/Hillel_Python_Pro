def create_user_settings():
    adjustments = {"theme": "light", "language": "italian", "notifications": True}

    def create_and_use(act, key=None, value=None):
        if act == "get":
            return adjustments.get(key, "Налаштування немає!")
        elif act == "set":
            adjustments[key] = value
            return f"Налаштування {key} оновленно до{value}"
        elif act == "all":
            return adjustments
        else:
            "Невідома дія"
    return create_and_use


user_01 = create_user_settings()
print(user_01('all'))
print(user_01('get', 'theme'))
print(user_01('set', 'theme', 'dark'))
print(user_01('get', 'theme'))
print(user_01('all'))
