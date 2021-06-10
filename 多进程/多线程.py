# encoding: utf-8
import threading
import os


"""
多线程之间的调度是无序的，由cpu直接调用，线程依赖进程
一个进程至少由一个线程，
线程与进程的对比：
    同样高并发的情况下，使用线程相比与进程占用资源更少
        
"""
def sing(x, y):
    for i in range(x, y):
        print("正在唱歌........{}".format(i))

def dance():
    for i in range(3):
        print("正在跳舞........{}".format(i))


if __name__ == '__main__':
    sing_s = threading.Thread(target=sing, args=(1, 7))
    sing_s1 = threading.Thread(target=sing, kwargs={'x': 1, 'y': 4})
    dance_s = threading.Thread(target=dance)
    sing_s.start()
    dance_s.start()
    sing_s1.start()