# 告诉天依你的小秘密——while循环。
prompt = "\n 请告诉天依你的小秘密。保密这些小秘密的价格是十个甚至九个小笼包。"
prompt += "\n 输入'quit'退出程序。"
message = " "
messages = []
while message != 'quit':
    message = input(prompt)
    messages.append(message)
    #print(message)
    if message == 'quit':
        print("我即将泄密，此过程不可逆！！！现在即将对你处刑，三回啊三回！\n")
        messages.remove('quit')
        print(messages)