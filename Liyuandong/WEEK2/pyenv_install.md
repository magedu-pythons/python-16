pyenv install for CentOS 6.5 2.6.32 x86_64

1、更换阿里云yum源
[python@localhost ~]# mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup

[python@localhost ~]# wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-6.repo

2、安装相关依赖包
[python@localhost ~]# yum -y install git

[python@localhost ~]# yum -y install gcc make patch gdbm-devel openssl-devel sqlite-devel readline-devel zlib-devel bzip2-devel

3、添加python用户并设置密码
[python@localhost ~]# useradd python
[python@localhost ~]# passwd python

4、pyenv
# 进入 python用户
[python@localhost ~]# su - python

4.1、 pyenv安装
# 在线安装
[python@localhost ~]$ curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

# 离线安装
[python@localhost ~]$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
[python@localhost ~]$ checkout https://github.com/pyenv/pyenv-doctor.git     ~/.pyenv/plugins/pyenv-doctor
[python@localhost ~]$ checkout https://github.com/pyenv/pyenv-installer.git  ~/.pyenv/plugins/pyenv-installer
[python@localhost ~]$ checkout https://github.com/pyenv/pyenv-update.git     ~/.pyenv/plugins/pyenv-update
[python@localhost ~]$ checkout https://github.com/pyenv/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
[python@localhost ~]$ checkout https://github.com/pyenv/pyenv-which-ext.git  ~/.pyenv/plugins/pyenv-which-ext

# 添加环境变量
[python@localhost ~]$ vi ~/.bashrc
export PATH="/home/python/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

# 使环境变量生效
[python@localhost ~]$ source ~/.bashrc

4.2、 pyenv安装python

# 使用pyenv安装python
# 在线安装
[python@localhost ~]$ pyenv install 3.6.3

# 离线安装
[python@localhost .pyenv]$ cd ~/.pyenv/             # 进入用户家目录的.pyenv目录
[python@localhost .pyenv]$ mkdir cache              # 创建cache目录，用于放python源码包
[python@localhost .pyenv]$ cd cache/                # 进入cache目录并下载python源码包
[python@localhost cache]$ wget https://www.python.org/ftp/python/3.5.3/Python-3.5.3.tar.xz
[python@localhost cache]$ wget https://www.python.org/ftp/python/3.5.3/Python-3.5.3.tgz
[python@localhost cache]$ pyenv install 3.5.3       # 进行离线安装

4.3、pyenv控制python版本

# local