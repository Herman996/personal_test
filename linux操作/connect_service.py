# encoding: utf-8
import paramiko
import select
import os
import sys

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
host = "47.107.229.100"
user = "root"
pwd = "aliyun1996874353...A"

class SSH:
    def __init__(self, host, user, pwd, port=22):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.port = port
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(host, username=user, password=pwd, port=port)

    def exec_cmd(self, cmd):
        stdin, stdout, stderr = self.client.exec_command(cmd)
        res, err = stdout.read(), stderr.read()
        result = res if res else err  ##这里我们使用三元运算
        print("##" + result.decode(encoding="utf-8").replace('\n', '', -1) + "##")

    def put_file(self, local_file, service_file):
        tran = paramiko.Transport(self.host, self.port)
        tran.connect(username=self.user, password=self.pwd)
        sftp = paramiko.SFTPClient.from_transport(tran)
        sftp.put(local_file, service_file)
        tran.close()

    def get_file(self, service_file, local_file):
        self.client.get_transport()
        sftp = paramiko.SFTPClient.from_transport(self.client)
        sftp.get(service_file, local_file)


    def c_connect(self):
        channel = self.client.open_session()


    def close_ssh(self):
        self.client.close()



def test():
    import paramiko
    import os
    import select
    import sys
    # 建立一个socket
    trans = paramiko.Transport((host, 22))
    trans.start_client()
    # 如果使用rsa密钥登录的话
    '''

    default_key_file = os.path.join(os.environ['HOME'], '.ssh', 'id_rsa')

    prikey = paramiko.RSAKey.from_private_key_file(default_key_file)

    trans.auth_publickey(username='super', key=prikey)

    '''
    # 如果使用用户名和密码登录
    trans.auth_password(username=user, password=pwd)
    # 打开一个通道
    channel = trans.open_session()
    # 获取终端
    channel.get_pty()
    # 激活终端，这样就可以登录到终端了，就和我们用类似于xshell登录系统一样
    channel.invoke_shell()
    # 下面就可以执行你所有的操作，用select实现
    # 对输入终端sys.stdin和 通道进行监控,
    # 当用户在终端输入命令后，将命令交给channel通道，这个时候sys.stdin就发生变化，select就可以感知
    # channel的发送命令、获取结果过程其实就是一个socket的发送和接受信息的过程

    while True:

        readlist, writelist, errlist = select.select([channel, sys.stdin, ], [], [])    # 如果是用户输入命令了,sys.stdin发生变化
        if sys.stdin in readlist:       # 获取输入的内容
            input_cmd = sys.stdin.read(1)   # 将命令发送给服务器
            channel.sendall(input_cmd)  # 服务器返回了结果,channel通道接受到结果,发生变化 select感知到
        if channel in readlist:     # 获取结果
            result = channel.recv(1024)     # 断开连接后退出
            if len(result) == 0:
                print("\r\n**** EOF **** \r\n")
                break           # 输出到屏幕
    sys.stdout.write(result.decode())
    sys.stdout.flush()      # 关闭通道
    channel.close()         # 关闭链接
    trans.close()


if __name__ == '__main__':
    # put_file()
    ssh = SSH(host, user, pwd)
    # ssh.put_file("easyops.sh", "/tmp/easyops.sh")
    # ssh.exec_cmd("ls /tmp")
    # ssh.exec_cmd("sh /tmp/easyops.sh")
    # ssh.c_connect()
    test()