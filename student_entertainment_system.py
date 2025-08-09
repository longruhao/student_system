import time
import random


def print_info():
    print('*' * 39)
    print('-----------欢迎来到学生娱乐系统-----------')
    print('1. 口算游戏')
    print('2. 猜拳游戏')
    print('3. 猜数游戏')
    print('4. 猜质数游戏')
    print('5. 猜斐波那契数游戏')
    print('6. 报数游戏')
    print('7. 杀人游戏')
    print('8. 斗地主发牌')
    print('9. 退出系统')
    print('*' * 39)


def oral_arithmetic():
    def calculator(function, lst):
        result = 0
        if len(lst) == 1:
            result = lst[0]
        while len(lst) > 1:
            result = function(lst.pop(0), lst.pop(0))
            lst.insert(0, result)
        return result

    n = input('请选择您要口算的运算方式: 连加(1), 连减(2), 连乘(3), 连整除(4) => ')
    if n == '1':
        func = lambda x, y: x + y
    elif n == '2':
        func = lambda x, y: x - y
    elif n == '3':
        func = lambda x, y: x * y
    elif n == '4':
        func = lambda x, y: x // y
    else:
        print('您输入的是非法值, 请校验后重新输入!\n')
        return
    num_str = input('请输入您要运算的任意个数字, 数字之间用一个空格隔开, 首尾均不需空格: ')
    num_lst = num_str.split(' ')
    bool_lst = list(map(str.isdigit, num_lst))
    if all(bool_lst):
        answer = input('请输入您的运算结果: ')
        if answer.isdigit():
            num_lst1 = list(map(int, num_lst))
            result = calculator(func, num_lst1)
            result = str(result)
            if answer == result:
                print('恭喜你, 您的答案正确!')
            else:
                print('很遗憾, 您的答案错误')
            if n == '1':
                expr = ' + '.join(num_lst)
            elif n == '2':
                expr = ' - '.join(num_lst)
            elif n == '3':
                expr = ' * '.join(num_lst)
            else:
                expr = ' // '.join(num_lst)
            print(f'{expr} = {result}\n')
        else:
            print('您输入的值不合法, 请校验后重新输入!\n')
    else:
        print('您输入的数字格式或内容不合规则, 请校验后重新输入!\n')


def guess_punch():
    punch_dict = {1: '石头', 2: '剪刀', 3: '布'}
    print('电脑人将随机出拳, 快来pk吧!')
    player = input('请输入您要出的拳: 石头(1), 剪刀(2), 布(3) => ')
    pc = random.randint(1, 3)
    if player in ('1', '2', '3'):
        print(f'电脑人出的拳是 {punch_dict[pc]}')
        if (player == '1' and pc == 2) or (player == '2' and pc == 3) or (player == '3' and pc == 1):
            print('玩家胜!\n')
        elif player == str(pc):
            print('平局!\n')
        else:
            print('电脑人胜!\n')
    else:
        print('您输入的拳不合规则, 请核实后再重新尝试!\n')


def guess_numbers():
    print('电脑随机生成 1 ~ 100 之间的一个数, 快来猜猜看吧!')
    num = random.randint(1, 100)
    while True:
        my_num = input('请输入您要猜的数字: ')
        if my_num.isdigit():
            my_num = int(my_num)
            if num > my_num:
                print('您猜小了!')
            elif num < my_num:
                print('您猜大了!')
            else:
                print('恭喜你, 猜中了!\n')
                break
        else:
            print('您输入的值不合法, 请校验后重新输入!')


def guess_prime_numbers():
    num = input('请输入一个数字, 下面您再给出 1 到该数字之间的质数个数: ')
    answer = input('请给出您的答案: ')
    count = 0
    if num.isdigit() and answer.isdigit():
        num = int(num)
        answer = int(answer)
        for i in range(2, num + 1):
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    break
            else:
                count += 1
                print(i, end="\n" if count % 6 == 0 else "\t")
        print()
        if answer == count:
            print('恭喜你, 您的答案正确!')
        else:
            print('很遗憾, 您的答案错误')
        print(f"1 ~ {num} 之间的质数一共有 {count} 个\n")
    else:
        print('您输入的值不合法, 请校验后重新输入!\n')


