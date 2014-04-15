ops
===

ops管理平台

这是一个简单的ops管理平台，使用tornado+python编写。前端html,js,css代码来自互联网，经过少量修改。后端tornado代码完全有我独立编写。

安装指南：

1，所需安装环境，参见requirement.txt

2,下载代码后进行安装：

\# python setup.py install

3，第二步安装后，验证是否成功：
运行如下命令：

\# ops_server

出现如下显示则安装成功：
serve listen port 8888

4，使用supervisor启动程序

\# cp supervisord.conf /etc/

\# supervisord -c /etc/supervisord.conf

注：supervisord.conf配置文件中默认定义了server的监听端口和log路径等信息，有需要的话，可以自行修改。

5，使用ops_server命令启动

\# ops_server -port=8000 -log_file_prefix=/tmp/ops_server.log -logging=info -log_file_max_size=102400 -log_to_stderr=False &
