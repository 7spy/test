# coding=utf-8 
"""
@Time    : 2020/07/08  下午 14:42
@Author  : wangqn
@FileName: run.py
@IDE     : PyCharm
"""
import os
import time
import unittest
from BeautifulReport import BeautifulReport
#from common import sendEmail
from getRootPath import root_dir
#from common import getNewReport
from common import readReport
from common.readConfig import confParam
from common.dataBase import dataBase



def run():
    test_dir = os.path.join(root_dir, "cases")
    reportPath = os.path.join(root_dir, "report")

    dbName = confParam('db')
    db = dataBase(dbName)
    db.update_power("t_user_power", 12805)
    db.update_money("t_user_money", 12805)
    db.delete_money_list("t_user_status", 12805)
    db.closeDb()

    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py', top_level_dir=None)
    print(discover)
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    reportName = now + '测试报告.html'
    description = "python接口自动化测试报告"
    BeautifulReport(discover).report(filename=reportName, description=description, report_dir=reportPath)
    print(discover)


    # 发送邮件(用脚本发邮件，已改成jenkins构建自动发邮件)
    #sendEmail.email(report)

    # tomcat目录从.jenkins目录获取测试报告（windows下拉取测试报告，linux直接用命令拉取）
    #getNewReport.getReport()

    # 读测试报告中的参数，写入邮件模板中
    report = os.path.join(reportPath, reportName)
    writeFile = os.path.join(root_dir, "my_props.properties")
    readReport.writeResult(report, writeFile)


if __name__ == "__main__":
   run()

