class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"餐厅名字是 {self.restaurant_name}")
        print(f"餐厅类型是 {self.cuisine_type}")


    def open_restaurant(self):
        print(f"{self.restaurant_name} 正在营业!")
    


restaurant1 = Restaurant('张三餐厅', '川菜')
restaurant1.describe_restaurant()

restaurant2 = Restaurant('李四餐厅', '湘菜')
restaurant2.describe_restaurant()

restaurant3 = Restaurant('王麻子餐厅', '粤菜')
restaurant3.describe_restaurant()

