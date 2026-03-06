import requests
import time
from .config import BASE_URL, API_KEY

def fetch_weather(city, logger, retries=3):

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    for attempt in range(retries):

        try:
            response = requests.get(BASE_URL, params=params, timeout=10)

            if response.status_code == 200:
                logger.info(f"API success: {city}")
                return response.json()

            logger.warning(f"API status {response.status_code}")

        except Exception as e:
            logger.error(f"API error {city}: {e}")

        time.sleep(2)

    logger.error(f"Failed after retries: {city}")
    return None
