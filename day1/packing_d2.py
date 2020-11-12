# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
test_data = [20, 30, 90, 100, 110]
# 部分解包
_, *middle, _ = test_data  # middle 变量的类型是列表
print(middle)
# print(sum(middle) / len(middle))
