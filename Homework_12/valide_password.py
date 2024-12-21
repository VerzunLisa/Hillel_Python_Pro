import re


def is_password_strong(password):
    """Перевіряє, чи є пароль надійним."""
    if len(password) < 8:
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True


passwords = [
    "P@ssw0rd",
    "password",
    "Password123",
    "Short1@",
    "P@ssword1!"
]

for pwd in passwords:
    print(f"Пароль: {pwd} -> {'Надійний' if is_password_strong(pwd) else 'Ненадійний'}")
