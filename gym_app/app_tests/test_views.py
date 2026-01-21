from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class GymViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="1234")

    def test_dashboard_view(self):
        # Dashboard accessible without login (your current views don't use login_required)
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_members_view(self):
        response = self.client.get(reverse('members'))
        self.assertEqual(response.status_code, 200)

    def test_plans_view(self):
        response = self.client.get(reverse('plans'))
        self.assertEqual(response.status_code, 200)
