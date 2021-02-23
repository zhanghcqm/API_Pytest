#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zhc

import pytest
import random,string,datetime
from time import time
"""
fixture里面有个scope参数可以控制fixture的作用范围：session>module>class>function
-function：每一个函数或方法都会调用
-class：每一个类调用一次，一个类中可以有多个方法
-module：每一个.py文件调用一次，该文件内又有多个function和class
-session：是多个文件调用一次，可以跨.py文件调用，每个.py文件就是module
"""
@pytest.fixture(scope="module")
def gen_ran_str():
    """
    随机获取字符串
    :return:
    """
    random_char = string.digits + string.ascii_letters
    gen_char = random.sample(random_char, 4)

    gen_random_str = ''.join(gen_char)
    return gen_random_str

@pytest.fixture(scope="module")
def gen_next_time():
    """
    获取下一整点时间，精确到小时
    :return:
    """
    next_time = (datetime.datetime.now()+datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H") +":00:00"
    return next_time

@pytest.fixture(scope="session")
def time_stamp():
    """
    后获取当前13位时间戳(毫秒)
    :return:
    """
    t = time()
    time_stamp = int(round(t * 1000))
    return time_stamp
