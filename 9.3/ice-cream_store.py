from restaurant import Restaurant


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors, number_served=10):

        super().__init__(restaurant_name, cuisine_type, number_served=0)
        self.flavors = flavors

    def show_flavors(self):
        print(f'{self.restaurant_name}是一家{self.cuisine_type}, 它的口味是{self.flavors}')


ice = IceCreamStand('小小餐厅', '冰淇淋店', '香草', 10)
ice.show_flavors()
