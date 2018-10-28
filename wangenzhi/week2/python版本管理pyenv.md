# Python 版本管理 pyenv

## 前言
Python 程序员在本地进行功能开发后，最终是需要部署到我们的服务器上，而服务器上可能部署了多个程序都会依赖系统上默认安装的 Python 比如（yum命令），目前 CentOS 上默认安装的 Python 版本为 2.7.x 版本。而目前大多数开发的新项目都是使用 Python 3.x 那么如何不影响其它程序又能让新项目使用更高版本的 Python 呢？ pyenv 就是解决这个问题的，使用 pyenv 可以轻松让你在多个 Python 版本之间轻松进行切换。

## 1、安装 pyenv

GitHub：https://github.com/pyenv/pyenv

### 1.1、安装依赖

由于安装 Python 时需要依赖一些其它软件包，所以我们需要将可能会被依赖的软件包预先安装上。

```bash
$ yum -y install git gcc make patch gdbm-devel openssl-devel sqlite-devel readline-devel zlib-devel bzip2-devel
```

### 1.2、创建 python 用户

本着用户权限最小化的原则，我们运行大部分程序都应该有独立的程序用户来避免因使用 root 用户权限过大导致的一些安全问题。

```bash
$ useradd python
```

### 1.3、安装 pyenv

使用 python 用户来安装 pyenv 程序，pyenv 项目中为我们提供了自动安装程序。

项目地址：https://github.com/pyenv/pyenv-installer

```bash
$ su - python  
$ curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
```

安装完成后会提示以下信息：

```bash
# Load pyenv automatically by adding
# the following to ~/.bashrc:

export PATH="/home/python/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

意思添加下面环境变量会自动加载 pyenv，复制下面三行添加到用户家目录下的 .bashrc 文件中：

```bash
$ vim ~/.bashrc
export PATH="/home/python/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

$ source ~/.bashrc
```

## 2、使用 pyenv

### 2.1、获取使用帮助

```bash
python@k8s01-ops-bjqw:~ $ pyenv 
pyenv 1.2.7
Usage: pyenv <command> [<args>]

Some useful pyenv commands are:
   commands    List all available pyenv commands
   local       Set or show the local application-specific Python version
   global      Set or show the global Python version
   shell       Set or show the shell-specific Python version
   install     Install a Python version using python-build
   uninstall   Uninstall a specific Python version
   rehash      Rehash pyenv shims (run this after installing executables)
   version     Show the current Python version and its origin
   versions    List all Python versions available to pyenv
   which       Display the full path to an executable
   whence      List all Python versions that contain the given executable

See `pyenv help <command>' for information on a specific command.
For full documentation, see: https://github.com/pyenv/pyenv#readme
```

获取每个 command 的帮助可以使用 `pyenv help command` 例如，获取 install 的使用方法：

```bash
python@k8s01-ops-bjqw:~ $ pyenv help install
Usage: pyenv install [-f] [-kvp] <version>
       pyenv install [-f] [-kvp] <definition-file>
       pyenv install -l|--list
       pyenv install --version

  -l/--list          List all available versions
  -f/--force         Install even if the version appears to be installed already
  -s/--skip-existing Skip if the version appears to be installed already

  python-build options:

  -k/--keep          Keep source tree in $PYENV_BUILD_ROOT after installation
                     (defaults to $PYENV_ROOT/sources)
  -p/--patch         Apply a patch from stdin before building
  -v/--verbose       Verbose mode: print compilation status to stdout
  --version          Show version of python-build
  -g/--debug         Build a debug version

For detailed information on installing Python versions with
python-build, including a list of environment variables for adjusting
compilation, see: https://github.com/pyenv/pyenv#readme
```

### 2.2、pyenv install 指令

install 指令可以安装指定版本的 Python，使用 `-l` 参数可以获取到可以安装的 Python 版本列表：

```bash
# 安装 Python 3.5.3 版本
python@k8s01-ops-bjqw:~ $ pyenv install 3.5.3 -v

# 安装完成后可以看到如下信息
Collecting setuptools
Collecting pip
Installing collected packages: setuptools, pip
Successfully installed pip-9.0.1 setuptools-28.8.0
Installed Python-3.5.3 to /home/python/.pyenv/versions/3.5.3
```

默认情况下 install 安装时会去 Python 官方下载地址进行下载，如果不想每次都去官方下载，可以提前将 Python 安装程序包下载到本地：

```bash
# 在 ~/.pyenv 目录下创建 cache 目录
python@k8s01-ops-bjqw:~ $ cd ~/.pyenv/
python@k8s01-ops-bjqw:~/.pyenv $ mkdir cache
python@k8s01-ops-bjqw:~/.pyenv $ cd cache/
```

由于 pyenv 程序的原因我们需要将多种 tarball 格式的安装包都下载到 cache 目录中，示例安装 3.6.3 版本的 Python：

```bash
python@k8s01-ops-bjqw:~/.pyenv/cache $ ls
Python-3.6.3.tar.xz  Python-3.6.3.tgz
python@k8s01-ops-bjqw:~/.pyenv/cache $ pyenv install 3.6.3 -v
```

### 2.3、pyenv version & pyenv versions

- version：显示当前正在使用的 Python 版本；
- versions：显示所有可用的Python版本，和当前版本；

