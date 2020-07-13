# coding=utf-8 
"""
@Time : 2020/07/08  下午 14:42
@Author : wangqn
@FileName : writeLog.py 
@IDE : PyCharm
"""

from common.logger import Log


def writeLog(caseName, url, Data, check,text):
    log = Log()
    log.info("#" * 100 + "开始测试" + "#" * 100)
    log.info("用例名字：{}".format(caseName))
    log.info("请求接口地址：{}".format(url))
    log.info("请求参数：{}".format(Data))
    log.info("-" * 200)
    log.info("期望结果：{}".format(check))
    log.info("实际结果：{}".format(text))
    log.info("#" * 100 + "测试结束" + "#" * 100)