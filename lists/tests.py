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

    def test_can_save_a_POST_request(self):
        item_text = 'to do a new item'
        response = self.client.post('/', data={'item_text': item_text})

        self.assertContains(response, item_text)
        self.assertTemplateUsed(response, 'lists/home_page.html')

