# 关于类，及面向对象的编程操作。
import random
class VirtualSinger:
    """模拟虚拟歌手"""
    def __init__(self, name, year, color):
        # 方法。这里的int前后必须各是两条下划线。
        """初始化属性name,age,color，代表歌姬（基）们的姓名，年龄，应援的十六进制色号。"""
        self.name = name
        self.year = year
        self.color = color
    def sing(self):
        """模拟唱歌。"""
        print(f"{self.name}正在唱歌。")
        return 0
    def eat(self):
        """模拟进食。"""
        print(f"{self.name}正在进食。")
    def introduce_vsinger(self,name,year,color):
        """模拟Vsinger六位成员的自我介绍。"""
        print(f"大家好，我是Vsinger{name}，于{year}年出道，应援色号是{color}。\n")
        print("我们会为了你唱下去，直到荒芜！")
class Songs(VirtualSinger):
    """模拟虚拟歌手唱的歌曲，选择的背景是2022,2021两年的生日贺曲。"""
    def __init__(self, name, singer, year, color):
        super().__init__(name, year, color)
        self.name = name
        self.singer = singer
        self.year = year
    def introduce(self, name , singer, year):
        print(f"《{name}》是{singer}{year}年的生贺曲。")

Luo_Tianyi = VirtualSinger("洛天依", "2012", '66CCFF')
Yuezheng_Ling = VirtualSinger("乐正绫", "2015", "EE0000")
Yuezheng_Longya = VirtualSinger("乐正龙牙", "2017", "006666")
Yan_He = VirtualSinger("言和", "2013", "99FFFF")
Zhiyu_Moke = VirtualSinger("徵羽摩柯", "2018", "0080FF")
Mo_Qingxian = VirtualSinger("墨清弦", "2018", "FFFF00")
print(Mo_Qingxian.eat())
print(Zhiyu_Moke.sing())
Songs.introduce("self",'心音盒','言和',"2022")
Songs.introduce('Songs','余火','乐正龙牙','2022')
try:
    VirtualSinger.introduce_vsinger(Yuezheng_Ling)
except:
    pass