# -*- coding:utf-8 -*-
# @Author : zhc

from configparser import ConfigParser
import os

class Config:
    path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


    def __init__(self):
        """
        初始化
        """
        self.config = ConfigParser()
        self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
        self.xml_report_path = Config.path_dir + '/Report/xml'
        self.html_report_path = Config.path_dir + '/Report/html'

        if not os.path.exists(self.conf_path):
            raise FileNotFoundError("请确保配置文件存在！")

        self.config.read(self.conf_path, encoding='utf-8')

        self.url = self.get_conf("testServer","url")

        #登录信息
        self.username = self.get_conf("login","username")
        self.password = self.get_conf("login","password")

        #邮箱配置信息
        self.smtpserver=self.get_conf("mail","smtpserver")
        self.sender = self.get_conf("mail","sender")
        self.receiver = self.get_conf("mail","receiver")

        self.user = self.get_conf("mail","username")
        self.passwd = self.get_conf("mail","password")

        #认证信息
        self.token = self.get_conf("identity","token")
        self.userId = self.get_conf("identity", "userId")


    def get_conf(self, title, value):
        """
        配置文件读取
        :param title: 配置组
        :param value: 配置项
        :return:
        """
        return self.config.get(title, value)

    def set_conf(self, title, value, text):
        """
        配置文件修改
        :param title: 配置组
        :param value: 配置项
        :param text: 配置值
        :return:
        """
        self.config.set(title, value, text)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

if __name__=='__main__':
    conf=Config()