```bash
python@k8s01-ops-bjqw:~/.pyenv/cache $ pyenv version
system (set by /home/python/.pyenv/version)
python@k8s01-ops-bjqw:~/.pyenv/cache $ pyenv versions
* system (set by /home/python/.pyenv/version)
  3.5.3
  3.6.3
```

"* system" 表示我们当前使用的 Python 为系统默认的 Python。

### 2.4、pyenv shell 指令

设定当前 shell 使用的版本，影响只作用于当前会话。

```bash
python@k8s01-ops-bjqw:~/.pyenv/cache $ pyenv shell 3.5.3
python@k8s01-ops-bjqw:~/.pyenv/cache $ python -V
Python 3.5.3
python@k8s01-ops-bjqw:~/.pyenv/cache $ pyenv versions
  system
* 3.5.3 (set by PYENV_VERSION environment variable)
  3.6.3
  
# 而在另一个终端我们在查看 Python 版本
python@k8s01-ops-bjqw:~ $ python -V
Python 2.7.5
```

### 2.5、pyenv local 指令

本地设置，可以针对某个项目目录设定 Python 版本。

```bash
python@k8s01-ops-bjqw:~ $ mkdir projects
python@k8s01-ops-bjqw:~ $ cd projects/
python@k8s01-ops-bjqw:~/projects $ pyenv local 3.5.3
python@k8s01-ops-bjqw:~/projects $ python -V
Python 3.5.3
```

而我们在切换到用户家目录 Python 版本还是系统版本：

```bash
python@k8s01-ops-bjqw:~/projects $ cd
python@k8s01-ops-bjqw:~ $ python -V
Python 2.7.5
```

### 2.6、virtualenv 虚拟机

vritrualenv 可以实现 Python 版本管理以及 Python 库隔离。

```bash
# 语法格式
pyenv virtualenv [version] <virtualenv-name>

# 示例对 3.5.3 版本创建一个虚拟机名字为 cmdb-3.5.3
python@k8s01-ops-bjqw:~ $ pyenv virtualenv  3.5.3 cmdb-3.5.3
Requirement already satisfied: setuptools in /home/python/.pyenv/versions/3.5.3/envs/cmdb-3.5.3/lib/python3.5/site-packages
Requirement already satisfied: pip in /home/python/.pyenv/versions/3.5.3/envs/cmdb-3.5.3/lib/python3.5/site-packages
```

查看可用版本

```bash
python@k8s01-ops-bjqw:~ $ pyenv versions
* system (set by /home/python/.python-version)
  3.5.3
  3.5.3/envs/cmdb-3.5.3
  3.6.3
  cmdb-3.5.3
```

本质上 cmdb-3.5.3 是一个软链接，指向 /home/python/.pyenv/versions/3.5.3/envs/cmdb-3.5.3

![-w1209](http://image.codegreen.cn/2018-10-08-15385763486813.jpg)

切换到 cmdb-3.5.3 的版本：

```bash
python@k8s01-ops-bjqw:~ $ pyenv local cmdb-3.5.3
(cmdb-3.5.3) python@k8s01-ops-bjqw:~ $ python -V
Python 3.5.3
```

## 3、pip 包管理工具

类似于 Linux 系统中的 yum 包管理工具，主要用来安装 Python 的包。Python 3.4+ 以上的版本都自带了 pip 工具。

由于国内网络问题，建议使用阿里云提供的 pip 镜像源：

```bash
$ vim ~/.pip/pip.conf
中添加或修改:

[global]
index-url = https://mirrors.aliyun.com/pypi/simple/

[install]
trusted-host=mirrors.aliyun.com
```

### 3.1、pip 常用命令

显示版本和路径

```bash
$ pip -V
```

升级 pip

```bash
$ pip install --upgrade pip
```

安装包

```bash
$ pip install ipython
$ pip install jupyter
```

升级包

```bash
$ pip install --upgrade SomePackage
```

卸载包

```bash
$ pip uninstall ipython
```

列出已经安装的包

```bash
$ pip list
```

显示包信息

```bash
$ pip show ipython
# 显示包的详细信息
$ pip show -f ipython
```

导出当前程序安装的所有依赖包及精确版本号

```bash
$ pip freeze > requirement.txt
```

安装 requirement.txt 依赖

```bash
$ pip install -r requirement.txt 
```

## 4. jupyter 使用

jupyter 是一个开源的程序，可以在 Web 浏览器上编写、运行 Python 代码以及其它编程语言。官方网站介绍了 jupyter 的基本用途。

> The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.

### 4.1 安装 jupyter 

```bash
pip install jupyter
```

### 4.2 运行 jupyter

生成 jupyter 默认配置文件，不然在配置 jupyter 使用密码访问的时候回报错。

```python
$ jupyter notebook --generate-config
```

设置 jupyter 密码用于访问 jupyter 时验证

```bash
$ jupyter notebook password
```

运行 jupyter 

```bash
$ jupyter notebook --ip=0.0.0.0 --no-browser

# --ip= 指定 jupyter 指定服务监听的IP地址
# --no-brower 在启动服务以后不在浏览器中打开一个窗口，默认直接运行 jupyter 时会自动打开一个浏览器窗口。
# --port= 指定 jupyter 服务监听的端口，默认 8888 。
```

运行成功后就可以直接在浏览器中访问 jupyter 啦

![-w1152](http://image.codegreen.cn/2018-10-15-15395948348986.jpg)