def guess_fibonacci_numbers():
    def fib(n):
        if n <= 2:
            return 1
        return fib(n - 1) + fib(n - 2)
    print('斐波那契数列从 1, 1 开始')
    num = input('请输入您要计算的第几个斐波那契数: ')
    answer = input('请输入您的计算答案: ')
    if num.isdigit() and answer.isdigit():
        num = int(num)
        answer = int(answer)
        result = fib(num)
        if answer == result:
            print('恭喜你, 您的答案正确!')
        else:
            print('很遗憾, 您的答案错误')
        print(f'第 {num} 个斐波那契数是 {result}\n')
    else:
        print('您输入的值不合法, 请校验后重新输入!\n')


def report_numbers():
    num = input('请输入要玩报数游戏的人数:')
    multiple = input('请输入要指定跳过哪个数字的倍数或者尾数为哪个数字: ')
    answer = input('请输入您认为的报数人数: ')
    count = 0
    if num.isdigit() and multiple.isdigit() and answer.isdigit() and len(multiple) == 1:
        num = int(num)
        multiple = int(multiple)
        answer = int(answer)
        for i in range(1, num + 1):
            if i % 10 != multiple and i % multiple != 0:
                count += 1
        if answer == count:
            print('恭喜你, 您的答案正确!')
        else:
            print('很遗憾, 您的答案错误')
        print(f'报数的学生一共有 {count} 人\n')
    else:
        print('您输入的值不合法, 请校验后重新输入!\n')


def killing_game():
    num = input('请输入玩游戏的总人数: ')
    kill_num = input('数到哪个数字的倍数就干掉这个人: ')
    answer = input('请输入您认为的幸运数字: ')
    if num.isdigit() and kill_num.isdigit() and answer.isdigit():
        num = int(num)
        kill_num = int(kill_num)
        answer = int(answer)
        nums = list(range(1, num + 1))
        count = 0
        i = 0
        while len(nums) != 1:
            count += 1
            if count % 3 == 0:
                nums.pop(i)
                i -= 1
            if i == len(nums) - 1:
                i = -1
            i += 1
        if answer == nums[0]:
            print('恭喜你, 您的答案正确!')
        else:
            print('很遗憾, 您的答案错误')
        print(f'玩游戏的总人数为 {num}, 幸运数字为 {nums[0]}\n')
    else:
        print('您输入的值不合法, 请校验后重新输入!\n')


def fight_landlord():
    poker_dict = {}
    poker_index = []
    player1 = []
    player2 = []
    player3 = []

    def get_poker():
        nonlocal poker_dict
        num_lst = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']
        color_lst = ['♦', '♣', '♥', '♠']
        poker_list = [i + j for i in num_lst for j in color_lst] + ['小🤡', '大🤡']
        poker_dict = {i: j for i, j in enumerate(poker_list)}

    def shuffle_poker():
        nonlocal poker_index
        poker_index = list(poker_dict.keys())
        random.shuffle(poker_index)

    def send_poker():
        while len(poker_index) > 3:
            player1.append(poker_index.pop())
            player2.append(poker_index.pop())
            player3.append(poker_index.pop())

    def look_poker():
        player1.sort()
        player2.sort()
        player3.sort()
        print('玩家一的牌为:', [poker_dict[i] for i in player1])
        print('玩家二的牌为:', [poker_dict[i] for i in player2])
        print('玩家三的牌为:', [poker_dict[i] for i in player3])
        print('     底牌为:', [poker_dict[i] for i in poker_index], '\n')

    get_poker()
    shuffle_poker()
    send_poker()
    look_poker()


def start_system():
    while True:
        print_info()
        n = input('请输入您要操作的数字: ')
        if n == '1':
            oral_arithmetic()
        elif n == '2':
            guess_punch()
        elif n == '3':
            guess_numbers()
        elif n == '4':
            guess_prime_numbers()
        elif n == '5':
            guess_fibonacci_numbers()
        elif n == '6':
            report_numbers()
        elif n == '7':
            killing_game()
        elif n == '8':
            fight_landlord()
        elif n == '9':
            print('正在退出学生娱乐系统, 期待下次再见!\n')
            time.sleep(2)
            break
        else:
            print('您输入的是非法值, 请校验后重新输入!\n')
