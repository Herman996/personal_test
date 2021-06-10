import sys
import threading
import time
import paramiko
import PyQt5
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QTextEdit, QLineEdit, QLabel, QFileDialog, \
    QTextBrowser
from PyQt5.QtGui import QTextCursor

#############################################################################


#############################################################################


port = 22
username = '********'  # 自定义
password = '*********'  # 自定义
rootPassword = '**********'  # 自定义


# 将控制台输出写入文本小部件
class Stream(QObject):
    newText = pyqtSignal(str)

    def write(self, text):
        self.newText.emit(str(text))


class GenMast(QMainWindow):
    def __init__(self):
        super().__init__()
        # QMainWindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.process = QTextEdit(self, readOnly=True)
        self.initUI()

        """自定义输出流"""
        sys.stdout = Stream(newText=self.onUpdateText)

    """将控制台输出写入文本小部件"""

    def onUpdateText(self, text):
        cursor = self.process.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.process.setTextCursor(cursor)
        self.process.ensureCursorVisible()

    def closeEvent(self, event):
        """关闭时关闭应用程序"""
        sys.stdout = sys.__stdout__
        super().closeEvent(event)

    """主界面信息"""

    def initUI(self):
        """ 显示框信息"""
        self.process.ensureCursorVisible()
        self.process.setLineWrapColumnOrWidth(580)
        self.process.setLineWrapMode(QTextEdit.FixedPixelWidth)
        self.process.setFixedWidth(600)
        self.process.setFixedHeight(405)
        self.process.move(290, 10)

        """主窗口"""
        self.setFixedSize(910, 425)
        # self.setGeometry(500, 300, 900, 425)
        self.setWindowTitle('SmartCamera1.1.1.988-huaxia-987')
        self.show()

        """文本：IP地址"""
        self.mqlabel = QLabel('IP地址：', self)
        self.mqlabel.move(40, 5)
        self.mqlabel.show()

        self.line_edit = QLineEdit('192.168.0.6', self)
        self.line_edit.move(90, 10)
        self.line_edit.resize(150, 20)
        self.line_edit.show()

        """文本：命令1"""
        self.cmd1_mqlabel = QLabel('命令1：', self)
        self.cmd1_mqlabel.move(10, 40)
        self.cmd1_mqlabel.show()

        """命令1"""
        self.cmd1 = QLineEdit('cd /home/cloudwalk/SmartCamera', self)
        self.cmd1.move(50, 40)
        self.cmd1.resize(220, 20)
        self.cmd1.show()

        """文本：命令2"""
        self.cmd2_mqlabel = QLabel('命令2：', self)
        self.cmd2_mqlabel.move(10, 60)
        self.cmd2_mqlabel.show()

        """命令2"""
        self.cmd2 = QLineEdit('./stopSmartCamera.sh', self)
        self.cmd2.move(50, 60)
        self.cmd2.resize(220, 20)
        self.cmd2.show()

        """文本：命令3"""
        self.cmd3_mqlabel = QLabel('命令3：', self)
        self.cmd3_mqlabel.move(10, 80)
        self.cmd3_mqlabel.show()

        """命令3"""
        self.cmd3 = QLineEdit('rm /home/cloudwalk/SmartCamera -rf', self)
        self.cmd3.move(50, 80)
        self.cmd3.resize(220, 20)
        self.cmd3.show()

        """文本：命令4"""
        self.cmd4_mqlabel = QLabel('命令4：', self)
        self.cmd4_mqlabel.move(10, 100)
        self.cmd4_mqlabel.show()

        """命令2"""
        self.cmd4 = QLineEdit('cd /home/cloudwalk', self)
        self.cmd4.move(50, 100)
        self.cmd4.resize(220, 20)
        self.cmd4.show()

        """文本：命令5"""
        self.cmd5_mqlabel = QLabel('命令5：', self)
        self.cmd5_mqlabel.move(10, 120)
        self.cmd5_mqlabel.show()

        """命令5"""
        self.cmd5 = QLineEdit('mv SmartCamera1.1.1.988-huaxia-987.tar.gz /usr/local/software/', self)
        self.cmd5.move(50, 120)
        self.cmd5.resize(220, 20)
        self.cmd5.show()

        """文本：命令6"""
        self.cmd6_mqlabel = QLabel('命令6：', self)
        self.cmd6_mqlabel.move(10, 140)
        self.cmd6_mqlabel.show()

        """命令6"""
        self.cmd6 = QLineEdit('rm /home/cloudwalk/SmartCamera1.1.1.987.tar.gz -rf', self)
        self.cmd6.move(50, 140)
        self.cmd6.resize(220, 20)
        self.cmd6.show()

        """文本：命令7"""
        self.cmd7_mqlabel = QLabel('命令7：', self)
        self.cmd7_mqlabel.move(10, 160)
        self.cmd7_mqlabel.show()

        """命令7"""
        self.cmd7 = QLineEdit('', self)
        self.cmd7.move(50, 160)
        self.cmd7.resize(220, 20)
        self.cmd7.show()

        """文本：命令8"""
        self.cmd8_mqlabel = QLabel('命令8：', self)
        self.cmd8_mqlabel.move(10, 180)
        self.cmd8_mqlabel.show()

        """命令8"""
        self.cmd8 = QLineEdit('', self)
        self.cmd8.move(50, 180)
        self.cmd8.resize(220, 20)
        self.cmd8.show()

        """文本：命令9"""
        self.cmd9_mqlabel = QLabel('命令9：', self)
        self.cmd9_mqlabel.move(10, 200)
        self.cmd9_mqlabel.show()

        """命令9"""
        self.cmd9 = QLineEdit('cd /usr/local/software/', self)
        self.cmd9.move(50, 200)
        self.cmd9.resize(220, 20)
        self.cmd9.show()

        """文本：命令10"""
        self.cmd10_mqlabel = QLabel('命令10：', self)
        self.cmd10_mqlabel.move(10, 220)
        self.cmd10_mqlabel.show()

        """命令10"""
        self.cmd10 = QLineEdit('rm /usr/local/software/SmartCamera1.1.1.987.tar.gz -rf', self)
        self.cmd10.move(50, 220)
        self.cmd10.resize(220, 20)
        self.cmd10.show()

        """文本：命令11"""
        self.cmd11_mqlabel = QLabel('命令11：', self)
        self.cmd11_mqlabel.move(10, 240)
        self.cmd11_mqlabel.show()

        """命令11"""
        self.cmd11 = QLineEdit('tar -zxvf SmartCamera1.1.1.988-huaxia-987.tar.gz', self)
        self.cmd11.move(50, 240)
        self.cmd11.resize(220, 20)
        self.cmd11.show()

        """文本：命令12"""
        self.cmd12_mqlabel = QLabel('命令12：', self)
        self.cmd12_mqlabel.move(10, 260)
        self.cmd12_mqlabel.show()

        """命令12"""
        self.cmd12 = QLineEdit('cd /usr/local/software/SmartCamera1_1.1.988/', self)
        self.cmd12.move(50, 260)
        self.cmd12.resize(220, 20)
        self.cmd12.show()

        """文本：命令13"""
        self.cmd13_mqlabel = QLabel('命令13：', self)
        self.cmd13_mqlabel.move(10, 280)
        self.cmd13_mqlabel.show()

        """命令13"""
        self.cmd13 = QLineEdit('./startSmartCamera.sh', self)
        self.cmd13.move(50, 280)
        self.cmd13.resize(220, 20)
        self.cmd13.show()

        """开始"""
        self.btdevices = QPushButton('开始升级', self)
        self.btdevices.move(10, 303)
        self.btdevices.resize(125, 30)
        self.btdevices.show()
        self.btdevices.clicked.connect(self.yuncong)

        """版本校验"""
        self.btversion = QPushButton('版本校验', self)
        self.btversion.move(140, 303)
        self.btversion.resize(130, 30)
        self.btversion.show()
        self.btversion.clicked.connect(self.version)

        # QApplication.processEvents()

        # """启动程序"""
        # btstart = QPushButton('启动程序（请谨慎使用）', self)
        # btstart.move(10, 100)
        # btstart.resize(150, 50)
        # btstart.show()
        # btstart.clicked.connect(self.btstart)

        """选择文件"""
        btfile_path = QPushButton('本地文件', self)
        btfile_path.move(10, 333)
        btfile_path.resize(65, 30)
        btfile_path.show()
        btfile_path.clicked.connect(self.btfile_path)

        """本地路径"""
        self.localpath = QTextBrowser(self)  # QLineEdit
        self.localpath.move(80, 335)
        self.localpath.resize(190, 25)
        self.localpath.show()

        """静态文件：服务器地址"""
        self.fileserver = QLabel('服务器地址:', self)
        self.fileserver.move(10, 360)
        self.fileserver.resize(65, 30)
        self.fileserver.show()

        """服务器路径"""
        self.serverlpath = QLineEdit('/home/cloudwalk/SmartCamera1.1.1.988-huaxia-987.tar.gz', self)
        self.serverlpath.move(80, 360)
        self.serverlpath.resize(190, 25)
        self.serverlpath.show()

        """上传文件"""
        self.upload = QPushButton('远程上传文件', self)
        self.upload.move(140, 385)
        self.upload.resize(130, 30)
        self.upload.show()
        self.upload.clicked.connect(self.uploadserver)

    def myuncong(self, event):
        Cmd1 = self.cmd1.text()
        Cmd2 = self.cmd2.text()
        Cmd3 = self.cmd3.text()
        Cmd4 = self.cmd4.text()
        Cmd5 = self.cmd5.text()
        Cmd6 = self.cmd6.text()
        Cmd7 = self.cmd7.text()
        Cmd8 = self.cmd8.text()
        Cmd9 = self.cmd9.text()
        Cmd10 = self.cmd10.text()
        Cmd11 = self.cmd11.text()
        Cmd12 = self.cmd12.text()
        Cmd13 = self.cmd13.text()
        hostname = self.line_edit.text()
        try:
            print("\n正在连接主机%s……\n" % hostname)
            time.sleep(0.1)
            tran = paramiko.Transport((hostname, port))
            tran.start_client()
            tran.auth_password(username, password)
            chan = tran.open_session()
            # chan.settimeout(10)  # 设置会话超时时间
            chan.get_pty()
            chan.invoke_shell()
            # time.sleep(1)
            print(chan.recv(65535).decode('ascii'), end="")

            print("\n进入系统,获取权限\n")
            time.sleep(0.1)
            chan.send('su\n')
            time.sleep(0.5)
            print(chan.recv(65535).decode('ascii'), end="")
            chan.send(rootPassword + '\n')
            time.sleep(0.5)
            print(chan.recv(65535).decode('ascii'), end="")

            """执行命令1"""
            chan.send(Cmd1 + '\n')
            time.sleep(0.5)
            print(chan.recv(65535).decode('ascii'), end="")
            time.sleep(0.1)

            """执行命令2"""
            chan.send(Cmd2 + '\n')
            time.sleep(0.5)
            print(chan.recv(65535).decode('ascii'), end="")
            time.sleep(0.1)

            """执行命令3"""
            chan.send(Cmd3 + '\n')
            time.sleep(0.5)
            print(chan.recv(65535).decode('ascii'), end="")
            time.sleep(0.1)

            """执行命令4"""
            chan.send(Cmd4 + '\n')
            time.sleep(0.5)
            print(chan.recv(65535).decode('ascii'), end="")
            time.sleep(0.1)

            """执行命令5"""
            chan.send(Cmd5 + '\n')
            time.sleep(0.5)
            print(chan.recv(65535).decode('ascii'), end="")
            time.sleep(0.1)

            """执行命令6"""
            chan.send(Cmd6 + '\n')
            time.sleep(0.5)
            print(chan.recv(65535).decode('ascii'), end="")
            time.sleep(0.1)

            """执行命令7"""
            chan.send(Cmd7 + '\n')
            time.sleep(0.5)
            print(chan.recv(65535).decode('ascii'), end="")
            time.sleep(0.1)

            """执行命令8"""
            chan.send(Cmd8 + '\n')
            time.sleep(0.5)
            print(chan.recv(65535).decode('ascii'), end="")
            time.sleep(0.1)

            """执行命令9"""
            chan.send(Cmd9 + '\n')
            time.sleep(0.5)
            print(chan.recv(65535).decode('ascii'), end="")
            time.sleep(0.1)

            """执行命令10"""
            chan.send(Cmd10 + '\n')
            time.sleep(0.5)
            print(chan.recv(65535).decode('ascii'), end="")
            time.sleep(0.1)

            """执行命令11"""
            chan.send(Cmd11 + '\n')
            line = ''  # 定义line为空的字符串
            while True:
                result = chan.recv(1).decode('ascii')  # 循环检查每一个返回值
                if result == "\n":
                    print(line, end="")
                    # 987: SmartCamera1_1.1.988/disableSmartCamera.sh
                    if "SmartCamera1_1.1.988/restartSmartCamera.sh" in line:
                        time.sleep(1)
                        print("\n\n\n-----------------------------------解压程序完成------------------------------------\n")
                        break

                    else:
                        line = ""
                else:
                    line = line + result

            """执行命令12"""
            print("\n-----------------------------------正在启动程序-----------------------------------\n")
            time.sleep(0.1)
            chan.send(Cmd12 + '\n')
            time.sleep(0.5)
            print(chan.recv(65535).decode('ascii'), end="")

            """执行命令13"""
            chan.send(Cmd13 + '\n')
            line = ''  # 定义line为空的字符串
            while True:
                result = chan.recv(1).decode('ascii')  # 循环检查每一个返回值
                if result == "\n":
                    print(line, end="")
                    if "/lib/systemd/system/broadcastserver.service." in line:
                        time.sleep(1)
                        print("\n\n\n-----------------------------------启动程序完成-----------------------------------\n")
                        break
                    elif "No such file or directory" in line:
                        print("\n\n\n*******************************未知原因，程序启动失败******************************\n")
                        break
                    else:
                        line = ""
                else:
                    line = line + result

            self.btdevices.setEnabled(True)
            tran.close()
        except Exception as e:
            print(e, "\n\n****************************执行错误**************************\n")
            self.btdevices.setEnabled(True)
            print("\n停止脚本\n\n\n")
            return False

    def yuncong(self, event):
        # Tab = self.btdevices.isChecked()
        self.btdevices.setEnabled(False)
        yuncong = threading.Thread(target=self.myuncong, args=(1,))
        yuncong.start()

    def bnstart(self, event):
        pass

    def btstart(self, event):
        btstart = threading.Thread(target=self.bnstart, args=(1,))
        btstart.start()

    def btfile_path(self, event):
        # 选择后缀为.tar.gz的文件或任何文件
        openfilepath = QFileDialog.getOpenFileName(self, "选择文件", "/", "(*.tar.gz)")
        print("本地路径：", openfilepath[0])
        self.localpath.setText(openfilepath[0])  # insert 添加

    def nuploadserver(self, event):
        hostname = self.line_edit.text()
        print("IP地址：", hostname)
        server_path = self.serverlpath.text()
        print("远程路径：", server_path)
        local_path = self.localpath.toPlainText()

        if hostname == '':
            print("请输入IP地址！")
            self.upload.setEnabled(True)
        elif server_path == '':
            print("请输入远程路径和文件命名！")
            self.upload.setEnabled(True)
        elif local_path == '':
            print("请选择本地文件路径！")
            self.upload.setEnabled(True)
        else:
            start = time.time()

            try:

                def calib(*args, **kwargs):
                    # 上传进度
                    result = args[0] / args[1]
                    result2 = result * 100
                    progress = str("%.2f" % result2)

                    # 上传速度
                    end = time.time()
                    timeresult = end - start
                    result3 = args[0] / 1024 / 1027 / round(timeresult)
                    speed = str("%.2f" % result3)
                    self.upload.setText(progress + "%" + "/" + speed + "MB/s")
                    pass

                print("\n开始上传文件到服务器，如文件过大，可能需要等待较长的时间，请耐心等待…………\n")
                tran = paramiko.Transport((hostname, port))
                tran.connect(username=username, password=password)
                sftp = paramiko.SFTPClient.from_transport(tran)
                sftp.put(local_path, server_path, callback=calib)

                tran.close()
                end = time.time()
                result = end - start
                result1 = 1.72 * 1024 / round(result)
                print("\n文件上传成功,耗时%s秒,上传平均速度为%.2fMB/s\n" % (round(result), result1))
                print("\n-----------------------------------上传成功-----------------------------------\n\n")
                self.upload.setEnabled(True)
                self.upload.setText("远程上传文件")
                return True
            except Exception as e:
                print(e, "\n*********************************文件上传错误*********************************\n\n")
                self.upload.setEnabled(True)
                return False

        """
            # sftp传输速度：100M网络上传速度：8Mb/s  1000M网络上传速度：22Mb/s
            # scp传输速度：100M网络上传速度：11Mb/s  1000M网络上传速度：40Mb/s

            try:
                ssh_client = paramiko.SSHClient()
                ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
                ssh_client.connect(hostname, port, username, password)
                scpclient = SCPClient(ssh_client.get_transport())  # socket_timeout=15.0

                print("\n---------------------------------开始上传文件---------------------------------\n")
                print("如文件过大，可能需要等待较长的时间，请耐心等待…………\n")
                scpclient.put(local_path, server_path)
                self.upload.setEnabled(True)

            except FileNotFoundError as e:
                print(e, "\n*********************************文件上传错误*********************************\n\n")
                self.upload.setEnabled(True)
                return False
            else:
                end = time.time()
                result = end - start
                average = 1.72 * 1024 / round(result)
                print("文件上传成功,耗时%s秒,平均速度为%.2fMB/s\n" % (round(result), average))
                print("\n-----------------------------------上传成功-----------------------------------\n\n")
                ssh_client.close()
                return True
            """

    def uploadserver(self, event):
        self.upload.setEnabled(False)
        uploadserver = threading.Thread(target=self.nuploadserver, args=(1,))
        uploadserver.start()

    def mversion(self, event):
        hostname = self.line_edit.text()
        try:
            print("\n----------------------------------------版本校验-------------------------------------\n")
            client = paramiko.SSHClient()  # 绑定实例
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname, port, username, password)  #
            stdin, stdout, stderr = client.exec_command('cat /usr/local/software/SmartCamera/bin/VERSION')  # 执行bash命令
            result = stdout.readline()
            error = stderr.readline()
            # 判断stderr输出是否为空，为空则打印执行结果，不为空打印报错信息
            if not error:
                print("\n版本信息：", result)
                print("-------------------------------------------------------------------------------------\n\n")
            else:
                print("\n错误：", error)
                print("*************************************************************************************\n\n")
            client.close()
        except Exception as e:
            print(e, "\n\n****************************************错误****************************************\n\n")
            return False

    def version(self, event):
        catversion = threading.Thread(target=self.mversion, args=(1,))
        catversion.start()


if __name__ == '__main__':
    """运行应用程序"""
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    gui = GenMast()  # 主程序入口
    sys.exit(app.exec_())

