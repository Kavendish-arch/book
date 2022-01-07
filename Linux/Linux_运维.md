1. CentOs7
1. 修改网卡 /etc/sysconfig/
2. yum 安装

# ssh服务安装
1. ssh 安装
2. 公钥私钥

3. 公钥上传
rz
cat id_rsa_2048.pub >> authorized_keys 
vi authorized_keys 
vi /etc/ssh/ssh_config 
systemctl restart sshd


# Cron 计划任务
### 环境

 1. 关闭selinux
```
    sed -i 's/=en
```

## 更改为阿里yum源 
163yum源：
1）备份当前yum源防止出现意外还可以还原回来
cd /etc/yum.repos.d/
cp /CentOS-Base.repo /CentOS-Base-repo.bak
2）使用wget下载163yum源repo文件
wget http://mirrors.163.com/.help/CentOS7-Base-163.repo
3) 清理旧包
yum clean all
4）把下载下来163repo文件设置成为默认源
mv CentOS7-Base-163.repo CentOS-Base.repo
5）生成163yum源缓存并更新yum源
yum makecache
yum update

阿里云yum源：
1）备份当前yum源防止出现意外还可以还原回来
cd /etc/yum.repos.d/
cp /CentOS-Base.repo /CentOS-Base-repo.bak
2）使用wget下载阿里yum源repo文件
wget http://mirrors.aliyun.com/repo/Centos-7.repo
3) 清理旧包
yum clean all
4）把下载下来阿里云repo文件设置成为默认源
mv Centos-7.repo CentOS-Base.repo
5）生成阿里云yum源缓存并更新yum源
yum makecache
yum update

3. 优化ssh远程登录
4. 历史记录数及登录超时环境变量配置
5. 优化Linux描述符
6. 定时清理邮件服务器的临时目录
7. 内核优化
8. 常用软件安装

### xShell xFtp

## 计划任务

#### 一次性计划任务 at 
一次性计划任务只执行一次，一般用于满足临时的工作需求。
我们可以用at命令实现这种功能，只需要写成“at 时间”的形式就可以。 
at的语法结构为： at [OPTION]... TIME TIME
可以设定为以下的形式，非常灵活多变：
HH:MM [YYYY-mm-dd] noon，midnight, teatime tomorrow now+# UNIT：minutes, hours, days, OR weeks 

比如： now +5minutes 表示任务将在5分钟后执行； now +1hours 表示任务将在1小时候执行； now + 31days 表示任务将在1个月后执行； now +1weeks表示任务将在1周后执行； 12:32 表示任务将在今天的12:32分的时候执行；

示例：今晚11点30分开启网站服务 前提：系统开启atd服务。 
[root@kongd ~]# yum install at 
[root@kongd ~]# systemctl start atd.service 
[root@kongd ~]# systemctl enable atd.service  
[root@kongd ~]# at 23:30 at> systemctl restart htt
d at> <EOT> job 1 at Mon Se
 23 23:30:00 2019

 一次性计划任务：Ctrl + D组合键来结束编写计划任务
 at命令接收前面echo命令的输出信息，以达到通过非交互 式的方式创建计划一次性任务的目的
[root@kongd ~]# echo "systemctl restart htt  d" | at 23:30 job 2 at Mon Se
  23 23:30:00 2019 
 查看：at -l 
 [root@kongd ~]# at -l 1 Mon Se
  23 23:30:00 2019 a root 2 Mon Se
  23 23:30:00 2019 a root 
 删除：atrm 
 [root@kongd ~]# atrm 2


#### 计划任务简介 
如果我们希望Linux系统能够周期性地. 有规律地执行某些具体的任务，
那么Linux系统中默认启用的crond服务创建. 
编辑计划任务的命令为“crontab -e”，
查看当前 计划任务的命令为“crontab -l”，
删除某条计划任务的 命令为“crontab -r”。 
crontab命令中加上-u参数来编辑他人的
### corn 基础


### 系统级计划任务
/etc/crontab
### 用户级计划任务



## 日志系统

## 日志轮转
## ssh服务
* tc
* dum
 * -i eth1 -nnX 
* ort 21

## o
## enssh 22端口
sshd服务
验证方式
    1. 口令
    2. 密钥：公钥，私钥
[root@localhost baiyang]# ls /etc/ssh/ -l
total 156
-rw-------. 1 root root 125811 A
r  9  2019 moduli
-rw-r--r--. 1 root root   2047 A
r  9  2019 ssh_config
-rw-------. 1 root root   3879 A
r  9  2019 sshd_config
-rw-------. 1 root root    668 Mar 11  2019 ssh_host_dsa_key
-rw-r--r--. 1 root root    590 Mar 11  2019 ssh_host_dsa_key.
ub
-rw-------. 1 root root    963 Mar 11  2019 ssh_host_key
-rw-r--r--. 1 root root    627 Mar 11  2019 ssh_host_key.
ub
-rw-------. 1 root root   1675 Mar 11  2019 ssh_host_rsa_key
-rw-r--r--. 1 root root    382 Mar 11  2019 ssh_host_rsa_key.
ub


