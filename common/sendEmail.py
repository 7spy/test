# coding=utf-8 
"""
@Time    : 2018/05/24  下午 12:36
@Author  : hzsyy
@FileName: sendEmail.py
@IDE     : PyCharm
"""

import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


username = '420578354@qq.com'
password = "bwnyklnkmvatcbdi"
sender = username
receivers = ['coin_wangqn@outlook.com']
smtp_server ='smtp.qq.com'

def email(report):

	#创建邮件内容对象
	msg = MIMEMultipart('mixed')
	msg['Subject'] = '接口自动化测试报告'  # 邮件名
	msg['From'] = sender
	msg['To'] = ';'.join(receivers)

	# 设置邮件内容
	html_file = open(report,'rb').read()
	html=MIMEText(html_file,'html','utf-8')

	#发附件需要
#	html["Content-Type"] = 'application/octet-stream'
#	html.add_header('Content-Disposition', 'attachment', filename='接口测试报告.html')
	msg.attach(html)

	try:
		#创建SMTP连接
		client = smtplib.SMTP_SSL(smtp_server,465)
		#设计调试级别
#		client.set_debuglevel(1)

		#登录邮箱
		client.login(username, password)
		#发送邮件
		client.sendmail(sender, receivers, msg.as_string())
		#退出连接
		client.quit()
		print("邮件发送成功，请查看！")


	except smtplib.SMTPException as e:
		print('邮件发送失败，失败原因:',e)




if __name__ == "__main__":
	re=r'E:\freeAutoTest-master\report\2020-04-30 17_43_00测试报告.html'
	email(re)