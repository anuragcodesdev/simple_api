from typing import Dict, Optional
from httpx import HTTPStatusError
from app.utils.client import async_client
from ..config import settings

async def get_weather(city: str) -> Optional[Dict[str, str]]:
    """
    Fetches current weather data for a city.

    Args:
        city (str): The city to fetch weather for.

    Returns:
        Optional[Dict[str, str]]: Temperature and weather description, or None if failed.
    """
    url = (
        f"http://api.openweathermap.org/data/2.5/weather?"
        f"q={city}&appid={settings.WEATHER_API_KEY}&units=metric"
    )
    
    try:
        response = await async_client.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return {
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
    except HTTPStatusError as e:
        print(f"Weather API, HTTP error: {e.response.status_code} - {e.response.text}")
    except Exception as e:
        print(f"Weather API Request failed: {e}")

    return None
