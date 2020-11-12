#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
list1 = ["a", "b", "c" , "d", ] #列表
# slice1 =  list1[1:4]
# print(slice1)
#
# list1[0] = "abcd" # 修改列表， 把第0个换成 "abcd"
# print(list1)
# 切片赋值
# list1[1:2] = ["e", "f"]
# print(list1)
# 了解下
s1 = slice(1,2)
r = list1[s1]
print(r)

#list函数
s1 = "hello, world"
r1 = list(s1)
r1[0] = "a"
print(list(s1))

print(r1)




