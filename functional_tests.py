import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_item_in_table(self, item):
        pass

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
        input_box.send_keys(item_1)
        input_box.send_keys(Keys.ENTER)
        self.check_item_in_table(item_1)


if __name__ == '__main__':
    unittest.main()

