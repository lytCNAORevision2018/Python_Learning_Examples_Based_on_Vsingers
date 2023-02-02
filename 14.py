unconfinished_classes =['advanced_mathmatics','college_physics','college_English',]#使用while在列表之间移动元素。
finished_classes = []
while unconfinished_classes:
    finished_class = unconfinished_classes.pop()
    finished_classes.append(finished_class)
for classes in finished_classes:
    print(finished_classes)
# 使用用户输入来填充字典。
responses = {}
polling_active = True#设置一个标志，调查是否继续。
while polling_active:
    name = input("请输入你的姓名。")
    response = input("你最喜爱的食物是？")
    responses[name] = response#将回答储存在字典中。
    repeat = input("还有人要参加调查吗？使用是或者否回答。")
    if repeat == "否":
        polling_active = False
for name,response in responses.items():
    print(f"{name}最喜爱的食物是{response}。")