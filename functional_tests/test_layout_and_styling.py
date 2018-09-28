# from django.test import LiveServerTestCase
from .base import FunctionalTest


MAX_TIME = 5


class LayoutAndStylingTest(FunctionalTest):
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
