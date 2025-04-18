from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now
import json

class RootURLTests(TestCase):
    def test_root_url_returns_expected_message(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        # Parse response content
        data = json.loads(response.content.decode('utf-8'))

        self.assertEqual(data["status"], "success")
        self.assertEqual(data["message"], "Welcome to SokaFix Backend!")
        self.assertIn("timestamp", data)
        self.assertIn("routes", data)
        self.assertEqual(data["routes"]["admin"], "/admin/")
        self.assertEqual(data["routes"]["contact_api"], "/api/contact/")
        self.assertEqual(data["routes"]["newsletter_api"], "/api/subscribe/")
