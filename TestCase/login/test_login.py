#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zhc

import pytest,allure
from Common.Log import Logger
from Common.Tools import ReadYaml
from Api.Login import Login


class TestLogin:
    """
    测试登录接口
    """
    log = Logger(logger="TestLogin").getlog()
    testdata = ReadYaml("login_data.yml").get_yaml_data()  # 读取数据

    @allure.story("登录用例")
    @pytest.mark.parametrize("username,password,expected", testdata["test_login_data"],
                             ids=["正常登录",
                                  "账号错误登录",
                                  "密码错误登录",
                                  "密码为空登录",
                                  "账号为空登录",
                                  "账号存在空格登录",
                                  ])
    def test_login(self,username,password,expected):
        self.log.info('------用户登录接口-----')
        result=Login().login(username,password)
        self.log.info('请求结果：%s' % result)

        assert result == expected

if __name__ == '__main__':
    TestLogin.test_login()


