# -*- coding:utf-8 -*-
#!/usr/bin/env python 3.7
# Python version 2.7.16 or 3.7.6
'''
# FileName： BaseSetting.py
# Author : MrYu
# Desc: 基础类
# Date： 2021/2/18 7:22
'''
import  os

class GlobalPath():
    """
    设置路径
    """
    # 程序主路径
    abs_path = os.path.dirname(os.path.abspath(__file__))
    # 用例
    case_path = os.path.join(abs_path, "TestCases")
    # 测试报告
    report_path = os.path.join(abs_path, "Reports")
    # 安装包存储
    apk_path = os.path.join(abs_path, "InstallApk")
    # 架包
    jar_path = os.path.join(abs_path, "Requirements.txt")
    # Config
    cfg_path = os.path.join(abs_path,"Config","config.ini")
