import pandas as pd


def load_weather_data(transformed_data, db_engine):
    df = pd.DataFrame(transformed_data)
    df.to_sql("weather_data", db_engine, if_exists="append", index=False)
