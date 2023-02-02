#关于函数的参数实验

def describe_vsinger(name):
    '''显示虚拟歌姬的信息。'''
    print(f"\n{name.title()}是我老婆！")
describe_vsinger("洛天依")


def describe_vsinger_2(name,year,color):#函数参数传导实验。
    '''显示虚拟歌姬的信息。'''
    print(f"\n{name.title()}于{year.title()}年出道，应援十六进制色号是{color}。")
describe_vsinger_2("乐正绫","2015","EE0000")
describe_vsinger_2("墨清弦","2018","FFFF00")
describe_vsinger_2("乐正龙牙","2017",color = "006666")
describe_vsinger_2(year ="2018",name="徵羽摩柯",color="0080FF")
describe_vsinger_2('洛天依',year='2012',color="66CCFF")
describe_vsinger_2(color='99FFFF',year="2013",name="言和")

def greet_to_the_vsingers(the_names_of_vsingers):#传递列表。
    for name in the_names_of_vsingers:
        message = f"Hello,{name.title()}"
        print(message)
the_names_of_vsingers = ['洛天依','乐正绫','乐正龙牙','徵羽摩柯','墨清弦','言和']
greet_to_the_vsingers(the_names_of_vsingers)