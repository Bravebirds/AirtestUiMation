# -*- coding:utf-8 -*-
#!/usr/bin/env python 3.7
# Python version 2.7.16 or 3.7.6
'''
# FileName： test_poco.py
# Author : MrYu
# Desc: PyCharm
# Date： 2021/2/18 6:16
'''
from Utils.UiMation import ReadConfig


class TestPoco(ReadConfig):
    def run(self):
        self.init_app()

TestPoco().run()