import re


def is_valid_email(email):
    """Перевіряє, чи є email-адреса валідною."""
    pattern = r'^[a-zA-Z0-9](\.?[a-zA-Z0-9]+)*@[a-zA-Z0-9]+\.[a-zA-Z]{2,6}$'
    return bool(re.match(pattern, email))


emails = [
    "verzun@domain.com",
    "lika.usik@domain.org",
    ".likausik@domain.com",
    "usik.@domain.com"
]

for email in emails:
    print(f"{email}: {'Валідний' if is_valid_email(email) else 'Невалідний'}")
