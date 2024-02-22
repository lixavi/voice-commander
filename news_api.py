# news_api.py

import requests

class NewsAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://newsapi.org/v2/top-headlines"

    def get_news(self):
        try:
            params = {"apiKey": self.api_key, "country": "us"}
            response = requests.get(self.base_url, params=params)
            data = response.json()
            if response.status_code == 200:
                articles = data["articles"]
                news_headlines = ""
                for article in articles:
                    news_headlines += f"{article['title']}\n"
                return news_headlines
            else:
                return "Sorry, unable to fetch news updates at the moment."
        except Exception as e:
            return f"An error occurred: {e}"
