#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2020/6/24 14:00
# @Author: zhc


from Conf import Config
import requests,json

config = Config.Config()
class Assay:
    def __init__(self):
        self.header = {
            "Authorization": "Bearer "+ config.token
        }

    def create_assay(self,name,deviceId,startTime,endTime):
        """
        创建检定计划
        :param name: 计划名称
        :param deviceId: 设备Id
        :param startTime: 开始时间
        :param endTime: 结束时间
        :return:
        """
        url = config.url + "/equipment/assay"
        data = {
            "status": 1,
            "name": "检定计划"+name,
            "remark": "post检定计划",
            "assayUser": config.userId,
            "deviceId": deviceId,
            "startTime": startTime +'00:00:00',
            "endTime": endTime+'23:59:59'
        }
        res = requests.post(url,json=data,headers=self.header)
        return res.json()

    def query_assay_list(self,name):
        """
        查询检定计划列表
        :param name: 计划名称
        :return:
        """
        url = config.url + "/equipment/assay/conditions"

        data={
            "current": 1,
            "size": 10,
            "name": name,
            "deviceName": "",
            "groupName": "",
            "assayUserName": "",
            "status": ""
        }
        res = requests.post(url,json=data,headers=self.header)
        return res.json()


    def get_assay_detail(self,assayId):
        """
        获取计划详情
        :param assayId: 计划Id
        :return:
        """
        url = config.url + "/equipment/assay/{assayId}".format(assayId=assayId)

        res = requests.get(url,headers=self.header)
        return res.json()

    def delete_assay(self,assayId):
        """
        删除检定计划
        :param assayId: 计划Id
        :return:
        """
        url = config.url + "/equipment/assay/{assayId}".format(assayId=assayId)

        res = requests.delete(url,headers=self.header)
        return res.json()


if __name__ == '__main__':
    assay=Assay()
    s=assay.get_assay_detail(135)

    v=assay.query_assay_list('')
    print(s, '\n', v)



