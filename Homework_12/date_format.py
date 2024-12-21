def reformat_date(date):
    """
    Перетворює дату з формату DD/MM/YYYY у формат YYYY-MM-DD."""
    try:
        day, month, year = date.split('/')
        return f"{year}-{month}-{day}"
    except ValueError:
        raise ValueError("Невірний формат дати. Очікується формат DD/MM/YYYY.")


dates = [
    "25/12/2024",
    "01/01/2023",
    "31/07/2022"
]

for date in dates:
    formatted_date = reformat_date(date)
    print(f"Оригінальна дата: {date} -> Форматована дата: {formatted_date}")
