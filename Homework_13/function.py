import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta


def get_page(url):
    """
    Завантажує HTML-код сторінки за вказаним URL."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    except requests.exceptions.RequestException as e:
        print(f"Помилка завантаження сторінки: {e}")
        return None


def parse_news(soup):
    """Парсить новини зі сторінки."""
    news_data = []
    news_items = soup.select(".article_news_list")

    for item in news_items:
        try:
            time = item.select_one(".article_time").get_text(strip=True)
            title = item.select_one(".article_header a").get_text(strip=True)
            link = item.select_one(".article_header a")["href"]
            summary = item.select_one(".article_subheader").get_text(strip=True) if item.select_one(
                ".article_subheader") else "Немає опису"
            date = datetime.now().strftime("%Y-%m-%d")

            news_data.append({
                "time": time,
                "title": title,
                "link": link,
                "summary": summary,
                "date": date
            })
        except AttributeError as e:
            print(f"Помилка парсингу однієї новини: {e}")

    return news_data


def save_to_csv(data, filename="news.csv"):
    """Зберігає новини у CSV-файл."""
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Новини збережено у файл {filename}.")


def filter_recent_news(news, days=7):
    """Фільтрує новини за останні кілька днів."""
    recent_date = datetime.now() - timedelta(days=days)
    return [item for item in news if datetime.strptime(item['date'], "%Y-%m-%d") >= recent_date]
