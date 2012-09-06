# -*- coding: utf-8 -*-

"""
所有导入的模块
"""
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtSignature
import socket
import time
import re
from UI_Server import Ui_Form

import sys
reload(sys)
sys.setdefaultencoding('utf-8') #中文化

class Thread1(QtCore.QThread):
    """
    Qt模块下QThread的子类，用于管理socket的连接线程，使发送与接收互不干扰。
    服务端使用该线程1。
    """
    pressed = QtCore.pyqtSignal()
    released = QtCore.pyqtSignal()
    def __init__(self, host, port):
        """
        __init__(self, host, port)
        初始化实例，接收本服务器地址host(等待外网连接需外网地址)和端口port，
        并使用socket模块新建连接。
        """
        super(Thread1, self).__init__()
        self.message = ""
        self.Host = host
        self.Port = port
        self.s = socket.socket() 
        self.s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.s.bind((self.Host,self.Port)) 
        self.s.listen(5)
        
    def run(self):
        """
        run(sef)
        等待客户端连接，并接受消息(<=1kB)
        这里有死循环。
        """
        self.s.listen(5)
        self.con,self.addr = self.s.accept()
        while 1:
            msg = self.con.recv(1024)
            if msg != "":
                self.message = msg
                self.pressed.emit()
            else:
                self.message = self.message
    def sendMsg(self, textMsg):
        """
        sendMsg(self,textMsg)
        向客户端发出消息textMsg。
        """
        self.con.send(textMsg)

def getip():
    """
    getip()
    使用socket模块中的gethostbyname_ex(hostname)函数，
    返回非192开头的ipv4地址，即公网地址，因此要求服务器必须连在公网上。
    """
    names, aliases, ips = socket.gethostbyname_ex(socket.gethostname())
    for ip in ips :
        if not re.match('^192', ip):
            return ip
    return ips[0]

class ServerWidget(QWidget, Ui_Form):
    """
    IM-haha的服务器端的实现类，程序的主要部分。
    """
    def __init__(self, parent = None):
        """
        __init__(self, parent = None)
        初始化UI，关联按钮的信号和槽。
        """
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.yourIP.setText(getip())
        self.pushButton.clicked.connect(self.sendMsg)
        self.pushButton_3.clicked.connect(self.setConnection)

    def setConnection(self):
        """
        setConnection(self)
        实例化Thread1，新建连接，关联Thread1的实例self.th的信号和槽，并报告建立成功。
        """
        self.Host = self.yourIP.displayText()
        self.Port = int(self.yourport.displayText())
        self.th = Thread1(self.Host, self.Port)
        self.th.start()
        QtCore.QObject.connect(self.th, QtCore.SIGNAL("pressed()"), self.display)
        self.textBrowser.append('建立连接在%s : %s'.decode('utf-8') % (self.Host,self.Port))

    def sendMsg(self):
        """
        sendMsg(self)
        用于格式化消息，并发送给客户端。
        可以不定义昵称。
        """
        txt = self.textEdit.toPlainText()
        msg = str(txt).decode('utf-8') 
        name = str(self.yourname.displayText()) if self.yourname.displayText() else self.Host
        name = str(name + ': ').decode('utf-8') 
        nowtime = time.strftime('%H:%M:%S')
        header = name + nowtime + '\n'
        text = header + msg + '\n'
        self.textBrowser.append(text)
        self.th.sendMsg(text)
        self.textEdit.setText("")
        
    def display(self):
        """
        display(self)
        将聊天记录表现在textBrowser部件上。
        """
        self.textBrowser.append((self.th.message).decode('utf-8') ) 
        
if  __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dlg = ServerWidget()
    dlg.show()
    sys.exit(app.exec_())

