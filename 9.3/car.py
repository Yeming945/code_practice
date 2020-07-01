class Car():

    def __init__(self, make, model, year):
        """ 
        :param make: 品牌
        :param model: 型号
        :param year: 出厂年份
        """
        self.make = make  # 品牌
        self.model = model  # 型号
        self.year = year  # 出厂年份
        self.odometer_reading = 0  # 里程表读数
        self.gas_tank = 0

    def get_descriptive_name(self):
        """ 获取车辆信息 """
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """ 读取里程表 """
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        更新里程表 
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """ 将里程表读数增加指定的量 """
        if miles > 0:
            self.odometer_reading += miles
        else:
            print('你不能填写负数')

    def fill_gas_tank(self):
        """ 填充油箱 """
        self.gas_tank = 1
