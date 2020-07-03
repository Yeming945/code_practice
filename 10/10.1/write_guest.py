name = input('请输入你的名字: ')

with open('user.txt', 'a', encoding='utf-8') as file_object:
    file_object.write(name)