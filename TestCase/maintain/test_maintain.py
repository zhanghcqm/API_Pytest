#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zhc

import allure,pytest
from Common.Log import Logger
from Api.Maintain import Maintain
from Common.Tools import ConnectMysql
from Conf.Config import Config

data=ConnectMysql()
result=Maintain()
conf=Config()

def setup_module():
    print('------开始执行维护接口用例-----')

def teardown_module():
    print("------设备维护用例执行完毕-----")

class TestMaintain():
    """
    测试维护单增删流程
    """
    log = Logger(logger="TestMaintain").getlog()
    @allure.story("设备维护流程用例")

    @allure.title("维护单生死过程")
    def test_create_maintain(self):
        """
        创建草稿维护单、修改、删除
        """
        with allure.step('创建草稿维护单'):
            self.log.info('------创建维护单接口-----')
            res=result.create_maintan(0,0)
            try:
                self.log.info('创建草稿维护单结果：%s' % res['mesg'])
                maintainId = res['data']
            except Exception as e:
                self.log.error('请求失败：%s' % e)

            assert res['mesg'] == "处理成功"

        with allure.step('更新维护单'):
            self.log.info('------更新维护单接口-----')
            res = result.update_maintan(maintainId,"更新描述",0,1)
            try:
                self.log.info('修改维护单结果：%s' % res['mesg'])
            except Exception as e:
                self.log.error('请求失败：%s' % e)

            assert res['mesg'] == "处理成功"

        with allure.step('删除维护单'):
            self.log.info('------删除维护单接口-----')
            res = result.delete_maintain(maintainId)
            try:
                self.log.info('删除维护单结果：%s' % res['mesg'])
            except Exception as e:
                self.log.error('请求失败：%s' % e)

            assert res['mesg'] == "处理成功"

    @allure.title("查询维护单列表")
    def test_query_maintain(self):
        """
        查询最新创建，查看维护单详情
        """
        with allure.step('查询维护单列表'):
            try:
                res = result.query_maintan_page()
                allure.attach('查询接口请求结果：%s' % res['mesg'])
                self.log.info('查询接口请求结果：%s' % res['mesg'])
                Id = res['data']['records'][0]['id']
            except Exception as e:
                self.log.error('请求失败：%s' % e)
            assert res['mesg'] == "处理成功"

        with allure.step('查看维护单详情'):
            try:
                res = result.get_maintain_detail(Id)
                self.log.info('维护单详情请求结果：%s' % res['mesg'])
            except Exception as e:
                self.log.error('请求失败：%s' % e)
            assert res['data']['id'] == Id

    @allure.title("维护单审批失败后提交")
    def test_audit_maintain(self):
        """
        维护单审批流
        """
        with allure.step('创建维护单并提交'):
            self.log.info('------创建维护单接口-----')
            res=result.create_maintan(1,0)
            try:
                maintainId = res['data']
                self.log.info('创建维护单结果：%s,返回维护单Id:%d' % (res['mesg'],maintainId))
            except Exception as e:
                self.log.error('请求失败：%s' % e)

            assert res['mesg'] == "处理成功"

        with allure.step('拒绝审批维护单'):
            self.log.info('------审批维护单接口-----')
            res=result.audit_maintan(maintainId,300)
            assert res['mesg'] == "处理成功"

        with allure.step('编辑审批失败维护单'):
            self.log.info('------更新维护单接口-----')
            res=result.update_maintan(maintainId,"失败后提交",1,1)
            assert res['mesg'] == "处理成功"
            assert data.sel_maintain(maintainId) == 11

    @allure.title("维护单维护验收流程")
    def test_repair_maintain(self,gen_next_time):
        """
        维护单维护流
        """
        with allure.step('创建维护单并提交'):
            self.log.info('------创建维护单-----')
            res=result.create_maintan(1,0)
            try:
                maintainId = res['data']
                self.log.info('创建维护单结果：%s,返回维护单Id:%d' % (res['mesg'],maintainId))
            except Exception as e:
                self.log.error('请求失败：%s' % e)
            assert res['mesg'] == "处理成功"
            assert data.sel_maintain(maintainId) == 11

        with allure.step('同意审批维护单'):
            self.log.info('------审批维护单-----')
            res=result.audit_maintan(maintainId,400)
            assert res['mesg'] == "处理成功"
            assert data.sel_maintain(maintainId) == 37

        with allure.step('分配维护员'):
            self.log.info('------分配维护员-----')
            res=result.assign_maintan(maintainId,conf.userId)
            assert res['mesg'] == "处理成功"
            assert data.sel_maintain(maintainId) == 38

        with allure.step('开始维护'):
            self.log.info('------接受维护单-----')
            res=result.receive_maintan(maintainId,gen_next_time)
            assert res['mesg'] == "处理成功"
            assert data.sel_maintain(maintainId) == 31

        with allure.step('完成维护'):
            self.log.info('------完成维护单-----')
            res = result.finish_maintan(maintainId)
            assert res['mesg'] == "处理成功"
            assert data.sel_maintain(maintainId) == 35

        with allure.step('验收维护单失败'):
            self.log.info('------验收失败维护单-----')
            res = result.check_maintan(maintainId,2,"验收失败")
            assert res['mesg'] == "处理成功"
            assert data.sel_maintain(maintainId) == 31

        with allure.step('再次完成维护'):
            self.log.info('------再次完成维护单-----')
            res = result.finish_maintan(maintainId)
            assert res['mesg'] == "处理成功"
            assert data.sel_maintain(maintainId) == 35

        with allure.step('验收维护单成功'):
            self.log.info('------验收成功维护单-----')
            res = result.check_maintan(maintainId,1,"")
            assert res['mesg'] == "处理成功"
            assert data.sel_maintain(maintainId) == 32

        with allure.step('查询维护单维护详情'):
            self.log.info('------查看维护单维护记录详情-----')
            res = result.get_records_detail(maintainId)
            assert res['mesg'] == "处理成功"
            assert res['data']['id'] == maintainId



