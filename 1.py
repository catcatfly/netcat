from calulation import *


def mode():
    print("=" * 40)
    print("=\t id management system © Copyright \
    \n=login\n=exit\n=indetify\n=change password")
    print("=" * 40)


def modeinput():
    name = input(">>>")
    qq = input(">>>")
    phone_num = input(">>>")
    com_addr = input(">>>")
    print("=" * 40)
    print("name: ", name)
    print("qq: ", qq)
    print("\nphone: ", phone_num)
    print("\ncom: ", com_addr)


"""
tt = ('sad', "sd")
for x in tt:
    print(x)
d = {1: 1, 2: 3}
"""


# sum rang（1，100）
def sum100():
    sum = 0
    for i in range(1, 100):
        sum = i + sum
    return sum


def time3():
    for i in range(1, 100):
        if (i % 3 == 0):
            print(i, end=" ")
    print('\n')


def ninenine():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(i, "*", j, "=", i * j, end=" ")
        print()


def utilzero_exit():
    n = input(">>>")
    while (n != '0'):
        if int(n) < 100:
            print(n)
        n = input(">>>")


def statictime():
    str = "hello world god always busy"
    resoult = {}
    for i in str:
        resoult[i] = str.count(i)
    print(resoult)


def calc(arg1, arg2, sym):
    if sym == '+':
        sum(arg1, arg2)
    else:
        if sym == '-':
            dec(arg1, arg2)
        else:
            if sym == '*':
                mult(arg1, arg2)
            else:
                if sym == '/':
                    divs(arg1, arg2)
                else:
                     if sym == 'e':
                      exit()


print(calc())
# 计算器 接受两个数
# 除数不为零
