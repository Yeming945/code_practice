class User():

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def describe_user(self):
        """ 用户信息 """
        print('用户姓名:{} '.format(self.name))
        print('用户年龄:{} '.format(self.age))
        print('用户身高:{} '.format(self.height))
        print('用户体重:{} '.format(self.weight))

    def greet_user(self):
        """ 欢迎语 """
        print('{}你好, 欢迎回来!'.format(self.name))


user_a = User('张三', 18, 175, 150)
user_a.describe_user()
user_a.greet_user()
print('-----------------------------')

user_b = User('李四', 22, 180, 120)
user_b.describe_user()
user_b.greet_user()
print('-----------------------------')

user_c = User('王麻子', 34, 184, 140)
user_c.describe_user()
user_c.greet_user()
