from car import Car
from battery import Battery


class ElectricCar(Car):
    """ 电动车的独特之处 """

    def __init__(self, make, model, year):
        """
        初始化父类的属性
        经过测试:父类有多少个参数, super这里就必须传入多少个
        默认参数不用
        """
        super().__init__(make, model, year)
        self.battery = Battery()  # 将实例用作属性

    def fill_gas_tank(self):
        """
        重写父类方法
        电动汽车没有油箱
        """
        print("This car doesn't need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
# 电瓶升级
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
