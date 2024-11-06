import json


def load_books(filename="books.json"):
    """Data download function"""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def display_available_books(books):
    """A function to display available books"""
    print("Список доступних книг:")
    available_books = [book for book in books if book["наявність"]]
    for book in available_books:
        print(f"{book['назва']} - {book['автор']} ({book['рік']})")


def add_book(new_book, filename="books.json"):
    """Function for adding a new book"""
    books = load_books(filename)
    books.append(new_book)
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)
    print(f"Додано книгу: {new_book['назва']}")


books = load_books()  # Завантажити дані з JSON
display_available_books(books)  # Вивести список доступних книг

new_book = {
    "назва": "Книга 3",
    "автор": "Автор 3",
    "рік": 2020,
    "наявність": True
}
add_book(new_book)

books = load_books()
display_available_books(books)
