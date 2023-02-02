# 字典1
luo_tianyi = {'color': '66CCFF', 'birthday': '0712'}
yuezheng_ling = {'color': 'EE0000', 'birthday': '0412'}
yuezheng_longya = {'color': '006666', 'birthday': '1002'}
mo_qingxian = {'color': 'FFFF00', 'birthday': '0520'}
zhiyu_moke = {'color': '0080FF', 'birthday': '1210'}
yan_he = {'color': '99FFFF', 'birthday': '0711'}
vsingers_of_henian = [luo_tianyi, yuezheng_ling, yuezheng_longya, mo_qingxian, zhiyu_moke,yan_he]# 定义字典的嵌套。
print(yan_he['color'])# 访问字典中的值。
print(f"徵羽摩柯的应援色号是",zhiyu_moke['color'])
print(vsingers_of_henian)
hatsune_miku = { }# 定义空字典。
hatsune_miku['birthday'] = '0831'
hatsune_miku['color'] ='39C5BB'# 添加键值对
print(hatsune_miku)
print(hatsune_miku['birthday'])
del hatsune_miku['birthday']# 从字典中删除键值对。
print(hatsune_miku)
# 使用get访问字典中的值。
birthday_of_luo_tianyi = luo_tianyi.get('birthday', 'No point value assigned.')
print(birthday_of_luo_tianyi)
works_celebrating_birthday_2022 = {#2022年生贺曲
    '洛天依': '光与影的对白',
    '乐正绫': '未知旅行',
    '乐正龙牙': '余火',
    '言和': '心音盒',
    '徵羽摩柯': '背光处的行星',
    '墨清弦': '白噪'
}
for works_celebrating_birthday_2022 in works_celebrating_birthday_2022.values():
    print(works_celebrating_birthday_2022.values)