from analytics.tests import BaseCase


class TestInfoApi(BaseCase):

    def test_get_info(self):
        response = self.client.get("/api/info")
        self.assertEqual(response.status_code, 200)
        self.assertListEqual(response.json["brand"], ["Downy"])
