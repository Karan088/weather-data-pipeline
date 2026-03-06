import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD")
}

CITIES = ["Colombo", "Matara"]

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
RAW_DATA_FOLDER = "data/raw"
LOG_FOLDER = "logs"
