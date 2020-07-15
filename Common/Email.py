#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2019/10/28 10:02
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
from email.utils import formataddr

from Common.Log import Logger
from Conf.Config import Config


class SendMail:

    def __init__(self):
        self.config = Config()
        self.log = Logger(logger="Email").getlog()

    def sendMail(self):
        msg = MIMEMultipart()

        body = 'Hi,all\n本次接口自动化测试报告如下：'
        mail_msg = MIMEText(body, _subtype='plain', _charset='utf-8')
        tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        msg['Subject'] = Header("接口自动化测试报告"+"_"+tm, 'utf-8')     #邮件主题
        msg['From'] = self.config.sender
        receivers = self.config.receiver
        toclause = receivers.split(',')
        msg['To'] = ",".join(toclause)
        msg['Date'] = formatdate()

        msg.attach(mail_msg)

        try:
            smtp = smtplib.SMTP("mail.unicloud.com", 587)  # 发件人邮箱中的SMTP服务器，端口是25
            # server.set_debuglevel(True)
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            # smtp = smtplib.SMTP("mail.unicloud.com",587)    #发件人邮箱中的SMTP服务器，端口587

            smtp.login(self.config.user, self.config.passwd)        #发件人邮箱账号、密码
            smtp.sendmail(self.config.sender, toclause, msg.as_string())  #发件人邮箱账号、收件人邮箱信息、发送邮件
            smtp.close()

        except Exception as e:
            print(e)
            print("发送失败!")
            self.log.error("邮件发送失败，请检查邮件配置")
        else:
            print("发送成功")
            self.log.info("邮件发送成功")


if __name__ == '__main__':
    res = SendMail()
    res.sendMail()
