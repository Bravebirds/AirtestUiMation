# -*- coding:utf-8 -*-
#!/usr/bin/env python 3.7
# Python version 2.7.16 or 3.7.6
'''
# FileName： InitEnviron.py
# Author : YuYanQing
# Desc: 初始化环境
# Date： 2021/2/18 2:07
'''
import os
import BaseSetting

class Start(BaseSetting.GlobalPath):
    def __init__(self):
        """
        初始化路径
        """
        self.set_testcase() # 初始化用例写入及后期读取路径
        self.set_report_path() # 初始化报告存储路径
        self.set_apk_path() # 初始化被测软件包存储路径
        self.install_jar() # 下载架包

    def set_testcase(self):
        """
        创建用例存储路径
        :return:
        """
        if os.path.exists(self.case_path) !=True:
            os.mkdir(self.case_path)
            with open(os.path.join(self.case_path,"该目录用于存放于Case.md"),"w") as file:
                file.close()

    def set_report_path(self):
        """
        创建测试报告存储目录
        :return:
        """
        if os.path.exists(self.report_path) != True:
            os.mkdir(self.report_path)
            with open(os.path.join(self.report_path, "该目录用于存放于测试报告.md"), "w") as file:
                file.close()

    def set_apk_path(self):
        """
        创建测试包存储路径
        :return:
        """
        if os.path.exists(self.apk_path) != True:
            os.mkdir(self.apk_path)
            with open(os.path.join(self.apk_path, "该目录用于存放于测试apk.md"), "w") as file:
                file.close()

    def install_jar(self):
        """
        下载所需的架包
        :return:
        """
        os.system("pip install -r %s"%(self.jar_path))

Start()