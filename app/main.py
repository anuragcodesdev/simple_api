from fastapi import FastAPI, HTTPException
from typing import Dict
from app.services.weather import get_weather
from app.services.news import get_news

app = FastAPI()

@app.get("/combined")
def read_combined(city: str) -> Dict[str, object]:
    """
    Get current weather for city and related news based on weather description.
    
    Params:
        :city: Name of city to get weather for.
    
    Returns:
        :Dict: Contains 'weather' dict and 'news' list related to weather description.
    """
    weather = get_weather(city)
    if not weather:
        raise HTTPException(status_code=404, detail="Weather data not found")

    news = get_news(weather["description"])
    return {
        "weather": weather,
        "news": news
    }
