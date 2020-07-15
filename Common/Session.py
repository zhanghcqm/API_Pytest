# -*- coding:utf-8 -*-
# @Time   : 2020/6/18 10:12
# @Author : zhc
"""
封装获取用户token方法

"""
import requests,json

from Common.Log import Logger
from Conf import Config

config = Config.Config()
class Session:
    def __init__(self):
        self.log = Logger(logger="Session").getlog()

    def get_token(self):
        """
        获取token,userId
        :return:
        """
        url = config.url + "/authorization-server/oauth/token"
        header = {
            "Authorization": "Basic dGVzdF9jbGllbnQ6dGVzdF9zZWNyZXQ="
        }
        params = {
            "scope": "read",
            "grant_type": "password",
            "username": config.username,
            "password": config.password
        }
        res = requests.post(url, params, headers=header)

        try:
            token = res.json()["access_token"]
            userId = str(res.json()["userId"])
            self.log.info("get token,useId successfully!")
            config.set_conf("identity", "token", token)
            config.set_conf("identity", "userId", userId)

        except requests.RequestException as e:
            self.log.error("identity failed: "% e)
            token = userId =''

        return token,userId

#
if __name__ == '__main__':
    ss = Session()
    ss.get_token()


