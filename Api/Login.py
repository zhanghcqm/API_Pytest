#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zhc



from Conf import Config
import requests,json,base64

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
        authorization=str(base64.b64encode(f'{"test_client"}:{"test_secret"}'.encode('utf-8')), 'utf-8')
        url = config.url + "/authorization-server/oauth/token"
        header = {
            "Authorization": f"Basic {authorization}"
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
    s=Login().login('zhc2','123456')
    print(s)

