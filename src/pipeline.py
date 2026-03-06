from .config import CITIES
from .extractor import fetch_weather
from .transformer import transform_weather
from .loader import save_raw, insert_raw, insert_clean, get_connection

def run_pipeline(logger):

    logger.info("Pipeline started")

    conn = get_connection()

    for city in CITIES:

        raw = fetch_weather(city, logger)

        if raw is None:
            continue

        save_raw(city, raw, logger)
        insert_raw(conn, city, raw, logger)

        clean = transform_weather(raw)
        insert_clean(conn, clean, logger)

    conn.close()

    logger.info("Pipeline finished")
