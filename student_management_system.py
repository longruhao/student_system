"""
需求:
    1. 先打印提示界面(1-6的数字), 让用户选择他/她要进行的操作
    2. 当用户选择1的时候, 实现操作: 添加学生(学号, 姓名, 手机号)
    3. 当用户选择2的时候, 实现操作: 删除学生(根据学号或者姓名删除)
    4. 当用户选择3的时候, 实现操作: 修改学生信息(只能改姓名, 手机号)
    5. 当用户选择4的时候, 实现操作: 查询单个学生信息(根据学号或者姓名查)
    6. 当用户选择5的时候, 实现操作: 查询所有学生信息
    7. 当用户选择6的时候, 实现操作: 退出系统

思路:
    1. 定义函数 print_info(), 打印提示信息.
    2. 自定义 while True 循环逻辑, 实现: 用户录入什么数据, 就进行相应的操作
        注意: 处理一下非法值
    3. 自定义函数 add_info(), 实现: 添加学生
        学号必须唯一
    4. 自定义函数 delete_info(), 实现: 删除学生
        根据学号删除(唯一)
        根据姓名删除(可重复)
    5. 自定义函数 update_info(), 实现: 修改学生信息
        根据学号修改, 只能修改姓名, 手机号
    6. 自定义函数 search_info(), 实现: 查询某个学生信息
        根据学号查询(唯一)
        根据姓名查询(可重复)
    7. 自定义函数 search_all(), 实现: 查询所有学生的信息

优化思路:
    基本版: 学生管理系统 + 列表嵌套字典
    升级版: 学生管理系统 + 文件
    进阶版: 学生管理系统 + 数据库
    终极版: 登录注册 + 学生管理系统(管理员使用) + 学生娱乐系统(学生使用)

"""
import json
import time
from student_system import data


def load_info(filename='data.json'):
    global data, stu_list
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            if 'student_info' in data:
                stu_list = data['student_info']
            else:
                stu_list = []
    except FileNotFoundError:
        stu_list = []  # 文件不存在时初始化为空列表


def save_info(filename='data.json'):
    with open(filename, 'w') as f:
        data['student_info'] = stu_list
        json.dump(data, f, indent=4)  # indent 参数增加可读性


def print_info():
    print('*' * 39)
    print('-----------欢迎来到学生管理系统-----------')
    print('1. 添加学生')
    print('2. 删除学生')
    print('3. 修改学生信息')
    print('4. 查询单个学生信息')
    print('5. 查询所有学生信息')
    print('6. 退出系统')
    print('*' * 39)


def add_info():
    id = input('请输入您要添加的学生学号: ')
    for d in stu_list:
        if d['id'] == id:
            print(f'学号 {id} 已存在, 请校验后重新输入!')
            break
    else:
        name = input('请输入您要添加的学生姓名: ')
        tel = input('请输入您要添加的学生手机号: ')
        stu_dict = {'id': id, 'name': name, 'tel': tel}
        stu_list.append(stu_dict)
        print(f'学生信息添加成功!')
    print()


def delete_info():
    while True:
        try:
            n = int(input('您要根据学号还是姓名删除, 请输入对应数字 => 1 学号/ 2 姓名: '))
        except ValueError:
            print('您输入的是非法值, 请重新输入!')
        else:
            if n == 1:
                id = input('请输入您要删除的学生学号: ')
                for d in stu_list:
                    if d['id'] == id:
                        stu_list.remove(d)
                        print(f'学号为 {id} 的学生信息已删除!')
                        break
                else:
                    print(f'学号 {id} 不存在, 请校验后重新输入!')
                print()
                break
            elif n == 2:
                name = input('请输入您要删除的学生姓名: ')
                # 定义标记变量flag, 表示: 是否有删除学生, 默认为False(没有删除); True(有删除).
                flag = False
                for d in stu_list[:]:
                    if d['name'] == name:
                        stu_list.remove(d)
                        # 删除学生则修改标记变量的值为True
                        flag = True
                if not flag:
                    print(f'姓名 {name} 不存在, 请校验后重新输入!')
                else:
                    print(f'姓名为 {name} 的学生信息已删除!')
                print()
                break
            else:
                print('您输入的数字不合法, 请校验后重新输入!')


def update_info():
    id = input('请输入您要修改的学生学号: ')
    for d in stu_list:
        if d['id'] == id:
            d['name'] = input('请输入修改后的姓名: ')
            d['tel'] = input('请输入修改后的手机号: ')
            print(f'学号为 {id} 的学生信息已修改!')
            break
    else:
        print(f'学号 {id} 不存在, 请校验后重新输入!')
    print()


def search_info():
    while True:
        try:
            n = int(input('您要根据学号还是姓名查询, 请输入对应数字 => 1 学号/ 2 姓名: '))
        except ValueError:
            print('您输入的是非法值, 请重新输入!')
        else:
            if n == 1:
                id = input('请输入您要查询的学生学号: ')
                for d in stu_list:
                    if d['id'] == id:
                        print(f"学号: {d['id']}, 姓名: {d['name']}, 手机号: {d['tel']}")
                        break
                else:
                    print(f'学号 {id} 不存在, 请校验后重新输入!')
                print()
                break
            elif n == 2:
                name = input('请输入您要查询的学生姓名: ')
                flag = False
                for d in stu_list:
                    if d['name'] == name:
                        print(f"学号: {d['id']}, 姓名: {d['name']}, 手机号: {d['tel']}")
                        flag = True
                if not flag:
                    print(f'姓名 {name} 不存在, 请校验后重新输入!')
                print()
                break
            else:
                print('您输入的数字不合法, 请校验后重新输入!')


def search_all():
    if len(stu_list) == 0:
        print('暂无学生信息, 请添加学生信息后再查询!')
    else:
        for d in stu_list:
            print(f"学号: {d['id']}, 姓名: {d['name']}, 手机号: {d['tel']}")
    print()


def start_system():
    load_info()
    while True:
        print_info()
        try:
            n = int(input('请输入您要操作的数字: '))
        except ValueError:
            print(f'您输入的是非法值, 请重新输入!\n')
        else:
            if n == 1:
                add_info()
            elif n == 2:
                delete_info()
            elif n == 3:
                update_info()
            elif n == 4:
                search_info()
            elif n == 5:
                search_all()
            elif n == 6:
                save_info()
                print('正在退出学生管理系统, 期待下次再见!\n')
                time.sleep(2)
                break
            else:
                print('您输入的数字不合法, 请校验后重新输入!\n')
