# -*- coding:utf-8 -*-
#!/usr/bin/env python 3.7
# Python version 2.7.16 or 3.7.6
'''
# FileName： AdbTools.py
# Author : YuYanQing
# Desc: ADB工具类
# Date： 2021/2/18 3:30
'''
from airtest.core.android.adb import ADB

class Manger():
    def __init__(self):
        pass

    def get_devices(self):
        """
        获取设备
        """
        devices = [tmp[0] for tmp in ADB().devices()]
        return devices
