cars =['bmw','audi','toyota','honda','subaru']
print(cars)
cars.sort()#正向排序，永久性。
print(cars)
cars.sort(reverse=True)#据首字母顺序反向排序，永久性。
print(cars)
print("\n Here is a sorted list:")
print(sorted(cars))#使用函数sorted()对列表临时排序。
cars.reverse()#反转着打印列表。
print(cars)

print(len(cars))