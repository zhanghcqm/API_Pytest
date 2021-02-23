#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zhc

import requests
from Conf import Config

config = Config.Config()
class Maintain:
    def __init__(self):
        self.header = {
            "Authorization": "Bearer " + config.token
        }

    def create_maintan(self,subCode,haltFlag):
        """
        创建维护单
        :param subCode: 类型 0:存草稿 1:提交审批
        :param haltFlag: 是否停机 0否，1是
        :return:
        """
        url = config.url + "/repair/api/maintenance/save"
        data = {
            "assetId": 1281648358,   #设备id
            "faultDesc": "长剑维护",
            "haltFlag": haltFlag,
            "files": [],
            "subCode": subCode
            }
        res = requests.post(url,json=data,headers=self.header)
        return res.json()

    def update_maintan(self,maintainId,faultDesc,subCode,haltFlag):
        """
        更新维护单
        :param subCode: 类型 0:存草稿 1:提交审批
        :param haltFlag: 是否停机 0否，1是
        :param faultDesc: 维护描述
        :param maintainId: 维护单主键Id，创建返回参数获取
        :return:
        """
        url = config.url + "/repair/api/maintenance/update"
        data = {
            "assetId": 1281648358,   #设备id
            "faultDesc": faultDesc,
            "haltFlag": haltFlag,
            "files": [],
            "subCode": subCode,
            "id":maintainId
            }
        res = requests.put(url,json=data,headers=self.header)
        return res.json()

    def query_maintan_page(self):
        """
        查询维护单列表
        :return:
        """
        url = config.url + "/repair/api/maintenance/query/page"
        res = requests.get(url,headers=self.header)
        return res.json()

    def audit_maintan(self,maintainId,approveStatus):
        """
        审批维护单
        :param maintainId: 维护单主键Id，创建返回参数获取
        :param approveStatus: 审批状态(300审批失败，400审批通过)
        :return:
        """
        url = config.url + "/repair/api/maintenance/audit"
        data = {
            "id": maintainId,
            "approveStatus": approveStatus,
            "remark": "审批"
            }
        res = requests.put(url,json=data,headers=self.header)
        return res.json()

    def assign_maintan(self,maintainId,repUserId):
        """
        分配维护员
        :param repUserId: 维护员Id
        :param maintainId: 维护单主键Id，创建返回参数获取
        :return:
        """
        url = config.url + "/repair/api/maintenance/assign"
        data = {
            "id": maintainId,
            "repUserId": repUserId,
            "repUserName": ""
            }
        res = requests.post(url,json=data,headers=self.header)
        return res.json()

    def receive_maintan(self,maintainId,repExpEndTime):
        """
        接受维护单
        :param repExpEndTime:
        :param maintainId: 维护单主键Id，创建返回参数获取
        :return:
        """
        url = config.url + "/repair/api/maintenance/receive"
        data = {
            "id": maintainId,
            "repExpEndTime": repExpEndTime
            }
        res = requests.post(url,json=data,headers=self.header)
        return res.json()

    def finish_maintan(self,maintainId):
        """
        完成维护
        :param maintainId: 维护单主键Id，创建返回参数获取
        :return:
        """
        url = config.url + "/repair/api/maintenance/finish"
        data = {
            "id": maintainId,
            "repRecordDesc": "维护完成啦",
            "faultType": "故障种类1",
            "faultLevel": "故障等级1",
            "files": [
                {
                    "archivePath": "长剑10维护单",
                    "viewPath": "http://192.168.6.60:9000/dmp-private/2021-01/17948b7a-c609-40d2-91b8-b4256c379e80.jpg"
                }
            ]
        }
        res = requests.post(url,json=data,headers=self.header)
        return res.json()

    def check_maintan(self,maintainId,checkStatus,remark):
        """
        验收维护单
        :param remark: 维护失败原因，失败时填写
        :param checkStatus: 验收状态 1:通过,2:失败
        :param maintainId: 维护单主键Id，创建返回参数获取
        :return:
        """
        url = config.url + "/repair/api/maintenance/check"
        data = {
            "id": maintainId,
            "checkStatus": checkStatus,
            "remark": remark,
        }
        res = requests.post(url,json=data,headers=self.header)
        return res.json()

    def get_maintain_detail(self,maintainId):
        """
        获取维护单详情
        :param maintainId: 维护单主键Id
        :return:
        """
        url = config.url + "/repair/api/maintenance/query/{maintainId}".format(maintainId=maintainId)
        res = requests.get(url,headers=self.header)
        return res.json()

    def get_records_detail(self,maintainId):
        """
        获取维护单维护记录详情
        :param maintainId: 维护单主键Id
        :return:
        """
        url = config.url + "/repair/api/maintenance/queryInfo/{maintainId}".format(maintainId=maintainId)
        res = requests.get(url,headers=self.header)
        return res.json()

    def delete_maintain(self,maintainId):
        """
        删除设备
        :param maintainId: 维护单主键Id
        :return:
        """
        url = config.url + "/repair/api/maintenance/deleteById/{maintainId}".format(maintainId=maintainId)
        res = requests.delete(url,headers=self.header)
        return res.json()

if __name__ == '__main__':
    maintain=Maintain()
    re=maintain.get_maintain_detail(308)
    print(re,'\n')

