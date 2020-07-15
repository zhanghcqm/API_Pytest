#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2020/6/24 14:40
# @Author: zhc



from Conf import Config
import requests,json

config = Config.Config()
class Login:
    @staticmethod
    def login(username,password):
        """
        登录认证
        :param username: 用户名
        :param password: 密码
        :return:
        """
        url = config.url + "/authorization-server/oauth/token"
        header = {
            "Authorization": "Basic dGVzdF9jbGllbnQ6dGVzdF9zZWNyZXQ="
        }
        params = {
            "scope": "read",
            "grant_type": "password",
            "username": username,
            "password": password
        }
        re = requests.post(url,params,headers=header)

        try:
            return_type = re.json()["token_type"]
        except:
            print("大兄弟，报错了，你自己看：\n %s" % re.text)
            return_type ='登录失败，请检查参数！'

        return return_type



if __name__ == '__main__':
    s=Login().login('zhcpcsp6','Password888')
    print(s)

