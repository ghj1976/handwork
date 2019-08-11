# -*- coding: utf-8 -*-    
#内置函数input
# https://jingyan.baidu.com/article/ab69b2709599102ca7189f0b.html
import random
n=int(input('请输入数字'))
#设定一个数字
a=random.randint(1,100)
if n==a:
    print('猜对了')
elif n>a:
    print('大了')
else:
    print('小了')
print('这个数是：',a)