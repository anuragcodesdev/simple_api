from typing import List, Dict
from httpx import HTTPStatusError
from app.utils.client import async_client
from app.config import settings

async def get_news(query: str) -> List[Dict[str, str]]:
    """
    Get top 5 news articles related to the query.
    Params:
        :query: Search term for news articles.

    Returns:
        :List[Dict[str, str]]: List of dictionaries each containing
        'title' and 'url' keys of news articles.
    """
    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={query}&apiKey={settings.NEWS_API_KEY}&pageSize=5"
    )
    
    try:
        response = await async_client.get(url, timeout=10)
        response.raise_for_status() # raise error if status isn't 200.
        articles = response.json().get("articles", [])
        return [{"title": a["title"], "url": a["url"]} for a in articles if a.get("title") and a.get("url")]
    
    except HTTPStatusError as e:
        print(f"[News API] HTTP error: {e.response.status_code} - {e.response.text}")
    except Exception as e:
        print(f"[News API] Request failed: {e}")

    return []
