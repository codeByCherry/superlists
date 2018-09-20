from django.test import TestCase
from django.urls import resolve
from .views import home_page


class SmokeTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_root_url_resolve_to_home_page(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/home_page.html')


