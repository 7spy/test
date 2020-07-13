# coding=utf-8 
"""
@Time    : 2020/07/08  下午 14:42
@Author  : wangqn
@FileName: getRootPath.py
@IDE     : PyCharm
"""
import os

root_dir = os.path.dirname(os.path.abspath(__file__))


if __name__ == "__main__":
    print(root_dir)
    yaml_path = os.path.join(root_dir, "yamlCase", "登录", "登录.yaml")
    print(yaml_path)