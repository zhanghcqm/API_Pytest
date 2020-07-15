#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2020/6/24 14:32
# @Author: zhc

import requests

from Conf import Config

config = Config.Config()
class Maintain:
    def __init__(self):
        self.header = {
            "Authorization": "Bearer " + config.token
        }

    def create_maintain(self,name,startTime,deviceId):
        """
        创建保养计划
        :param name: 计划名称
        :param startTime: 开始时间
        :param deviceId: 设备Id
        :return:
        """
        url = config.url + "/equipment/maintain"
        data = {
            "name": "保养计划"+name,
            "type": 6,
            "level": 2,
            "remark": "自动保养计划",
            "maintainTaskSet": [
                {
                    "key": "cbab4001-cf6d-44ad-ac98-5813f7cd489c",
                    "serialNumber": 1,
                    "createdBy": "system",
                    "createdTime": "2020-03-23",
                    "name": "自动保养项目1",
                    "cycle": 1,
                    "cycleType": 1,
                    "startTime": startTime,
                    "remark": "getenvironment"
                },
                {
                    "key": "77a3a74a-e546-4690-a181-e659fb6db42c",
                    "serialNumber": 2,
                    "createdBy": "system",
                    "createdTime": "2020-03-23",
                    "name": "自动保养项目2",
                    "cycle": 2,
                    "cycleType": "1",
                    "startTime": startTime,
                    "remark": "getenciormne"
                }
            ],
            "deviceId": deviceId,
            "maintainUser": config.userId,
            "status": 1
}
        res = requests.post(url,json=data,headers=self.header)
        return res.json()

    def query_maintain_list(self,name):
        """
        查询保养计划列表
        :param stamp: 当前时间戳
        :param name: 计划名称
        :return:
        """
        url = config.url + "/equipment/maintain/conditions"
        data={
            "current": 1,
            "size": 10,
            "name": name,
            "deviceName": "",
            "groupName": "",
            "maintainUserName": "",
            "startTime": "",
            "endTime": ""
        }
        res = requests.post(url,json=data,headers=self.header)
        return res.json()

    def get_maintain_detail(self,maintainId):
        """
        获取计划详情
        :param maintainId: 计划Id
        :return:
        """
        url = config.url + "/equipment/maintain/{maintainId}".format(maintainId=maintainId)

        res = requests.get(url, headers=self.header)
        return res.json()

    def delete_maintain(self,maintainId):
        """
        删除保养计划
        :param maintainId: 计划Id
        :return:
        """
        url = config.url + "/equipment/maintain/{maintainId}".format(maintainId=maintainId)

        res = requests.delete(url,headers=self.header)
        return res.json()


if __name__ == '__main__':
    maintain=Maintain()
    re=maintain.create_maintain('12','2020-06-29',3)
    print(re,'\n')