## DNS服务器 
### DNS服务及域名空间 
* 什么是域名？ 域名（Domain Name），简称域名. 网域，是由一串用点分 隔的名字组成的 Internet 上某一台计算机或计算机组的名称，用 于在数据传输时标识计算机的电子方位。具有独一无二，不可重复 的特性。
* 什么是 DNS？ 
* 域名系统（Domain Name System，缩写： DNS）是互联网的一项服务。 
* 域名解析是把域名指向网站空间IP，让人们通过注册的域名可以方便地访问到网站的一种服务。 
* IP地址是网络上标识 站点的数字地址，为了方便记忆，采用域名来代替 
* IP 地址标识站点地址。
* 域名解析就是域名到 IP 地址的转换过程。
* 域名的解析工作由 DNS 服务器完成。 可以理解为 DNS 就是翻译官
* DNS域名解析的过程 
 1. 递归
 2. 迭代
 3. 代理
* DNS的查询模式与解析类型 
* DNS服务器的类型与hosts文件 
* DNS资源记录及其种类 
* DNS软件信息 
* 正反向DNS配置 
* 主从DNS配置 
* DNS缓存服务器

## rsync 远程shell数据传输
## LAMP 架构 LAMP概述 
### BS架构
LAMP原理 
    动态网页和静态网页的区别 
LAMP部署方式
* 基于B/S的Web系统三层体系 
* 软件开发 C/s or B/S： 
    1. C/S : Client/Server 
    2. B/S : Browser/Server
* B/S架构的特点： 
    客户端要求低 可维护性很高 数据安全性高 实时交互性好
* B/S架构的三层体系 
    分层式设计：分散关注.  松散耦合.  逻辑复用.  标准定义 界面表现层 业务逻辑层 数据存储层

### LAMP是什么
1. 基于开源产品的Web架构 ：1998年 ， Michael Kunze为德国计算机杂志写了一篇关于Free软件如何成为商业软件替代品的文章时，创建了LAMP这个名词LAMP由Linux 操作系统.  A
2. ache Web服务器.  MySQL数据库（或MariaDB）和PHP ( Perl或Python ) 脚本语言四种技术的开头字母组成根据PHPChina资料统计在Alexa排名中国前200名的网站 中有61%的采用了LAMP架构 ， 包括腾讯.  百度.  雅 虎.  新浪.  搜狐. Tom等一大批网站
2. 
LAMP架构已成为互联网行业的一盏真正的明灯
2. LAMP的组成体系
* System L: Linux , 包括但不限于Linux ,我们认为可以泛指各种Linux/Unix系统，RedHat.  Suses Debians Turbo.  FreeBSD. Solaris… 
* 
* Server A: A
* ache 一种全球市场占有很高的开源的Web Server ,官方网站 htt
* ://www.a
* ache.org 
* 
* Storage M:MySQL 一种开源的关系型数据库，被下载上千万次，2008年2月26日为Sun收购，2009年4月20日Oracle收购Sun。
    MariaDB数据库管理系统是MySQL的一个分支，主要是应对MySQL闭源的潜在风险。 
* 
* Scri
* t P:PHP ,也可以泛指PHP.  Perl.  Python等解释型脚本语言。
 
据统计在Alexa排名中国TOP200的网站中 ，使用PHP的网站有121个，占60%。
最新web服务器市场排名 htt
s://w3techs.com/technologies/cross/web_server/ranking

### LAMP的实现原理
浏览器向服务器发送http 请求，服务器 (Apache) 接受请求；
A
ache判断客户端请求的资源是否为静态请求。若是静态请求，则A
ache直接将客户端请求的静态资源（.html, .htm .shtml等文件），通过Htt
 res
onse的形式传送给客户端；
若为
h
动态请求，则通过CGI协议将客户端的
h
请求传输给PHP程序，然后由
h
程序调用
h
解析器执行
h
请求。
PHP在执行
h
请求时判断是否会依赖mysql数据库。若不依赖 mysql数据库，则由
h
解析器直接执行
h
相关脚本，将解析后的脚本再次通过CGI协议返传送给A
ache.服务器，再执行 “静态请求”的流程；
若依赖mysql数据库，则
h
程序通过
h
-mysql 驱动与mysql 进行关联 ，获取相关数据 ，然后将其返还给
h
解释器 ，再次执行“不依赖mysql数据库”的流程。


# 系统管理
Linux 目录结构
Linux 文件类型
/etc/fstab

# 服务管理
1. systemctl

# 进程管理

# shell脚本编程
* shell 起源

工具
1. vi/vim
2. linux 指令
3. grep sed awk
4. 服务器部署，优化，日志
 
