# encoding: utf-8
import psutil
import time
import datetime

# print(psutil.cpu_times())
# print(psutil.cpu_count())           # 逻辑cpu个数
# print(psutil.cpu_count(logical=False))      # 物理cpu个数
# print(psutil.cpu_percent())                 # cpu使用率
#
# print(psutil.virtual_memory())
# print(psutil.swap_memory())
# mem = psutil.virtual_memory()
#
# print(psutil.disk_partitions())
# print(psutil.disk_usage('/'))
# print(psutil.disk_io_counters())
#
# print(psutil.net_io_counters())
# print(psutil.net_io_counters(pernic=True))
# print(psutil.net_if_addrs())
# print(psutil.net_if_stats())

print(datetime.datetime.fromtimestamp(psutil.boot_time ()).strftime("%Y-%m-%d %H:%M:%S"))
print(psutil.users())
print(psutil.pids())
pro = psutil.Process(35591)
print(pro.name())
print(pro.uids())
print(pro.username())
print(pro.status())
print(pro.exe())
print(pro.as_dict())
print(pro.cwd())
print(pro.cmdline())
print(pro.ppid())
print(pro.parent())
print(pro.children())
print(pro.cpu_percent())
print(pro.cpu_times())
print(datetime.datetime.fromtimestamp(pro.create_time()).strftime("%Y-%m-%d %H:%M:%S"))
print(pro.memory_info())

print(psutil.test())


def main():
    for i in range(1, 20):
        print(psutil.cpu_percent())                 # cpu使用率
        time.sleep(1)