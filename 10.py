# 两种算法求解鸡兔同笼问题：定义行列式函数计算二阶行列式。
import time
# 开始时间
def determine_2(a,b,c,d):
#此处定义一个求解二阶行列式的函数。
    return ( a * d - b *c )
a = int(input('请输入头的数目。'))
b = int(input('请输入脚的数目。'))
start = time.time()
x = determine_2(a,1,b,4)/determine_2(1,1,2,4)
y = determine_2(1,a,2,b)/determine_2(1,1,2,4)
print(int(x),int(y))
end = time.time()
print("鸡兔同笼问题行列式算法求解总耗时：", end - start)

# 另一种算法：循环无限搜索。
m = int(input('请输入头的数目。'))
n = int(input('请输入脚的数目。'))
start_2 = time.time()
for x_1 in range (1,a+1):
    for y_1 in range(1,a+1):
        if (x_1+y_1 ==m) and(2*x_1+4*y_1 == n):
            print(x_1,y_1)
end_2 = time.time()
print("鸡兔同笼问题循环搜索算法求解总耗时：", end_2 - start_2)

def determine_3(a,b,c,d,e,f,g,h,i):
# 这里真·自己造个轮子，三阶行列式：其中a,b,c;d,e,f;g,h,i分别为从上到下三行，从左到右顺序的诸多元素。
    return (a* (e* i- f* h)- b* (d* i- f* g)+ c* (d * h - e * g))