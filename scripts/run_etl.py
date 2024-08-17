import sys
import os

script_path = os.path.abspath(__file__)

project_root = os.path.dirname(os.path.dirname(script_path))

sys.path.insert(0, project_root)

from etl.extract import extract_weather_data
from etl.transform import transform_weather_data
from etl.load import load_weather_data
from config import config
from sqlalchemy import create_engine


def main():
    # Step 1: Extract
    raw_data = extract_weather_data(config.CITIES, config.API_KEY)

    # Step 2: Transform
    transformed_data = transform_weather_data(raw_data)

    # Step 3: Load
    engine = create_engine(config.DATABASE_URI)
    load_weather_data(transformed_data, engine)


if __name__ == "__main__":
    main()
