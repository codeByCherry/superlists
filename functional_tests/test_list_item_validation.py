# from django.test import LiveServerTestCase
from .base import FunctionalTest
from unittest import skip


MAX_TIME = 5


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # 用户访问首页
        self.browser.get(self.live_server_url)
        # 用户没有输入内容，直接按下回车键

        # 首页刷星显示一个错误信息
        # 提示用户输入不能为空

        # 用户再次输入内容，并提交。显示正常

        # 再次提交一个空白事项，显示错误信息，提示用户输入不能为空
        self.fail('Write me!')
