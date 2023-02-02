import time
start = time.time()
with open('gdbhcx.txt')as file_object:#读取和本py文件处于同一文件夹内的gdbhcx.txt所有的文字。这里用了相对路径。
    contens = file_object.read()
print(contens)
print("14514")
time.sleep(10.0)
with open('gdbhcx.txt')as file_object:
    for line in file_object:
        print(line)#每一行输出。
        #print(line.rstrip())
end = time.time()
print(start -end)
"""写入文件"""
filename = 'gdbhcx.txt'
with open(filename,'a')as file_object_2:
    file_object_2.write('我是四年级学生森下下士。\n')