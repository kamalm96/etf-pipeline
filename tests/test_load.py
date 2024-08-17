import unittest
from etl.load import load_weather_data
from sqlalchemy import create_engine
import pandas as pd


class TestLoad(unittest.TestCase):
    def setUp(self):
        # Setup an in-memory SQLite database for testing
        self.engine = create_engine("sqlite:///:memory:")
        self.transformed_data = [
            {
                "city": "London",
                "temperature": 15,
                "humidity": 80,
                "weather": "clear sky",
                "timestamp": 1625256000,
            },
            {
                "city": "New York",
                "temperature": 20,
                "humidity": 60,
                "weather": "few clouds",
                "timestamp": 1625256000,
            },
        ]

    def test_load_weather_data(self):
        load_weather_data(self.transformed_data, self.engine)
        df = pd.read_sql("SELECT * FROM weather_data", self.engine)
        self.assertEqual(len(df), 2)
        self.assertIn("city", df.columns)
        self.assertEqual(df["city"].iloc[0], "London")


if __name__ == "__main__":
    unittest.main()
