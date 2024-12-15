import unittest
from string_processor import StringProcessor


class TestStringProcessor(unittest.TestCase):
    def test_reverse_string(self):
        """Тест на правильністі виконання StringProcessor.reverse_string."""
        self.assertEqual(StringProcessor.reverse_string("hello"), "olleh")
        self.assertEqual(StringProcessor.reverse_string("Python"), "nohtyP")
        self.assertEqual(StringProcessor.reverse_string("12345"), "54321")

    @unittest.skip("Тест з порожнім рядком пропущено через відому проблему")
    def test_reverse_string_empty(self):
        self.assertEqual(StringProcessor.reverse_string(""), "")

    def test_capitalize_string(self):
        """Тест на правильністі виконання StringProcessor.capitalize_string."""
        self.assertEqual(StringProcessor.capitalize_string("hello"), "Hello")
        self.assertEqual(StringProcessor.capitalize_string("python"), "Python")
        self.assertEqual(StringProcessor.capitalize_string("123abc"), "123abc")
        self.assertEqual(StringProcessor.capitalize_string(""), "")

    def test_count_vowels(self):
        """Тест на правильністі виконання StringProcessor.count_vowels."""
        self.assertEqual(StringProcessor.count_vowels("hello"), 2)
        self.assertEqual(StringProcessor.count_vowels("Python"), 1)
        self.assertEqual(StringProcessor.count_vowels("bcdfg"), 0)
        self.assertEqual(StringProcessor.count_vowels("AEIOU"), 5)
        self.assertEqual(StringProcessor.count_vowels(""), 0)
        self.assertEqual(StringProcessor.count_vowels("123456"), 0)
