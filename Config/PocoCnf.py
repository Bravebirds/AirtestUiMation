# -*- coding:utf-8 -*-
#!/usr/bin/env python 3.7
# Python version 2.7.16 or 3.7.6
'''
# FileName： PocoCnf.py.py
# Author : MrYu
# Desc: Poco元素信息
# Date： 2021/2/18 5:29
'''
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

UiConfig={
    "msg": poco(text="消息"),
    "friend": poco(text="朋友"),
    "qq": poco(text="QQ"),
    "qq_zoom": poco(text="QQ空间"),
}