#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2020/6/24 15:53
# @Author: zhc

import pytest,allure
from Common.Log import Logger
from Api.Assay import Assay

@allure.story("检定计划流程用例")
class TestAssay:
    """
    测试检定计划接口
    """
    log = Logger(logger="TestAssay").getlog()

    def setup_class(self):
        print('------开始执行检定用例-----')

    def teardown_class(self):
        print("------检定用例执行完毕-----")

    @allure.title("默认查询检定计划列表")
    def test_query_assay(self):
        """
        默认查询
        """
        self.log.info('------获取检定计划列表接口-----')
        result=Assay().query_assay_list('')
        self.log.info('默认查询接口请求结果：%s' % result['mesg'])

        assert result['mesg'] == "处理成功"

    @allure.title("创建检定计划")
    def test_create_assay(self,gen_random_string,gen_now_time):
        """
        创建检定计划正向流程
        """
        self.log.info('------创建检定计划接口-----')
        result = Assay().create_assay(gen_random_string,3,gen_now_time,gen_now_time)
        try:
            self.log.info('创建接口请求结果：%s' % result['mesg'])
        except Exception as e:
            self.log.error('请求失败：%s' % e)

        assert result['mesg'] == "处理成功"

    @allure.title("查询最新创建并删除")
    def test_delete_assay(self):
        """
        查询最新创建，查看详情并删除该实例
        """
        with allure.step('按计划名查询并提取最新一条'):
            result = Assay().query_assay_list("检定计划")
            try:
                self.log.info('查询接口请求结果：%s' % result['mesg'])
            except Exception as e:
                self.log.error('请求失败：%s' % e)

            assert result['mesg'] == "处理成功"

            self.log.info('最新创建的检定计划名为：%s' % result['data']['records'][0]['name'])
            assayId = result['data']['records'][0]['id']

        with allure.step('查看检定计划详情'):
            self.log.info('提取到的计划Id：%s' % assayId)
            if assayId:
                self.log.info('------保养计划详情接口-----')
                try:
                    result = Assay().get_assay_detail(assayId)
                    self.log.info('查看计划详情请求结果：%s' % result['mesg'])
                    assert result['data']['id'] == assayId
                except Exception as e:
                    self.log.error('接口请求失败：%s' % e)
            else:
                self.log.info('检定计划列表为空')

        with allure.step('删除检定计划'):
            result = Assay().delete_assay(assayId)
            self.log.info('------删除检定计划接口-----')
            try:
                self.log.info('删除接口请求结果：%s' % result['mesg'])
            except Exception as e:
                self.log.error('请求失败：%s' % e)

            assert result['mesg'] == "处理成功"
