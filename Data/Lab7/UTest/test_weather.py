# UTest/test_weather.py
import unittest

from Data.Lab7.Functions.WeatherFunctions import get_weather


class TestWeatherFunctions(unittest.TestCase):
    def test_get_weather_success(self):
        city = "London"
        weather = get_weather(city)
        self.assertIsNotNone(weather)
        self.assertIn("temperature", weather)
        self.assertIn("city", weather)

    def test_get_weather_invalid_city(self):
        city = "InvalidCityName"
        weather = get_weather(city)
        self.assertIsNone(weather)


if __name__ == '__main__':
    unittest.main()
