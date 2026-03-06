# Weather Data Pipeline

This project implements a simple end-to-end data engineering pipeline that collects weather data from the OpenWeather API and stores it in PostgreSQL using a modular ETL architecture.

Pipeline workflow:

1. Extract weather data from the OpenWeather API for multiple cities
2. Store raw API responses as JSON files and in a PostgreSQL raw table
3. Transform JSON data into structured fields
4. Load cleaned data into an analytics-ready PostgreSQL table
5. Log pipeline execution and handle API retries

Key features:
- Modular pipeline structure (extractor, transformer, loader)
- API ingestion with retry handling
- Raw and clean data layers (Bronze / Silver architecture)
- PostgreSQL integration
- Structured logging
- Environment variable configuration for secrets

Technologies used:
- Python
- PostgreSQL
- REST API
- Requests
- Psycopg2
- Python Logging
- dotenv

The pipeline can be executed using:python run_pipeline.py


## How to Run the Pipeline

1. Clone the repository


2. Install dependencies

pip install -r requirements.txt


3. Create a `.env` file in the project root and add your credentials

OPENWEATHER_API_KEY=your_api_key
DB_HOST=localhost
DB_NAME=de_lab
DB_USER=postgres
DB_PASSWORD=your_password


4. Ensure PostgreSQL is running and the database (`de_lab`) exists.  
Create the required tables (`weather_raw` and `weather_clean`) if they are not already present.


5. Run the pipeline

python run_pipeline.py


The pipeline will:
- Pull weather data from the OpenWeather API
- Save raw JSON files
- Insert raw data into PostgreSQL
- Transform and load cleaned data into the analytics table
- Generate execution logs
