#本程序计算任意自然数立方和。
n = int(input("请输入一个整数n。"))
lifanghe=[]
for values in range(1,n+1):
    lifanghe.append(values*values*values)
print(sum(lifanghe))


#这是另外一个计算两个数之间端点在内所有数立方和的程序。
p = int(input("请输入左端点的数据："))
q = int(input("请输入右端点的数据："))
k:int
for k in range(p, q+1):
    while k <= q:
        A = k**3+p**3
        k=k+1
    print(A)