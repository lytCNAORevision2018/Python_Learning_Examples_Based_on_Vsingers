# 编写代码验证哥德巴赫猜想对于不大于一万的正整数成立。
# 任意大于2的偶数都可以写成两个整数的和。
import math
import time
def prime(i):  # 定义函数，判断i是否为素数
    if i <= 1:  # 如果小于等于1，返回0（i不是素数）
        return 0
    if i == 2:  # 如果等于2，返回1（i是素数）
        return 1
    for j in range(2, i):  # 判断i是否为素数
        if i % j == 0:  # i可以被j除尽，余数为0
            return 0  # 返回0，i不是素数
        elif i != j + 1:  # 如果i不等于j+1，继续
            continue
        else:
            return 1  # 否则，i等于j+1，返回1（i是素数）
n=0
a = int(input("请输入搜索的下限。"))
b = int(input("请输入搜索的上限。"))
start = time.time()
for i in range(a, b, 2):
    k = 2
    while k <= i/2:
        j = i-k
        flag1 = prime(k)		#调用prime函数
        if flag1:		#如果k为素数
            flag2 = prime(j)	#调用prime函数
            if flag2:		#如果k和j都是素数
                filename = 'gdbhcx.txt'
                try:
                    with open(filename, 'a') as file_object:
                        file_object.write(i=k+j)
                except:
                    pass
                print(i, '=', k, '+', j)#输出结果
                n += 1
        k = k+1
end = time.time()
print("算法总耗时：", end - start)