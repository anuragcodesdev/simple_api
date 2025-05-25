from fastapi import FastAPI, HTTPException
from typing import Dict
from contextlib import asynccontextmanager
from app.services.weather import get_weather
from app.services.news import get_news
from app.utils.client import async_client

app = FastAPI()

@app.get("/combined")
async def read_combined(city: str) -> Dict[str, object]:
    """
    Get current weather for city and related news based on weather description.
    
    Params:
        :city: Name of city to get weather for.
    
    Returns:
        :Dict: Contains 'weather' dict and 'news' list related to weather description.
    """
    weather = await get_weather(city)
    if not weather:
        raise HTTPException(status_code=404, detail="Weather data not found.")

    news = await get_news(weather["description"])
    return {
        "weather": weather,
        "news": news
    }
    
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Everything that needs to run before startup
    yield
    # Everything that needs to run after startup
    
    # Shutdown logic: close async HTTP client
    await async_client.aclose()
