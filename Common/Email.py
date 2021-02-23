#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zhc

"""
封装发送邮件的方法

"""
import smtplib
import time
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate

from Common.Log import Logger
from Conf.Config import Config

class SendMail:
    def __init__(self):
        self.config = Config()
        self.log = Logger(logger="Email").getlog()

    def sendMail(self):
        msg = MIMEMultipart()

        body = 'Hi,all\n本次接口测试报告如下：'
        mail_msg = MIMEText(body, _subtype='plain', _charset='utf-8')
        tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        msg['Subject'] = Header("接口测试报告"+"_"+tm, 'utf-8')
        msg['From'] = self.config.sender
        receivers = self.config.receiver
        toclause = receivers.split(',')
        msg['To'] = ",".join(toclause)
        msg['Date'] = formatdate()

        msg.attach(mail_msg)

        try:
            smtp = smtplib.SMTP("smtp.ym.163.com", 994,timeout=5)
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(self.config.user, self.config.passwd)
            smtp.sendmail(self.config.sender, toclause, msg.as_string())
            smtp.close()

        except Exception as e:
            self.log.error("邮件发送失败，请检查邮件配置! %s" % e)
        else:
            self.log.info("邮件发送成功")

if __name__ == '__main__':
    res = SendMail()
    res.sendMail()
