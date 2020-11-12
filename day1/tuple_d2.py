#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
# 元组不可变
# test_data = ("a" , "b" , "c" ,"d")
#
# list1 = list(test_data)
# list1[1] = "f"
#
# print(tuple(list1))
list1 = ["语文" , "数学" , "英语"]
list2 = [90, 80, 70]
r = zip(list1, list2)
for i in r:
    print(i)
