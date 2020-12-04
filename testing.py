import unittest
from app.utils import get_current_weather
from app import app


class TestCase(unittest.TestCase):
    def test_weather(self):
        weather = get_current_weather(app.config["CURRENT_CITY"])
        self.assertEqual(type(weather), list)  # If overall return is a list, then other functions won't break
        self.assertEqual(type(weather[2]), str)  # If icon is found, then request was successful

if __name__ == '__main__':
    unittest.main()
