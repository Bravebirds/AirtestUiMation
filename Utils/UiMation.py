# -*- coding:utf-8 -*-
#!/usr/bin/env python 3.7
# Python version 2.7.16 or 3.7.6
'''
# FileName： UiMation.py
# Author : YuYanQing
# Desc: 获取Poco中的元素
# Date： 2021/2/18 2:07
'''

from airtest.core.api import *
from Config import PocoCnf
import BaseSetting
import configparser
config = configparser.ConfigParser() # 类实例化

class ReadConfig():
    def __init__(self):
        """
        初始化配置
        """
        self.config = PocoCnf.UiConfig
        self.globalabs = BaseSetting.GlobalPath()

    def find(self,keyword=None):
        """
        查找配置文件中的元素 为真则返回具体的内容/若无则返回None
        :return:
        """
        return self.config.get(keyword)

    def init_app(self,package=None):
        """
        初始化App
        :return:
        """
        if package == None:
            cfg_path = self.globalabs.cfg_path
            config.read(cfg_path)
            package = config['Poco']['package']
        stop_app(package)
        sleep(1)
        start_app(package)