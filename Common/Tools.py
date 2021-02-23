#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zhc

import os
import yaml,pymysql

class ReadYaml:
    def __init__(self,filename):
        path_ya = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
        self.filepath = path_ya+"/data/"+filename

    def get_yaml_data(self):
        with open(self.filepath, "r", encoding="utf-8")as f:
            return yaml.load(f)

class ConnectMysql:
    @staticmethod
    def sel_deveice(Id):
        """
        用于判断设备状态
        P_DRAFT(10,"草稿"),
        P_WAIT_AUDIT(11,"待审批"),
        P_AUDIT_FAIL(12,"审批失败"),
        P_START(13,"启用"),
        P_STOP(14,"停用"),
        P_DELETED(15,"已删除"),
        :param Id: 设备Id
        :return:
        """
        db = pymysql.connect("192.168.6.60", "root", "swai123456", "zbzk_device")
        cur = db.cursor()
        sql = "select state from device_asset where id = %d" % Id
        try:
            cur.execute(sql)
            db.commit()
        except:
            db.rollback()
        data = cur.fetchone()
        return data[0]

    @staticmethod
    def sel_maintain(Id):
        """
        判断维护单状态
        I_STARTING(31, "进行中"),
        I_COMPLETE(32, "已完成"),
        T_TIME_OUT_COMPLETE(25,"超时完成"),
        I_WAIT_CONFIRM(35,"待验收"),
        I_WAIT_ASSIGN(37,"待分配"),
        I_WAIT_STARTING(38,"待进行"),
        :param Id: 维护单Id
        :return:
        """
        db = pymysql.connect("192.168.6.60", "root", "swai123456", "zbzk_device_repair")
        cur = db.cursor()
        sql = "select state from maintenance_order where id = %d" % Id
        try:
            cur.execute(sql)
            db.commit()
        except:
            db.rollback()
        data = cur.fetchone()
        return data[0]

