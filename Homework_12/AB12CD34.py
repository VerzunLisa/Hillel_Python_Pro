import re


def contains_pattern(text):
    """Перевіряє, чи міститься у тексті рядок формату AB12CD34."""
    pattern = r'\b[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{2}\b'
    return bool(re.search(pattern, text))


text1 = "This is a sample text with pattern AB12CD34."
text2 = "No valid pattern here, just AB12CD3 or A1B2C3D4."

print("Результат для text1:", contains_pattern(text1))
print("Результат для text2:", contains_pattern(text2))
