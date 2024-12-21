import pandas as pd
from function import get_page, parse_news, filter_recent_news, save_to_csv

if __name__ == "__main__":
    URL = "https://www.pravda.com.ua/news/"

    print("Завантаження сторінки новин...")
    soup = get_page(URL)

    if soup:
        print("Парсинг новин...")
        news = parse_news(soup)

        if news:
            print(f"Знайдено {len(news)} новин.")
            print("Фільтрація новин за останні 7 днів...")
            recent_news = filter_recent_news(news, days=7)
            print(f"Новин за останні 7 днів: {len(recent_news)}.")

            print("Збереження новин у CSV...")
            save_to_csv(recent_news)

            print("Аналіз даних...")
            df = pd.DataFrame(recent_news)
            print(df['date'].value_counts())
        else:
            print("Новини не знайдено.")
    else:
        print("Не вдалося завантажити сторінку.")
