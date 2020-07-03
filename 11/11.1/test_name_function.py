import unittest
from name_function import get_formatted_name

class NameTestClass(unittest.TestCase):
    """ 测试name_function.py """

    def test_first_last_name(self): # 测试方法必须以test_开头, 否则不会自动运行
        """ 能够正确处理像Janis Joplin这样的姓名吗? """
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
        
unittest.main()