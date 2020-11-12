# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
'''
增加一项， gender  : 男
修改 2项 ， 学生编号 -》 002  学生名字 --》 甘露
删除gradeid项，并返回数据
'''
# 字典
stu = {
    "studentNo": "001",
    "studentName": "陈超",
    "phone": "1212312",
    "address": "武汉",
    "bornDate": "2020/9/8",
    "gradeId": 3
}

stu.update(
    {
        "gender": "男",
        "studentNo": "002",
        "studentName": "甘露"

    }

)

value = stu.pop("gradeId")

print("被删除的年级是", value)

print(stu)


