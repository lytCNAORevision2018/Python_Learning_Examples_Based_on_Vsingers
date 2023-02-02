# 算法：Python实现百钱买百鸡。
# 百钱买百鸡原题干：鸡翁一，值钱五；鸡母一，值钱三；鸡雏三，值钱一；百钱买百鸡，则翁、母、雏各几何？
import time
# 开始时间
start = time.time()
# 外层循环控制公鸡数量取值范围：0~20
for x in range(0, 21):
    # 内层循环控制母鸡数量取值范围：0~33
    for y in range(0, 34):
        # 嵌套内层循环控制小鸡数量取值范围：0~100
        for z in range(0, 101):
            # 条件判断同时满足 5x+3y+ z/3== 100 和 x + y + z == 100
            if (x * 5 + y * 3 + z / 3 == 100) and (x + y + z == 100):
                print("公鸡有%d只\t母鸡有%d只\t小鸡有%d只" % (x, y, z))
# 结束时间
end = time.time()
print("算法总耗时：", end - start)