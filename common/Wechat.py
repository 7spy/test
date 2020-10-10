# coding=utf-8
"""
@Time    : 2020/07/23  下午 14:58
@Author  : wangqn
@FileName: Wechat.py
@IDE     : PyCharm
"""
import requests
import json

class WechatAlert():
    def __init__(self,corpid,corpsecret):

        self.url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        self.corpid = corpid
        self.corpsecret = corpsecret

    def get_token(self):
        # 获取token时，携带企业id和secret(注册企业号时，后台可查)
        url = self.url
        values = {'corpid': self.corpid,
                  'corpsecret': self.corpsecret,
                  }
        req = requests.get(url, params=values)
        response = json.loads(req.text)
        # print('response:%s' %response)
        return response["access_token"]

    def send_msg(self, values):
        # 给单个人发送，也可以发送给多个人，但是不是一个群，"touser" : "wangqn","agentid":"1000005",
        url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + self.get_token()
        send_values = {"touser": "wangqn|wangwq|wangsh|wanl",
            "toparty": "",
            "totag": "",
            "msgtype": "text",
            "agentid": "1000005",
            "text": {
                "content": values   # 要推送的内容
            },
            "safe": "0"
        }

        a = requests.post(url, json=send_values)
        a = json.loads(a.text)
        # print(a)


if __name__ == '__main__':
    corpid='wx8d3e67cf49434a0f'
    corpsecret='g4b6P5-QsZAdov-R4Ha7fv1RX26QSLnFEKjMCp4R3HM'
    alert = WechatAlert(corpid,corpsecret)
    alert.send_msg("接口自动化测试已完成，本次报告详情请查看：http://10.0.0.239:8080/examples/report/report.html")
