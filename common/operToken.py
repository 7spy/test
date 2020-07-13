# coding=utf-8 
"""
@Time    : 2020/07/08  下午 14:42
@Author  : wangqn
@FileName: readToken.py
@IDE     : PyCharm
"""
from getRootPath import root_dir
import os

token_file = os.path.join(root_dir, "conf", "tokens")


def write_file(token):
	with open(token_file, "w") as fp:
		fp.write(token)


def read_token():
	with open(token_file) as fp:
		return eval((fp.readlines()[0]))


if __name__ == "__main__":
	#token = "12345"
	#write_file(token)
	print(read_token()["cookie"])

