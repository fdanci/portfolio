from django.test import TestCase


class TestViews(TestCase):
    """Test cases for all the views."""

    def test_index(self):
        """Test if requests work for index page."""
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)

    def test_work(self):
        """Test if requests work for work page."""
        response = self.client.get('/work/')
        self.assertEqual(response.status_code, 200)

    def test_about_me(self):
        """Test if requests work for about_me page."""
        response = self.client.get('/about_me/')
        self.assertEqual(response.status_code, 200)

    def test_hobbies(self):
        """Test if requests work for hobbies page."""
        response = self.client.get('/hobbies/')
        self.assertEqual(response.status_code, 200)