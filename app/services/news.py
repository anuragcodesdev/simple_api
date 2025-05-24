import requests
from typing import List, Dict
from ..config import settings

def get_news(query: str) -> List[Dict[str, str]]:
    """
    Get top 5 news articles related to the query.
    Params:
        :query: Search term for news articles.

    Returns:
        :List[Dict[str, str]]: List of dictionaries each containing
        'title' and 'url' keys of news articles.
    """
    api_key = settings.NEWS_API_KEY
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}&pageSize=5"
    try:
        response = requests.get(url)
        response.raise_for_status() # raise error if status isn't 200.
        articles = response.json().get("articles", [])
    except requests.RequestException as e:
        print(f"News API request failed: {e}")
        return []

    return [{"title": a["title"], "url": a["url"]} for a in articles]
