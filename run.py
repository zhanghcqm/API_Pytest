#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author: zhc

"""
运行用例集：
    python run.py
"""

import pytest

from Common.Log import Logger
from Common import Shell
from Conf import Config
from Common.Session import Session

if __name__ == '__main__':
    log = Logger(logger="run").getlog()
    Session().get_token()
    log.info('先登录进行全局token认证')

    conf = Config.Config()
    log.info('初始化配置文件, path=' + conf.conf_path)

    shell = Shell.Shell()
    xml_report_path = conf.xml_report_path
    html_report_path = conf.html_report_path

    # 定义测试集
    args = ['-s', '-q', '--alluredir', xml_report_path,'--clean-alluredir']
    pytest.main(args)

    cmd = 'allure generate %s -o %s --clean' % (xml_report_path, html_report_path)

    try:
        shell.invoke(cmd)
    except Exception:
        log.error('执行用例失败，请检查环境数据')
        raise

    # try:
    #     mail = Email.SendMail()
    #     mail.sendMail()
    # except Exception as e:
    #     log.error('发送邮件失败，请检查邮件配置')
    #     raise

