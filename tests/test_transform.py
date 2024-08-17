import unittest
from etl.transform import transform_weather_data


class TestTransform(unittest.TestCase):
    def test_transform_weather_data(self):
        raw_data = [
            {
                "name": "London",
                "main": {"temp": 15, "humidity": 80},
                "weather": [{"description": "clear sky"}],
                "dt": 1625256000,
            }
        ]
        transformed_data = transform_weather_data(raw_data)
        self.assertEqual(len(transformed_data), 1)
        self.assertIn("city", transformed_data[0])
        self.assertEqual(transformed_data[0]["city"], "London")


if __name__ == "__main__":
    unittest.main()
