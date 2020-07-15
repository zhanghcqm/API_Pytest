#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2020/6/29 9:25
# @Author: zhc

import pytest,allure
from Common.Log import Logger
from Api.Maintain import Maintain

@allure.story("保养计划流程用例")

class TestMaintain:
    """
    测试保养计划接口
    """
    log = Logger(logger="TestMaintain").getlog()

    def setup_class(self):
        print('------开始执行保养用例-----')

    def teardown_class(self):
        print("------保养用例执行完毕-----")

    @allure.title("默认查询保养计划列表")
    def test_query_maintain(self):
        """
        默认查询
        """
        self.log.info('------获取保养计划列表接口-----')
        result=Maintain().query_maintain_list('')
        try:
            self.log.info('默认查询接口请求结果：%s' % result['mesg'])
        except Exception as e:
            self.log.error('请求失败：%s' % e)

        assert result['mesg'] == "处理成功"

    @allure.title("创建保养计划")
    def test_create_maintain(self,gen_random_string,gen_now_time):
        """
        创建保养计划正向流程
        """
        self.log.info('------创建保养计划接口-----')
        result = Maintain().create_maintain(gen_random_string,gen_now_time,3)
        try:
            self.log.info('创建接口请求结果：%s' % result['mesg'])
        except Exception as e:
            self.log.error('请求失败：%s' % e)

        assert result['mesg'] == "处理成功"

    @allure.title("查询最新创建并删除")
    def test_delete_maintain(self):
        """
        查询最新创建，查看详情并删除该实例
        """
        with allure.step('按计划名查询并提取最新一条'):
            result = Maintain().query_maintain_list("保养计划")
            try:
                self.log.info('查询接口请求结果：%s' % result['mesg'])
            except Exception as e:
                self.log.error('请求失败：%s' % e)

            assert result['mesg'] == "处理成功"

            self.log.info('最新创建的保养计划名为：%s' % result['data']['records'][0]['maintainName'])
            maintainId = result['data']['records'][0]['id']

        with allure.step('查看保养计划详情'):
            self.log.info('获取要查看的计划Id：%s' % maintainId)
            if maintainId:
                self.log.info('------保养计划详情接口-----')
                try:
                    result = Maintain().get_maintain_detail(maintainId)
                    self.log.info('查看计划详情请求结果：%s' % result['mesg'])
                    assert result['data']['id'] == maintainId
                except Exception as e:
                    self.log.error('接口请求失败：%s' % e)
            else:
                self.log.info('保养计划列表为空')

        with allure.step('删除保养计划'):
            result = Maintain().delete_maintain(maintainId)
            try:
                self.log.info('删除接口请求结果：%s' % result['mesg'])
            except Exception as e:
                self.log.error('请求失败：%s' % e)

            assert result['mesg'] == "处理成功"

