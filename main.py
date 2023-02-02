first_name = 'Tianyi'
last_name = 'Luo'
full_name = f" {first_name} {last_name} "#f字符串
print(full_name.strip())

virtual_singers = ['洛天依','乐正绫','乐正龙牙','徵羽摩柯','言和','墨清弦']#列表
print(virtual_singers)
print(virtual_singers[0].title())#打印列表中的第一个。
print(virtual_singers[-2].title())# 打印列表中的倒数第二个。
message_1=f"最早出道的虚拟歌手是{virtual_singers[0].title()}。"#f 字符串。
print(message_1)
virtual_singers[1]="乐正凤爪"#改变列表中的某个元素。
print(virtual_singers)
virtual_singers.append("初音未来")#向列表中添加某个元素。
virtual_singers[1]='乐正绫'
print(virtual_singers)
virtual_singers.insert(7,'镜音连')# insert 方式插入
virtual_singers.insert(8,'KAITO')
virtual_singers.insert(9,'MEIKO')
virtual_singers.insert(10,'镜音铃')
virtual_singers.insert(11,'巡音流歌')
virtual_singers_2=[virtual_singers[6],virtual_singers[7],virtual_singers[8],virtual_singers[9],virtual_singers[10],virtual_singers[11]]
print(virtual_singers)
del virtual_singers[6]# 删除。
virtual_singers.pop(6)
print(virtual_singers)
virtual_singers.remove('KAITO')
virtual_singers.remove('MEIKO')
virtual_singers.remove('镜音铃')
virtual_singers.remove('巡音流歌')
print(virtual_singers)
print(f"{virtual_singers_2}，是日文虚拟歌手。")
for virtual_singers in virtual_singers:# 使用for循环遍历整个列表
    print(virtual_singers)
    print(f"{virtual_singers.title()},是一个一个优秀的虚拟歌手。\n")

