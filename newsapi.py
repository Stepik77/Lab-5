import requests
import json

def get_news(api_key, country='us', category='business', language='en'):
    base_url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'apiKey': api_key,
        'country': country,
        'category': category,
        'language': language,
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        news_data = response.json()

        for article in news_data.get('articles', []):
            print("Заголовок:", article.get('title'))
            print("Источник:", article.get('source', {}).get('name'))
            print("Автор:", article.get('author'))
            print("Дата:", article.get('publishedAt'))
            print("Описание:", article.get('description'))
            print("URL:", article.get('url'))
            print("-" * 30)
    else:
        print(f"Ошибка запроса: {response.status_code}")

if __name__ == "__main__":
    api_key = "08ba1a453d354fd1a24ff276727ef576"
    get_news(api_key)
