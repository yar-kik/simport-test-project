from analytics.tests import BaseCase, create_event


class TestAnalyticApi(BaseCase):

    def test_get_info(self):
        """
        Testing get info endpoint
        """
        create_event()
        response = self.client.get("/api/info")
        self.assertEqual(response.status_code, 200)
        self.assertListEqual(response.json["brand"], ["Downy"])

    def test_get_timeline(self):
        """
        Testing get timeline endpoint
        """
        create_event()
        response = self.client.get('/api/timeline')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json["timeline"]), 1)
        self.assertEqual(response.json["timeline"][0]["value"], 1)
