class Restaurant():

    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"餐厅名字是 {self.restaurant_name}")
        print(f"餐厅类型是 {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} 正在营业!")

    def set_number_served(self, served):
        """ 设置就餐人数 """
        if served < 0:
            print('禁止设置为负数')
        else:
            self.number_served = served
        return self.number_served

    def increment_number_served(self, served):
        """ 增加就餐人数 """
        if served < 0:
            print('禁止设置为负数')
        else:
            self.number_served += served
        return self.number_served


restaurant1 = Restaurant('张三餐厅', '川菜')
restaurant1.describe_restaurant()
print('餐馆现在就餐人数{}'.format(restaurant1.set_number_served(10)))
print('餐馆扩容后的就餐人数{}'.format(restaurant1.increment_number_served(10)))
print('-------------------------')

restaurant2 = Restaurant('李四餐厅', '湘菜', 20)
restaurant2.describe_restaurant()
print('餐馆现在就餐人数{}'.format(restaurant2.set_number_served(12)))
print('餐馆扩容后的就餐人数{}'.format(restaurant2.increment_number_served(32)))
print('-------------------------')

restaurant3 = Restaurant('王麻子餐厅', '粤菜', 30)
restaurant3.describe_restaurant()
print('餐馆现在就餐人数{}'.format(restaurant3.set_number_served(54)))
print('餐馆扩容后的就餐人数{}'.format(restaurant3.increment_number_served(105)))
print('-------------------------')