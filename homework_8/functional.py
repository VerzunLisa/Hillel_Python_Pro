def add_movie():
    conn = sqlite3.connect("kinobaza.db")
    cursor = conn.cursor()

    title = input("Введіть назву фільму: ")
    release_year = int(input("Введіть рік випуску: "))
    genre = input("Введіть жанр: ")

    cursor.execute("INSERT INTO movies (title, release_year, genre) VALUES (?, ?, ?)",
                   (title, release_year, genre))
    movie_id = cursor.lastrowid

    print("Додайте акторів, які знімалися у цьому фільмі (введіть 0 для завершення):")
    while True:
        actor_id = int(input("ID актора: "))
        if actor_id == 0:
            break
        cursor.execute("INSERT OR IGNORE INTO movie_cast (movie_id, actor_id) VALUES (?, ?)",
                       (movie_id, actor_id))

    conn.commit()
    conn.close()
    print("Фільм успішно додано!")

def add_actor():
    conn = sqlite3.connect("kinobaza.db")
    cursor = conn.cursor()

    name = input("Введіть ім'я актора: ")
    birth_year = int(input("Введіть рік народження: "))

    cursor.execute("INSERT INTO actors (name, birth_year) VALUES (?, ?)", (name, birth_year))
    conn.commit()
    conn.close()
    print("Актор успішно доданий!")

def show_movies_with_actors():
    conn = sqlite3.connect("kinobaza.db")
    cursor = conn.cursor()

    query = """
        SELECT movies.title, GROUP_CONCAT(actors.name, ', ') AS actors
        FROM movies
        LEFT JOIN movie_cast ON movies.id = movie_cast.movie_id
        LEFT JOIN actors ON movie_cast.actor_id = actors.id
        GROUP BY movies.id
    """
    for row in cursor.execute(query):
        print(f"Фільм: {row[0]}, Актори: {row[1] if row[1] else 'немає'}")

    conn.close()

def show_unique_genres():
    conn = sqlite3.connect("kinobaza.db")
    cursor = conn.cursor()

    query = "SELECT DISTINCT genre FROM movies"
    for row in cursor.execute(query):
        print(row[0])

    conn.close()

def show_movies_by_genre():
    conn = sqlite3.connect("kinobaza.db")
    cursor = conn.cursor()

    query = """
        SELECT genre, COUNT(*) as count
        FROM movies
        GROUP BY genre
    """
    for row in cursor.execute(query):
        print(f"Жанр: {row[0]}, Кількість фільмів: {row[1]}")

    conn.close()

def show_average_birth_year_by_genre():
    conn = sqlite3.connect("kinobaza.db")
    cursor = conn.cursor()

    genre = input("Введіть жанр: ")
    query = """
        SELECT AVG(actors.birth_year) AS average_birth_year
        FROM movies
        JOIN movie_cast ON movies.id = movie_cast.movie_id
        JOIN actors ON movie_cast.actor_id = actors.id
        WHERE movies.genre = ?
    """
    cursor.execute(query, (genre,))
    row = cursor.fetchone()
    print(f"Середній рік народження акторів: {row[0] if row[0] else 'немає даних'}")

    conn.close()

def search_movies():
    conn = sqlite3.connect("kinobaza.db")
    cursor = conn.cursor()

    keyword = input("Введіть ключове слово для пошуку: ")
    query = "SELECT title FROM movies WHERE title LIKE ?"
    for row in cursor.execute(query, (f"%{keyword}%",)):
        print(row[0])

    conn.close()

def paginate_movies():
    conn = sqlite3.connect("kinobaza.db")
    cursor = conn.cursor()

    page = int(input("Введіть номер сторінки: "))
    limit = 5
    offset = (page - 1) * limit
    query = "SELECT title FROM movies LIMIT ? OFFSET ?"
    for row in cursor.execute(query, (limit, offset)):
        print(row[0])

    conn.close()

def union_movies_actors():
    conn = sqlite3.connect("kinobaza.db")
    cursor = conn.cursor()

    query = """
        SELECT name FROM actors
        UNION
        SELECT title FROM movies
    """
    for row in cursor.execute(query):
        print(row[0])

    conn.close()

def show_movies_with_age():
    conn = sqlite3.connect("kinobaza.db")
    cursor = conn.cursor()

    query = """
        SELECT title, movie_age(release_year) AS age
        FROM movies
    """
    for row in cursor.execute(query):
        print(f"Фільм: {row[0]}, Вік: {row[1]} років")

    conn.close()
