# coding=utf-8 
"""
@Time    : 2018/05/28  下午 1:38
@Author  : hzsyy
@FileName: readYaml.py
@IDE     : PyCharm
"""

import yaml
import os
from getRootPath import root_dir


class operYaml:
	def __init__(self, yamlPath):
		self.yamlPath = yamlPath

	def caseList(self):
		with open(self.yamlPath, 'r', encoding='utf-8') as fp:
			contents = fp.read()
			testCase_dict = yaml.safe_load(contents)
			case_list = []
			for caseName, caseInfo in testCase_dict.items():
				new_dict = {}
				new_dict[caseName] = caseInfo
				if caseName == 'method':
					method = caseInfo
				elif caseName == 'uri':
					uri = caseInfo
				else:
					case_list.append(new_dict)
				#print('caseName:',caseName)
				#print('caseInfo:',caseInfo)


			print('case_list:\n', case_list)
			return case_list,method,uri



if __name__ == "__main__":
	yamlPath = os.path.join(root_dir, "yamlCase", "登录", "游客登录.yaml")
	oper_yaml = operYaml(yamlPath)
	case_list,method,uri = oper_yaml.caseList()
	num = 0
	for i in case_list:
		num +=1
		print(i)
	print("共%d条用例" % num)






