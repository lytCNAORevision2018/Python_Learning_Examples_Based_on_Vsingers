#测试代码
import unittest
from name_function import get_formatted_name
class NamesTestCase(unittest.TestCase):
    """测试！"""
    def test_first_last_name(self):
        formatted_name = get_formatted_name('A','B')
        self.assertEqual(formatted_name,'AB')

print("输入q以退出此程序。")
last :str
first :str
while True:
    first = input("\n请输入名：")
    if first == 'q':
        break
    last = input("\n请输入姓：")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first,last)
    print(formatted_name)
