class StringProcessor:

    def reverse_string(s: str) -> str:
        """Повертає рядок в зворотньорму порядку."""
        return s[::-1]

    def capitalize_string(s: str) -> str:
        """Повертає рядок в якому перша літера заглавна."""
        return s.capitalize()

    def count_vowels(s: str) -> int:
        """Підраховує кількість голосних літер в тексті."""
        vowels = "aeiouAEIOU"
        return sum(1 for char in s if char in vowels)
