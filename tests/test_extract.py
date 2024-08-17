import unittest
from etl.extract import extract_weather_data
from config import config


class TestExtract(unittest.TestCase):
    def test_extract_weather_data(self):
        data = extract_weather_data(config.CITIES, config.API_KEY)
        self.assertGreater(len(data), 0)
        self.assertIn("name", data[0])


if __name__ == "__main__":
    unittest.main()
