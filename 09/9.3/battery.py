class Battery():

    def __init__(self, battery_size=70):
        """ 初始化电瓶的属性 """
        self.battery_size = battery_size

    def describe_battery(self):
        """ 打印一条描述电瓶容量的消息 """
        print("This car has a " + str(self.battery_size) + '-kWh battery.')

    def get_range(self):
        """ 打印一条信息, 指出电瓶的续航里程 """
        if self.battery_size == 70:
            car_range = 240
        elif self.battery_size == 85:
            car_range = 270

        message = "This car can go approximately {}".format(str(car_range))
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """ 电瓶升级 """
        if self.battery_size != 85:
            self.battery_size = 85

