# from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from unittest import skip

import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException

MAX_TIME = 5


class FunctionalTest(StaticLiveServerTestCase):

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
