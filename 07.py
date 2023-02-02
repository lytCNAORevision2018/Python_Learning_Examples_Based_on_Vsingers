#字典2
#天钿爆料：以下是洛天依某一周想象中的食谱：（参考资料：千年食谱颂）
food_desiring_1={
    'Monday': "小笼包，叉烧包，奶黄芝麻豆沙包；大肉包，菜包还有灌汤包",
    'Tuesday': "阿绫的麻花辫和呆毛",
    'Wednesday' :'言和的绑腿带',
    'Thursday' :'清弦的反射弧',
    'Friday': '摩柯的帽子',
    'Saturday' :'龙牙的架子鼓鼓棒',
    'Sunday' :'老V的面具'
}
print("以下是洛天依某周的食谱：\n")
for food in food_desiring_1.values():
    print(food.title())

for food in set(food_desiring_1.values()):
    print(food.title())#这里用set表示集合，自动删除重复项。

#字典3：嵌套-小笼包。
xiaolongbao = []
h=int(input("请输入天依每顿饭吃包子的数目。"))
for num_xiaolongbao in range(h):
    new_xiaolongbao = {'status':'fresh','tempreature':'warm'}
    xiaolongbao.append(new_xiaolongbao)
print(f"天依每顿饭吃了{len(xiaolongbao)}个小笼包。")
for xiaolongbao in xiaolongbao [:]:#批量修改。
    if xiaolongbao['status'] == 'fresh':
        xiaolongbao['temperature'] = 'cold'
print(xiaolongbao)