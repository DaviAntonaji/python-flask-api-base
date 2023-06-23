import unittest
import requests

HEALTH_CHECK_URL = "http://localhost:5001/"

class HealthCheck(unittest.TestCase):

    def test_health_check(self):
        response = requests.get(HEALTH_CHECK_URL)
        self.assertEqual(response.status_code, 200)
        json_data = response.json()
        self.assertIn("version", json_data)
        self.assertLess(response.elapsed.total_seconds(), 1.0)

if __name__ == '__main__':
    unittest.main()
