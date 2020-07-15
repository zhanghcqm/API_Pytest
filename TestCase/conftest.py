#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2020/6/23 14:02
# @Author: zhc
"""
# @allure.feature # 用于定义被测试的功能，被测产品的需求点
# @allure.story # 用于定义被测功能的用户场景，即子功能点
# @allure.severity #用于定义用例优先级
# @allure.issue #用于定义问题表识，关联标识已有的问题，可为一个url链接地址
# @allure.testcase #用于用例标识，关联标识用例，可为一个url链接地址

# @allure.attach # 用于向测试报告中输入一些附加的信息，通常是一些测试数据信息
# @pytest.allure.step # 用于将一些通用的函数作为测试步骤输出到报告，调用此函数的地方会向报告中输出步骤

"""

import pytest
import random,string
from time import strftime,localtime,time

@pytest.fixture(scope="session")
def gen_random_string():
    """
    随机获取字符串
    :param str_len: 输入需要几位的字符串
    :return:
    """
    random_char = string.digits + string.ascii_letters
    gen_char = random.sample(random_char, 4)

    gen_random_str = ''.join(gen_char)
    return gen_random_str

@pytest.fixture(scope="session")
def gen_now_time():
    """
    获取当前时间，精确到天
    :return:
    """
    now_time = strftime("%Y-%m-%d", localtime())
    return now_time

@pytest.fixture(scope="session")
def time_stamp():
    """
    后获取当前13位时间戳(毫秒)
    :return:
    """
    t = time()
    time_stamp = int(round(t * 1000))
    return time_stamp

