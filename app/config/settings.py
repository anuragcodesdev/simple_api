import os
from dotenv import load_dotenv

# Load env vars
load_dotenv()

def get_env_var(name: str) -> str:
    """Get env var or raise an error if missing.
    
    Params:
        :name: The name of the API Key stored in OS env.
    
    Returns:
        :value: API key stored in OS env.
    
    """
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"{name} environment variable is required but not set")
    return value

WEATHER_API_KEY = get_env_var("WEATHER_API_KEY")
NEWS_API_KEY = get_env_var("NEWS_API_KEY")
