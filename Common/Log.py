# -*- coding:utf-8 -*-
# @Time   : 2019/2/23 11:05
# @Author : zhc

"""
封装log方法

"""

import logging
import os.path
import time

#log_path是存放日志的路径
cur_path= os.path.dirname(os.path.abspath(__file__))
log_path= os.path.join(os.path.dirname(cur_path),"Log")

class Logger(object):
    def __init__(self, logger):
        """
        指定保存日志的文件路径，日志级别，以及调用文件
        将日志存入到指定的文件中
        :param logger:
        """

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        rq = time.strftime('%Y%m%d', time.localtime(time.time()))
        log_name = os.path.join(log_path,'%s.log'% rq)

        fh = logging.FileHandler(log_name,encoding='utf-8')
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger


