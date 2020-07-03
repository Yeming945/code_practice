class User():

    def __init__(self, name, age, height, weight, login_attempts=0):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.login_attempts = login_attempts

    def describe_user(self):
        """ 用户信息 """
        print('用户姓名:{} '.format(self.name))
        print('用户年龄:{} '.format(self.age))
        print('用户身高:{} '.format(self.height))
        print('用户体重:{} '.format(self.weight))

    def greet_user(self):
        """ 欢迎语 """
        print('{}你好, 欢迎回来!'.format(self.name))

    def increment_login_attempts(self):
        """ 记录登录次数 """
        self.login_attempts += 1

    def reset_login_attempts(self):
        """ 重置登录次数 """
        self.login_attempts = 0


if __name__ == "__main__":
    user_a = User('张三', 18, 175, 150)
    user_a.describe_user()
    user_a.greet_user()

    user_a.increment_login_attempts()
    user_a.increment_login_attempts()
    user_a.increment_login_attempts()

    print('用户尝试登录的次数', user_a.login_attempts)
    user_a.reset_login_attempts()
    print('次数清零', user_a.login_attempts)
    print('-----------------------------')
