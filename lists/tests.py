from django.test import TestCase
from .models import Item


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


class ItemModelTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_save_and_retrieving_items(self):
        item_1 = Item.objects.create(text="#1")
        item_2 = Item.objects.create(text="#2")
        item_3 = Item.objects.create(text="#3")

        saved_items = Item.objects.all()

        self.assertIn(item_1, saved_items)
        self.assertIn(item_2, saved_items)
        self.assertIn(item_3, saved_items)

        saved_item_1 = Item.objects.get(pk=1)
        self.assertEqual(item_1.text, saved_item_1.text)


