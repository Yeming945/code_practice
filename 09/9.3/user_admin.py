from user import User


class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        for i in self.privileges:
            print('Admin{0}'.format(i))


class Admin(User):

    def __init__(self, name, age, height, weight, login_attempts=0):
        super().__init__(name, age, height, weight, login_attempts=0)
        self.privileges = Privileges()


admin = Admin('张三', 18, 180, 150)
admin.privileges.show_privileges()
