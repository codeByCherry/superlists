import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException

MAX_TIME = 5


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_item_in_table(self, item):
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
        self.browser.get('http://localhost:8000')
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
        self.check_item_in_table(item_1)

        # 继续在输入框中输入内容
        item_2 = '# item 2'
        self.input_todo_item(item_2)
        self.check_item_in_table(item_1)
        self.check_item_in_table(item_2)


if __name__ == '__main__':
    unittest.main()

