import requests


class WebService:

    def get_data(self, url: str) -> dict:
        """Робиться GET запит використовуючи бібліотеку requests, та повертається відповідь в json форматі."""
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
