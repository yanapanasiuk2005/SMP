# UTest/test_logging.py
import unittest

from Data.Lab7.Classes.Logger import Logger


class TestLogger(unittest.TestCase):
    def setUp(self):
        self.logger = Logger()

    def test_log_query(self):
        self.logger.log_query("New York", {"temperature": 20})
        self.assertEqual(len(self.logger.query_history), 1)
        self.assertEqual(self.logger.query_history[0]['query'], "New York")
        self.assertEqual(self.logger.query_history[0]['result']['temperature'], 20)

    def test_empty_history(self):
        self.assertEqual(len(self.logger.query_history), 0)


if __name__ == '__main__':
    unittest.main()
