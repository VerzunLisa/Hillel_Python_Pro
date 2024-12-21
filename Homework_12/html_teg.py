import re


def remove_html_tags(text):
    """Видаляє всі HTML-теги з тексту."""
    return re.sub(r'<[^>]+>', '', text)


html_text = """
<h1>Welcome to my website</h1>
<p>This is a <strong>sample</strong> paragraph.</p>
<a href="https://example.com">Click here</a> for more information.
"""

clean_text = remove_html_tags(html_text)
print("Текст без HTML-тегів:")
print(clean_text)
