import unittest
from src.api.app import app

class TestAddressNormalizationAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_normalize_address(self):
        response = self.app.post('/normalize', json={'address': 'Av. Juárez 123, Col. Centro'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('normalized_address', response.get_json())

    def test_normalize_address_invalid(self):
        response = self.app.post('/normalize', json={'address': ''})
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()