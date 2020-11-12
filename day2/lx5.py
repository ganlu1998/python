'''
练习3：自定义一个函数，求  20 ， 30 ， ‘a’ ,  -1 , 2.34 的平均值。
'''
def avg1(list) :
    sum = 0
    a = 0
    for i in list :
        if type(i) == int:
            a = a + 1
            sum = sum + i;
    b = sum/a
    return b
c = [20,30,'a',-1,2.34]
d = avg1(c)
print(d)