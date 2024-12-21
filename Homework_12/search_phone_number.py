import re


def find_phone_numbers(text):
    """Знаходить усі телефонні номери в тексті."""
    pattern = r'\(?\d{3}\)?[.\-\s]?\d{3}[.\-\s]?\d{4}'
    return re.findall(pattern, text)


text = """
Список можливих телефоних номерів:
(123) 456-7890, 123-456-7890, 123.456.7890, 1234567890, and 987 654 3210.
Помилкові: 123-45-678, (123)4567-890, 12-3456-7890.
"""

found_numbers = find_phone_numbers(text)

print("Знайдені номери:")
for number in found_numbers:
    print(number)
