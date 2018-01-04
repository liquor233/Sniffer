# Sniffer

**《计算机通信网基础》课程设计大作业——网络嗅探器<br>
编译环境：Ubuntu16.04<br>**

## requirements.txt

**this is about the required python module**<br>
- python == 2.7.12<br>
- pyqt==4.12.1<br>
- Qt==4.8.7<br>
- sip==4.19.6<br>
- prettytable==0.7.2<br>

## the module of our project

**主要模块**
- sniffer_sqlite: 数据库的建立，使用数据库处理分片重组、报文过滤、信息查找、数据保存<br>
- mainwindow: 程序的主界面（GUI）<br>
- mainDialog: 报文查找和报文过滤弹出的对话框（GUI）<br>
- mthread: 数据包的抓取和存储（使用一个多线程）<br>
- parser: 数据包的解析<br>
- interfaces: 从本地机器上获取网卡列表<br>

> 具体模块关系可查看主目录下的sniffer.png<br>

## headerimg
各种报文的首部图片可以在headerimg文件夹中获取<br>

## 使用方法
### 安装
1. 直接使用bin程序<br>
exe位于目录bin下<br>
使用了Pyinstaller,将我们的项目打包成为了一个exe，可以直接在Ubuntu上使用该exe<br>
因为抓包嗅探需要管理员权限，运行时请加上sudo加以调用<br>
2. 使用python运行source文件夹中的内容<br>
因为Pyinstaller编译出的exe可能存在问题，因此，建议配置环境直接使用python运行程序<br>
项目中使用了第三方依赖库，PyQt4和prettytable，后者可以用pip直接安装，前者可以访问PyQt的官网了解详细配置过程<br>
使用python2.7（需要sudo权限）运行程序的主入口（mainwindow.py），即可调用所需程序<br>
### 使用方法
**页面下部是主要显示界面，可分为:**<br>
- 左下角的报文列表：显示报文简短信息列表，每一行为一条报文信息<br>
- 右下角为报文详细信息显示框：显示报文详细信息，或IP重组之后的报文的全部大报文信息<br>

**页面上部是主要按钮，分为：**<br>

- choose NIC： 一个下拉选框，可以选择网卡，any则表示抓取所有网卡的数据<br>
- begin：点击即开始抓包，会将抓包的简略信息显示在页面左下部的表格中,抓取时除退出/显示详细信息按钮，其余按钮无法使用，再次点击begin按钮（此时显示提示“stop”），可停止抓包<br>
- show detail：在左下角的报文表格中选中一个表项，双击或点击show detail，会显示相关报文的详细信息，包括首部和数据（ASCII码）<br>
- search: 点击该按钮，弹出对话框，输入查找的内容后，会查找含有指定信息的报文显示在左下角的报文列表中<br>
- save: 点击save，弹出文件保存对话框，可以将目前抓取到的报文保存为可读性强的文件<br>
- IpRecombination: 选中报文表格中的相应表项，点击该按钮，可以显示相应报文重组后的整个大报文的详细信息，如果没有分片，显示错误提示<br>
- Filter: 点击该按钮，弹出选择对话框，输入过滤条件（协议类型，源IP，目的IP，源端口，目的端口），端口号用10进制表示，IP4用点分10进制，IP6用冒分16进制表示，如果无过滤条件则缺省，过滤之后符合条件的报文显示在左下角的报文显示列表中
