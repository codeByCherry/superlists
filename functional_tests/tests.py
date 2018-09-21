# from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException

MAX_TIME = 5


class NewVisitorTest(StaticLiveServerTestCase):
    def setUp(self):
        web_host = os.environ.get('STAGING_SERVER')
        if web_host:
            self.live_server_url = f'http://{web_host}'

        print()
        print("*"*30)
        print("live_server_url->" + self.live_server_url)
        print("*"*30)
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, item):
        start_time = time.time()
        while True:
            try:

                items = self.browser.find_element_by_id('id_list_table').text
                self.assertIn(item, items)
                break

            except (StaleElementReferenceException,
                    AssertionError,
                    NoSuchElementException,
                    ) as err:
                cost_time = time.time()-start_time
                print('cost time:', cost_time)
                if cost_time >= MAX_TIME:
                    raise err
                else:
                    time.sleep(0.1)

    def input_todo_item(self, item_text):
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys(item_text)
        input_box.send_keys(Keys.ENTER)

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get(self.live_server_url)

        self.assertIn('To-Do', self.browser.title)

        # 断言该页面的 h1 内容含有 'To-Do'
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        input_box = self.browser.find_element_by_id('id_new_item')
        place_holder = input_box.get_attribute('placeholder')
        self.assertEqual(place_holder, "Enter a new item")

        # 在输入框中输入内容
        item_1 = '# item 1'
        self.input_todo_item(item_1)
        self.wait_for_row_in_list_table(item_1)

        # 继续在输入框中输入内容
        item_2 = '# item 2'
        self.input_todo_item(item_2)
        self.wait_for_row_in_list_table(item_1)
        self.wait_for_row_in_list_table(item_2)

    def test_multiple_users_can_start_lists_at_different_urls(self):
        self.browser.get(self.live_server_url)

        # 用户1 输入待办事项
        tony_item1 = "#tony_item1"
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys(tony_item1)
        input_box.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table(tony_item1)

        tony_url = self.browser.current_url
        self.assertRegex(tony_url, '/lists/.+')

        # 现在另外一个用户继续输入内容
        # 断言: 之前用户输入的内容不在该页面显示
        # 断言: 现在的输入显示在该页面中
        # 断言: 两个用户的 url 不同

        # # 为了防止两个用户之间的 cookie 的影响,
        # # 所以关闭了浏览器后，重新开启该浏览器
        self.browser.quit()
        self.browser = webdriver.Firefox()
        self.browser.get(self.live_server_url)

        andy_item1 = "#andy_item1"
        andy_item2 = "#andy_item2"

        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys(andy_item1)
        input_box.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table(andy_item1)

        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys(andy_item2)
        input_box.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table(andy_item2)

        # 断言浏览器的 url 符合 REST 风格
        andy_url = self.browser.current_url
        self.assertRegex(andy_url, '/lists/.+')
        # 断言: 之前用户输入的内容不在该页面显示
        lists_text = self.browser.find_element_by_id('id_list_table').text
        self.assertNotIn(tony_item1, lists_text)
        # 断言: 现在的输入显示在该页面中
        self.wait_for_row_in_list_table(andy_item1)
        self.wait_for_row_in_list_table(andy_item2)
        # 断言: 两个用户的 url 不同
        self.assertNotEqual(tony_url, andy_url)

    def test_layout_and_styling(self):
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # 确定输入框水平居中
        input_from = self.browser.find_element_by_id('id_new_item_form')

        self.assertAlmostEqual(
            input_from.location['x']+input_from.size['width']*0.5,
            512,
            delta=20,
        )
