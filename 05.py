# 列表切片
virtual_singers = ['洛天依','乐正绫','乐正龙牙','徵羽摩柯','言和','墨清弦']
print(virtual_singers[-3])#列表倒数第三个
print(virtual_singers[1:4])# 列表中第二个到第五个
for virtual_singers in virtual_singers:
    print(virtual_singers.title())
for virtual_singers in virtual_singers[:-3]:#没有遍历整个列表，只有前三个。
    print(virtual_singers[:3].title())


# 元组
birthdays_of_the_vsingers = (412,520,711,712,1002,1210)
for birthdays_of_the_vsingers in birthdays_of_the_vsingers:
    print(birthdays_of_the_vsingers)