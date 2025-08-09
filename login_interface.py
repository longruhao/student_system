import json
import time
from student_system import data
import student_management_system
import student_entertainment_system


def load_info(filename='data.json'):
    global data, user_list
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            user_list = data['login_data']
    except FileNotFoundError:
        user_list = []


def save_info(filename='data.json'):
    with open(filename, 'w') as f:
        data['login_data'] = user_list
        json.dump(data, f, indent=4)


def print_info():
    print('*' * 36)
    print('-----------欢迎来到学生系统-----------')
    print('1. 登录')
    print('2. 注册')
    print('3. 注销')
    print('4. 退出系统')
    print('*' * 36)


def log_on():
    id = input('请输入您的身份 [管理员/学生] : ')
    if id in ['管理员', '学生']:
        username = input('请输入您的用户名: ')
        for user in user_list:
            if user['name'] == username:
                for i in range(3):
                    password = input('请输入您的密码: ')
                    if user['pwd'] == password:
                        if user['id'] == id:
                            print('登录成功, 正在跳转页面...\n')
                            time.sleep(2)
                            if id == '管理员':
                                student_management_system.start_system()
                                return
                            else:
                                student_entertainment_system.start_system()
                                return
                        else:
                            print('您的身份信息不符, 请校验后重新输入\n')
                            return 
                    else:
                        if i == 2:
                            print('您的账号已锁定, 请联系客服找回密码!\n')
                            return 
                        else:
                            print(f'密码错误, 您还有 {2 - i} 次输入机会')
        else:
            print('该用户名不存在, 请先注册或校验后重新输入!\n')
    else:
        print('您输入的身份不合法, 请校验后重新输入!\n')
            
            
def register():
    id = input('请输入您的身份 [管理员/学生] : ')
    if id in ['管理员', '学生']:
        username = input('请输入您要注册的用户名: ')
        for user in user_list:
            if user['name'] == username:
                print('该用户名已被注册, 请换个名字再试试吧!\n')
                break
        else:
            password = input('请设置您的密码: ')
            user_dict = {'name': username, 'pwd': password, 'id': id}
            user_list.append(user_dict)
            print('注册成功! 欢迎使用学生系统\n')
    else:
        print('您输入的身份不合法, 请校验后重新输入!\n')


def log_off():
    username = input('请输入您要注销的用户名: ')
    for user in user_list:
        if user['name'] == username:
            for i in range(3):
                password = input('请输入您的密码: ')
                if user['pwd'] == password:
                    user_list.remove(user)
                    print('该用户已注销完毕!\n')
                    return
                else:
                    if i == 2:
                        print('您的账号已锁定, 请联系客服找回密码!\n')
                        return
                    else:
                        print(f'密码错误, 您还有 {2 - i} 次输入机会')
    else:
        print('该用户名不存在, 请校验后重新操作!\n')


def start_system():
    load_info()
    while True:
        print_info()
        n = input('请输入您要操作的数字: ')
        if n == '1':
            log_on()
        elif n == '2':
            register()
        elif n == '3':
            log_off()
        elif n == '4':
            save_info()
            break
        else:
            print('您输入的是非法值, 请校验后重新输入!\n')


if __name__ == '__main__':
    start_system()