#### 历史命令 
#### 1）历史命令的查看 
[root@localhost ~]# history [选项] [历史命令保存文件] 
选项：
-c： 清空历史命令 
-w： 把缓存中的历史命令写入历史命令保存文件
如果不手工指定历史命令保存文件，则放入默认历史命令保存文件~/.bash_history 中

#### 输入输出重定向 
1） Bash 的标准输入输出 设备 设备文件名 文件描述符 类型 键盘 
/dev/stdin 0 标准输入 显示器 
/dev/stdout 1 标准输出 显示器 
/dev/stderr 2 标准错误输出 2） 

输入重定向 <
Bash 的基本功能 
* 输入输出重定向 3） 
 输出重定向 类 型 符 号 作用 标准输出重定向 
 命令 > 文件 以覆盖的方式，把命令的正确输出输出到指定 的文件或设备当中。 
 命令 >> 文件 以追加的方式，把命令的正确输出输出到指定 的文件或设备当中。 
 
 标准错误输出重定向 
 1. 错误命令 2>文件 以覆盖的方式，把命令的错误输出输出到指定的文件或设备当中。 
 2. 错误命令 2>>文件 以追加的方式，把命令的错误输出输出到指定 的文件或设备当中。 
 
 正确输出和错误输出同时保存 
 命令 > 文件 2>&1 以覆盖的方式， 命令 &>文件 以覆盖的方式
 命令 >> 文件 2>&1 以追加的方式， 命令 &>>文件 以追加的方式
 >> 把正确输出和错误输出都保存到同一个文件当中
 
 命令>>文件 1 2>>文件 2 把正确的输出追加到文件 1 中，把错误的输出追加到文件 2 中

### 用户登录shell类型 
login shell 取得bash 时需要完整的登录流程，需要读取完整的配置文件，
例如我们通过tty1-tty6通过用户名和密码登录的shell就属 于login shell，ssh 
远程登录的用户的shell也是login shell。 
login shell 主要读取两个配置文件
/etc/profile 和 ~/.bash_profile 首先/etc/profile在系统登录的时候进行配置环境 
~/.bash_profile是login shell 登录时进行读取，且该文件会读取 
    ~/.bash_profile 
    ~/.bash_login 
    ~/.profile
### non-login shell 取得bash的接口不需要重复登录，
比如在图形化界面的ctl+alt+t出来的shell就属于non-login shell 
直接在命令行中通过su username也属于non-login shell。 
非登录式shell如何读取配置文件？ ~./.bashrc-->/etc/bashrc-->/etc/profile.d/*.sh

#### 测试运算符。Shell程序能够判断某种或者几个条件是否成立。
条件测试的基本语法 
格式1： test 条件表达式 
格式2： [ 条件表达式 ] 
格式3： [[ 条件表达式 ]] 

#### 文件测试表达式 
[ 操作符 文件或目录 ] 操作符 说明 举例 
-b file 检测文件是否是块设备文件，    [ -b $file ] 返回 false。 
-c file 检测文件是否是字符设备文件，  [ -b $file ] 返回 false。 
-d file 检测文件是否是目录，   [ -d $file ] 返回 false。 
-f file 检测文件是否是普通文件（既不是目录，也不是设备文件）[ -f $file ] 返回 true。 
-g file 检测文件是否设置了 SGID 位，    [ -g $file ] 返回 false。 
-k file 检测文件是否设置了粘着位(Sticky Bit)，    [ -k $file ] 返回 false。 
-
 file 检测文件是否是具名管道，     [ -
 $file ] 返回 false。 
-u file 检测文件是否设置了 SUID 位， [ -u $file ] 返回 false。 
-r file 检测文件是否可读，           [ -r $file ] 返回 true。




# NoSql
## Redis 全称：Remote Dictionary Server（远程字典服务器）
是完全开源免费的，用C语言编写的， 遵守BSD协 议。是一个高性能的(key/value)分布式内存数据库，基于 内存运行并支持持久化的NoSQL数据库，是当前最热门的 NoSql数据库之一,也被人们称为数据结构服务器。 
Redis 与其他 key - value 缓存产品有以下三个特点Redis支持数据的持久化，可以将内存中的数据保持在磁盘中，重启的时候可以再次加载进行使用 Redis不仅仅支持简单的key-value类型的数据，同时还提供 list，set，zset，hash等数据结构的存储 Redis支持数据的备份，即master-slave模式的数据备份

## MongoDB 是由C++语言编写的，
是一个基于分布式文件 存储的开源数据库系统。
在高负载的情况下，添加更多的节点，可以保证服务器性能。
MongoDB 旨在为WEB应用提供可扩展的高性能数据存储 解决方案。
MongoDB 将数据存储为一个文档，数据结构由键值 (key=>value)对组成。
MongoDB 文档类似于 JSON 对象。字段值可以包含其 他文档，数组及文档数组。
# Nginx 反向代理