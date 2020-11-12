'''
优化猜数字游戏
（1）猜错了提示用户，猜打了还是猜小了
（2）用户可以有3次猜的机会
（3）猜玩两次以后提示用户"还有最后一次机会"
（4）使用random模块，里面有一个函数randint()，可产生一个随机数
	a、导入模块
	import random
	b、产生随机数
	key=random.randint(1,10)#参数的意思是产生一个1-10之间的随机数
'''
import random
print("猜数字游戏开始了")
a = random.randint(1,10)
d = 0
while d < 3:
    b = input("请输入你猜的数字：")
    c = int(b)

    if a == c :
        print("恭喜你，猜对了，可惜没有奖励！")
        break
    else:
        print("猜错了")
    d = d + 1
    if d == 2:
        print("你还有一次机会")
    if d == 3:
        print("游戏结束了，不玩了！")
print("正确答案是"  , a)