import unittest
from django.test import Client

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()


    def test_get_shipment(self):
        resp = self.client.get('/api/v1/shipment/')
        self.assertEqual(
            resp.status_code, 200
        )
        self.assertEqual(
            len(resp.data['results']), resp.data['page_size']
        )


    def test_post_shipment(self):
        object = {
            "arrival_dt": "2022-05-10T05:53:00Z",
            "arrival_point": "London",
            "departure_dt": "2022-05-12T05:53:00Z",
            "departure_point": "Minsk",
            "cargo_volume": 100
        }
        resp = self.client.post(
            '/api/v1/shipment/',
            data = object,
            content_type="application/json"
        )
        self.assertEqual(
            resp.status_code, 200
        )
        self.assertEqual(
            all([object[key] == resp.data[key] for key in object.keys()]), True
        )

    def test_get_shipment_id(self):
        id = self.client.get('/api/v1/shipment/').data['results'][0]['id']
        resp = self.client.get(f'/api/v1/shipment/{id}/')
        self.assertEqual(
            resp.status_code, 200
        )


    def test_put_shipment_id(self):
        id = self.client.get('/api/v1/shipment/').data['results'][0]['id']
        object = {
            "arrival_dt": "2022-05-10T05:53:00Z",
            "arrival_point": "Test",
            "departure_dt": "2022-05-12T05:53:00Z",
            "departure_point": "Mest",
            "cargo_volume": 500
        }
        resp = self.client.put(
            f'/api/v1/shipment/{id}/',
            data = object,
            content_type="application/json"
        )
        self.assertEqual(
            resp.status_code, 200
        )
        self.assertEqual(
            all([object[key] == resp.json()[key] for key in object.keys()]), True
        )

        resp = resp = self.client.get(f'/api/v1/shipment/{id}/')
        self.assertEqual(
            all([object[key] == resp.json()[key] for key in object.keys()]), True
        )


    def test_put_shipment_id(self):
        id = self.client.get('/api/v1/shipment/').data['results'][0]['id']
        resp = self.client.delete(f'/api/v1/shipment/{id}/')
        self.assertEqual(
            resp.status_code, 204
        )
        resp = resp = self.client.get(f'/api/v1/shipment/{id}/')
        self.assertEqual(
            resp.status_code, 400
        )
