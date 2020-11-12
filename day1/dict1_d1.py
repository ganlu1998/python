# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
#字典
stu = {
    "studentNo": "001",
    "studentName": "陈超",
    "phone": "1212312",
    "address": "武汉",
    "bornDate": "2020/9/8",
    "gradeId": 3
}

r = stu.popitem() # 删除，并返回字典最下面一项
print(r)

#print(stu)
