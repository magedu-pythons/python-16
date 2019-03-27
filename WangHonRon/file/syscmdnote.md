### 操作系统常用命令和技巧
 #### [1.linux命令](#1)
 #### [2.windows命令](#2)
 
 
 <h3 id='1'>1.linux命令</h3>
 
 #### 1.1账号管理
 添加账号：命令`]# useradd  username`
 *默认创建用户家目录，权限为700*  
 CentOS默认值会帮创建几个项目：
 - 在/etc/passwd里建立一行与账号相关的数据，包括UID、GID、家目录等；
 - 在/etc/shadow里将此账号的密码相关参数填入，但是尚未有密码；
 - 在/etc/group里加入一个与账号名称一模一样的组名；
 - 在/home底下建立一个与账号同名的目录作为用户家目录，且权限为700
 
 
 <h3 id='2'>2.windows命令</h3>
 
 功能|命令|说明  
 --|:--|:--   
 |运行|win+R|启用运行|   
 |远程|mstsc|启用远程桌面|
 |注册表|regedit|打开注册表编辑器|  
 |系统配置|msconfig|打开系统配置|
 
 