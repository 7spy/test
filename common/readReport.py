# coding=utf-8 
"""
@Time : 2020/2/28 10:12 
@Author : hzsyy
@FileName : readReport.py 
@IDE : PyCharm
"""
import os
import re


def writeResult(reportPath, writeFile):
    result = {}
    with open(reportPath, "r", encoding='UTF-8') as fp:
        reportContent = fp.read()

    for test in ["testAll", "testPass", "testFail", "testSkip", "beginTime", "totalTime"]:
        value = re.findall("\"%s\": (.+)," % test, reportContent)[0]
        print(value)
        if re.match("\D+", value):
            value = re.findall("\"(.+)\"", value)[0]
            result[test] = value
        result[test] = value

    result["successRate"] = "%.1f" % ((int(result["testPass"]) / int(result["testAll"]))*100)

    with open(writeFile, "w") as my_file:
        for key in result.keys():
            my_file.write(key + "=" + str(result[key]) + "\n")


if __name__ == "__main__":
    if os.sep == "\\":
        reportPath = r"E:\\freeAutoTest-master\\report\\2020-06-24_16_05_56测试报告.html"
        writeFile = r"C:\\Users\\Administrator.WANGQN-PC\\.jenkins\\workspace\\autotest\\my_props.properties"
    else:
        reportPath = r"/report/2020-06-24_16_05_56测试报告.html"
        writeFile = r"/autotest/my_props.properties"

    writeResult(reportPath, writeFile)
