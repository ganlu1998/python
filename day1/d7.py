#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang



test_data  = ("hello,world") # 只有字符串类型，没有字符类型
print(type(test_data))
print(test_data[0]) # 索引是整数, 从0开始
print(test_data[-1])
#切片 slice
print(test_data[6:9 + 1])
print(test_data[6:-1])
print(test_data[7:-7]) #注意，保证。起始位置，在 终了位置的左边，否则切出空白
print(test_data[7:]) #注意，保证。起始位置，在 终了位置的左边，否则切出空白
print(test_data[:6]) #注意，保证。起始位置，在 终了位置的左边，否则切出空白




