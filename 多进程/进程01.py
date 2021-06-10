# encoding: utf-8
import time
import multiprocessing
import os

"""
进程是同是进行的，cpu会分发内存、磁盘等资源
创建进程，使用multiprocessing模块
创建一个进程对象，使用multiprocessing模块的Process方法，target对应的为函数名
创建进程对象时，为调用的函数传参，在Process方法中还有两个参数:
    - args 以元组的方式向函数中传参,实例（3, ） 这是一个元组，当参数为一个时后面的逗号必须有，多参数时，参数顺序需要与函数中定义的顺序相同
    - kwargs 以字典的方式向函数中传参，实例{'i': 3}，字典中的key需要与函数中的参数变量相同
启动进程，调用进程对象的start()
主进程在所有子进程停止后再停止
通过os模块获取到当前进程号
os.getpid()    获取当前进程的编号
os.getppid()   获取当前进程的父进程编号
"""

def sing(i):
    for i in range(i):
        print("当前跳舞的父进程的pid：{}".format(os.getppid()))
        print("当前唱歌的pid：{}".format(os.getpid()))
        print("唱歌")
        time.sleep(0.5)

def dance(i):
    for i in range(i):
        print("当前跳舞的父进程的pid：{}".format(os.getppid()))
        print("当前跳舞的pid：{}".format(os.getpid()))
        print("跳舞")
        time.sleep(0.5)

if __name__ == '__main__':
    s = multiprocessing.Process(target=sing, args=(3,))
    d = multiprocessing.Process(target=dance, kwargs={'i': 3})
    s.start()
    d.start()

