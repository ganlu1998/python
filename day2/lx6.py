list1 = [1,3,5,7,0,-1,-9,-4,-5,8]
a = 0
b = 0
for i in list1 :
    if i > 0 :
        a = a + 1
    elif i < 0 :
        b = b + 1
print("队列中正数个数" , a)
print("队列中负数个数" , b)
