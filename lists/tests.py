from .models import Item
from .models import List
from .views import UNIQUE_LIST

from django.test import TestCase


class HomePageTest(TestCase):

    def test_root_url_resolve_to_home_page(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/home_page.html')


class ListViewTest(TestCase):

    def test_used_template(self):
        response = self.client.get(UNIQUE_LIST)
        self.assertTemplateUsed(response, 'lists/list.html')

    def test_can_save_a_POST_request(self):
        self.client.post("/lists/new", data={'item_text': "#1"})
        self.assertEqual(Item.objects.count(), 1)
        saved_item = Item.objects.first()
        self.assertEqual(saved_item.text, "#1")

    def test_redirect_after_POST(self):
        response = self.client.post("/lists/new", data={'item_text': '#1'})
        self.assertRedirects(response, UNIQUE_LIST)

    # 用于显示用户列表
    def test_displays_all_list_items(self):
        list1 = List.objects.create()
        item_1 = Item.objects.create(list=list1, text="#1")
        item_2 = Item.objects.create(list=list1, text="#2")
        item_3 = Item.objects.create(list=list1, text="#3")

        response = self.client.get(UNIQUE_LIST)
        self.assertContains(response, item_1.text)
        self.assertContains(response, item_2.text)
        self.assertContains(response, item_3.text)


class NewListTest(TestCase):

    def test_can_save_a_POST_request(self):
        self.client.post('/lists/new', data={'item_text': "#1"})
        self.assertEqual(Item.objects.count(), 1)
        saved_item = Item.objects.first()
        self.assertEqual(saved_item.text, "#1")

    def test_redirect_after_POST(self):
        response = self.client.post('/lists/new', data={'item_text': '#1'})
        self.assertRedirects(response, UNIQUE_LIST)


class ListAndItemModelTest(TestCase):

    def test_save_and_retrieving_items(self):
        list1 = List.objects.create()
        item_1 = Item.objects.create(text="#1", list=list1)
        item_2 = Item.objects.create(text="#2", list=list1)
        item_3 = Item.objects.create(text="#3", list=list1)

        list2 = List.objects.create()
        item_4 = Item.objects.create(text="#4", list=list2)
        item_5 = Item.objects.create(text="#5", list=list2)
        item_6 = Item.objects.create(text="#6", list=list2)

        self.assertEqual(Item.objects.count(), 6)
        self.assertEqual(List.objects.count(), 2)

        self.assertEqual(item_1.list, list1)
        self.assertEqual(item_2.list, list1)
        self.assertEqual(item_3.list, list1)

        self.assertEqual(item_4.list, list2)
        self.assertEqual(item_5.list, list2)
        self.assertEqual(item_6.list, list2)


