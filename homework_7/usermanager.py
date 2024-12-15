class UserManager:
    """Управління користувачами"""
    def __init__(self):
        self.users = []

    def add_user(self, name: str, age: int):
        """Додати користувача за параметрами ім'я та вік."""
        self.users.append({"name": name, "age": age})

    def remove_user(self, name: str):
        """Видалення користувача за ім'ям"""
        self.users = [user for user in self.users if user["name"] != name]

    def get_all_users(self) -> list:
        """Відобразити список користувачів"""
        return self.users
    