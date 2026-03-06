from datetime import datetime

def transform_weather(raw):

    return {
        "city": raw["name"],
        "temperature": raw["main"]["temp"],
        "humidity": raw["main"]["humidity"],
        "pressure": raw["main"]["pressure"],
        "wind_speed": raw["wind"]["speed"],
        "weather_desc": raw["weather"][0]["description"],
        "observation_time": datetime.fromtimestamp(raw["dt"]),
        "ingestion_time": datetime.now()
    }
