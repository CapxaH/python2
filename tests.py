import unittest
import json
import client
import server


class TestClient(unittest.TestCase):

    def test_presence_structure(self):
        msg = client.get_presence_message("")

        expected_keys = ["action", "time", "type", "user"]

        self.assertTrue(all([i in msg for i in expected_keys]))

    def test_user_structure(self):
        msg = client.get_user("", "")

        expected_keys = ["account_name", "status"]

        self.assertTrue(all([i in msg for i in expected_keys]))

    def test_format_message(self):
        msg = {"Hello": "World"}
        expected = json.dumps(msg).encode("utf-8")

        self.assertEqual(expected, client.format_message(msg))
