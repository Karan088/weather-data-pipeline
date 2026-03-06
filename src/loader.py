import psycopg2
import json
import os
from .config import DB_CONFIG, RAW_DATA_FOLDER

def get_connection():

    return psycopg2.connect(**DB_CONFIG)


def save_raw(city, data, logger):

    os.makedirs(RAW_DATA_FOLDER, exist_ok=True)

    from datetime import datetime

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{RAW_DATA_FOLDER}/{city}_{timestamp}.json"

    with open(filename, "w") as f:
        json.dump(data, f)

    logger.info(f"Raw saved: {filename}")


def insert_raw(conn, city, data, logger):

    cur = conn.cursor()

    query = """
    INSERT INTO weather_raw (city, api_response)
    VALUES (%s,%s)
    """

    cur.execute(query, (city, json.dumps(data)))
    conn.commit()

    logger.info(f"Raw inserted: {city}")


def insert_clean(conn, data, logger):

    cur = conn.cursor()

    query = """
    INSERT INTO weather_clean
    (city, temperature, humidity, pressure, wind_speed, weather_desc, observation_time, ingestion_time)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """

    cur.execute(query, (
        data["city"],
        data["temperature"],
        data["humidity"],
        data["pressure"],
        data["wind_speed"],
        data["weather_desc"],
        data["observation_time"],
        data["ingestion_time"]
    ))

    conn.commit()

    logger.info(f"Clean inserted: {data['city']}")
