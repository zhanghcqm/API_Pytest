# API_Pytest
基于Pytest+request+Allure的接口自动化框架

----
#### 模块类的设计

`Config.py`读取配置文件，包括：不同环境的配置，email相关配置

`Log.py` 封装记录log方法，分为：debug、info、warning、error、critical

`Email.py`封装smtplib方法，运行结果发送邮件通知

`Session.py` 封装获取登录token/cookies方法

`Tools.py` 封装常用工具方法(读取yaml)

`run.py` 核心代码,定义并执行用例集，生成报告

----
