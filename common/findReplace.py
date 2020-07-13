# coding=utf-8 
"""
@Time    : 2020/07/08  下午 14:42
@Author  : wangqn
@FileName: findReplace.py
@IDE     : PyCharm
"""

import re


def findAndReplace(old, new):
	pattern = re.compile(r'\${(.+?)}')
	it = re.finditer(pattern, old)

	for match in it:
		old = old.replace(match.group(), str(new[match.group(1)]))
	return old


if __name__ == "__main__":
	new = {'projectName': 'q12345656qqq'}
	line = {'assetKind': 'CREDIT', 'projectName': '${projectName}', 'projectType': 'PRO_CONSUMPTION'}
	data = findAndReplace(str(line), new)
	print(data)
	new = {'projectName': 'q12345656'}
	line = {'assetKind': 'CREDIT', 'projectName': 'wqqwqw', 'projectType': 'PRO_CONSUMPTION'}
	data = findAndReplace(str(line), new)
	print(data)





