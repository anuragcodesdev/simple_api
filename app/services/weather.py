import requests
from typing import List, Dict
from ..config import settings

def get_weather(city: str) -> Dict[str, object]:
    """
    Get current weather data for the specified city.

    Params:
        :city: Name of the city to fetch weather for.

    Returns:
        :Dict[str, object]: Dictionary containing:
            - 'temperature' (float): Current temperature in Celsius.
            - 'description' (str): Weather description.
    """
    api_key = settings.WEATHER_API_KEY
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status() # raise error if status isn't 200.
        data = response.json()
    except requests.RequestException as e:
        print(f"Weather API request failed: {e}")
        return {}

    return {
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"]
    }
