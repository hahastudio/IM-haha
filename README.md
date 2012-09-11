# IM-haha

这是项目 [IM-haha](https://github.com/hahastudio/IM-haha) ，
欢迎访问。

本项目采用Python编写，使用标准库socket进行数据传输，UI使用PyQt库。

主程序分成两部分，一个是`IM-haha-Server.py`，是聊天的服务器端，也是发起者；`IM-haha-Client.py`是客户端，向服务端请求连接许可之后可与服务端聊天。

**很简单的啦= =甚至都没有加密传输**

##编译成二进制文件

**请先确保您安装了Python2.x，PyQt4，Py2exe**

然后在命令提示符（CMD）中执行如下命令：

`python setup-server.py py2exe` #编译`IM-haha-Server.py`

`python setup-client.py py2exe` #编译`IM-haha-Client.py`

##使用说明

* 发起者运行`IM-haha-Server.py`或者`IM-haha-Server.exe`
* 程序会自动识别您的外网IP，如果不对，请自己填写正确的IP
* 填写一个未使用的端口号
* 起一个昵称
* 点击`新建`
* 客户端运行`IM-haha-Client.py`或者`IM-haha-Client.exe`
* 填写服务端的IP与端口，并起一个昵称
* 点击`连接`
* 聊天过程中，在下方输入框内输入内容，之后点击`发送`


## 版本库地址

支持三种访问协议：

* HTTP协议: `https://github.com/hahastudio/IM-haha.git` 。
* Git协议: `git://github.com/hahastudio/IM-haha.git` 。
* SSH协议: `ssh://git@github.com:hahastudio/IM-haha.git` 。

## 克隆版本库

操作示例：

    $ git clone git://github.com/hahastudio/IM-haha.git