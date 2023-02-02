class Car:
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odmeter_reading = 0
    def get_descriptive_name(self):
        """返回整齐的描述性信息。"""
        long_name = f"{self.year},{self.make},{self.year}"
        return long_name.title()
    def read_odmeter(self):
        """输出一条显示汽车里程的信息。"""
        print(f"这辆车已经行驶了{self.odmeter_reading}千米。")
    def updating_odmeter(self,mileage):
        """将里程表读数设置为指定的值。"""
        if mileage >= self.odmeter_reading:
            self.odmeter_reading = mileage
        else:
            print("你不能这样设置！")
    def increment_odmeter(self,miles):
        """将里程表读数增加指定的数量。"""
        self.odmeter_reading += miles
class ElectricCar(Car):#子类的定义
    def __init__(self,make,model,year):
        """
        初始化父类的属性，再初始化电动汽车特有的属性。
        """
        super().__init__(make,model,year)
        self.battery_size = 75
    def describe_battery(self):
        """打印一条描述电瓶容量的消息。"""
        print(f"电动汽车的电瓶容量为{self.battery_size}")
# 调用父类
my_used_car = Car('subaru','ouback',2015)
print(my_used_car.get_descriptive_name())

my_used_car.updating_odmeter(114514)
my_used_car.read_odmeter()

my_used_car.increment_odmeter(1919810)
my_used_car.read_odmeter()
# 调用子类
my_tesla = ElectricCar('tesla','model s ',2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()