import re


def extract_hashtags(text):
    """Видобуває список хеш-тегів з тексту."""
    pattern = r'#\w+'
    return re.findall(pattern, text)


text = """
#Python, #coding, #100DaysOfCode, and #AI2024., #, #123abc$, and normal text without hashtags.
"""

hashtags = extract_hashtags(text)

print("Знайдені хеш-теги:")
for hashtag in hashtags:
    print(hashtag)
