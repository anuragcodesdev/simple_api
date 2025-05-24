# Weather and News API Integration — Learning Project

This is a simple project I built to review and reinforce my understanding of working with FastAPI and creating APIs. It’s intentionally straightforward — nothing fancy or complex — just practical, clean, and easy to follow.


## What This Does

- Fetches current weather data for any city using the OpenWeatherMap API
- Retrieves the top 5 news articles related to the weather description via NewsAPI
- Demonstrates modular code organisation with separate config, service, and main app files
- Shows how to manage API keys securely with environment variables
- Includes basic error handling


## Requirements

- Python 3.10+
- pip (Python package manager)
- [OpenWeatherMap API key](https://openweathermap.org/api)
- [NewsAPI key](https://newsapi.org/)


## Setup

1. Clone this repo:

   ```bash
   git clone https://github.com/anuragcodesdev/simple_api.git
   ```

2. Create and activate a virtual environment:
    python -m venv venv
    source venv/bin/activate

3. Install dependencies:
    pip install -r requirements.txt

4. Create an .env file in the root directory and API Keys as follows:
    
    WEATHER_API_KEY = `your_openweathermap_api_key_here`

    NEWS_API_KEY= `your_newsapi_key_here`


## Running the app
1. Start the FastAPI server with:
    '''bash
    uvicorn run:fastapi_app --reload
    '''

2. Open your browser and go to:
    
    `{whatever_server_stated}`/combined?city=Melbourne

    Replace 'Melbourne' with any city you want.