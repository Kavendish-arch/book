linux档案权限
group 组批量管理用户权限

gedit 带图形界面的打开
## 文本编辑器 vim vi

```
[root@localhost hadoop]# chmod o+rwx myfile.h 
[root@localhost hadoop]# u group other all
[root@localhost hadoop]# chmod
[root@localhost hadoop]# echo 'hadoop ALL=(ALL) ALL' >> /etc/sudoers
```
### 用户及用户组管理命令
    chown [-R] user  file
    chgrp [-R] group file
    chown [-R] user group file 

1. useradd
    useradd 命令可以创建一个新的用户帐号 其最基本用法为
    useradd 用户名
    如输入以下命令
    [root@localhost hadoop]# useradd newuser
    系统将创建一个新用户 newuser 该用户的 Home 目录为/home/newuser

    useradd 命令的参数较多 常用的组合为
    useradd 用户名 -g 组名 –G 组名 -d Home 目录名 -p 密码
    其中 -g 指定该用户的首要组
    -G 指定该用户的次要组
    -d 指定该用户的 Home 目录
    -p 指定该用户的密码
    如输入以下命令
    [root@localhost hadoop]# useradd oracle –g oinstall –G dba –d /home/oracle –p ora123
    系统将创建一个用户 oracle oracle 用户的首要组为 oinstall 次要组为 dba
    Home 目录为/home/oracle 密码为 ora123

2. userdel
userdel 命令用于删除一个已存在的帐号 其用法为
userdel 用户名
3. groupadd
groupadd 命令可以创建一个新的用户组 其最基本用法为
groupadd 组名
如输入以下命令
groupadd newgroup
系统将创建一个新的用户组 newgroup
4. groupdel
groupdel 命令用于删除一个已存在的用户组 其用法为
groupdel 组名
5. passwd
    出于系统安全考虑 Linux系统中的每一个用户除了有其用户名外还有其对应
    的用户口令 用户可以随时用 passwd 命令改变自己的口令 该命令的一般格式为
    [root@localhost hadoop]# passwd
    输入该命令后 按系统提示依次输入密码和密码确认后 即可完成用户密码的修改
    此外 超级用户还可以修改其他用户的口令 命令如下
    [root@localhost hadoop]# passwd 用户名
6. su
su 命令这个命令非常重要 它可以让一个普通用户拥有超级用户或其他用户的权限 也可以让超级用户以普通用户的身份做一些事情,普通用户使用这
个命令时必须有超级用户或其他用户的口令 如要离开当前用户的身份 可以键入 exit 命令 su 命令的一般形式为
su - 用户名

## 权限；r w x
7. chmod
    chmod 命令是非常重要的 用于改变文件或目录的访问权限 该命令有两种
    用法 一种是包含字母和操作符表达式的文字设定法 
    另一种是包含数字的
    数字设定法 由于数字设定法不太直观 本文不做介绍 文字设定法的用法如下
    [root@localhost hadoop]# chmod [who] [+ | - | =] [mode] 文件名
    命令中各选项的含义为
 1. 操作对象 who 可以是下述字母中的任一个或者它们的组合
    u 表示用户(user) 即文件或目录的所有者
    g 表示同组(group)用户 即与文件属主有相同组 ID 的所有用户
    o 表示其他(others)用户
    a 表示所有(all)用户 它是系统默认值
2. 操作符号可以是
    + 添加某个权限
    - 取消某个权限
    = 赋予给定权限,并取消其他所有权限
3. mode 表示权限 常用的参数有
    r 可读 w 可写 x 可执行
举例
1 将文件 script 的权限设为可执行 命令如下
    chmod =rx text
    执行成功后 用 ls -l script 命令查看文件属性的结果如下
    -r-xr-xr-x 1 user group 0 Feb 10 09:42 script
2 将文件 text 的权限设为 文件属主可读 可写 可执行 与文件属主同组
    的用户可读 其他用户不可读 命令如下
    chmod u=rwx,g=r,o= text 注意,后无空格 o=后有空格
    执行成功后 用 ls –l text 命令查看文件属性的结果如下
    -rwxr----- 1 user group 0 Feb 10 09:42 text

8. chown
    chown 用于更改某个文件或目录的属主和属组这个命令也很常用 
    例如
    root 用户把自己的一个文件拷贝给用户 oracle 为了让用户 oracle 能够存
    取这个文件 root 用户应该把这个文件的属主设为oracle 否则用户oracle
    无法存取这个文件 chown 的基本用法为
    chown [用户:组] 文件
    举例
    chown oracle:dba text
    该命令将 text 文件的属主和属组分别改为 oracle 和 dba

目录 {
    FHS规范，Linux都遵循这个规范
    bin: 可执行文件
    boot: 启动文件
    dev: 设备文件
    etc: 配置文件
    home: 用户目录
    lib: 库文件
    media: 设备挂载点文件
    mnt: 手动设备挂载点
    opt: 大型软件安装包（源码安装包）
    usr: 软件安装包
    proc: 进程文件
    sbin: 系统管理员命令文件
    tmp: 临时文件
    var: 日志缓存、数据文件
}
### 查看系统信息{
    uname 
    uname -i 配置信息
    uname -r 内核信息
    uname -a 所有信息
    lsb_release -a
    cat /etc/redhat-release 
}
目录操作命令{
    pwd
    cd 
    mkdir
    rmdir 删除空目录
    rm -f 强制删除
    mv
    cp 
    touch
    filecat
}
### 绝对路径和相对路径{
    . 当前目录、.. 上一级、-、/ 根目录、~ 用户级别 ~account
}

### 进程及任务管理命令
Linux系统上所有运行的东西都可以称之为一个进程 每个用户任务 每个系
统管理守护进程都可以称之为进程 Linux用分时管理方法使所有的任务共同
分享系统资源 以下将介绍一些常用的查看和控制进程的命令
1. ps
ps 命令是最基本同时也是非常强大的进程查看命令 使用该命令可以查看有
哪些进程正在运行以及运行的状态 进程是否结束 进程有没有僵死 哪些
进程占用了过多的资源等等
Linux 操作指导专题 文档密级 内部公开
2004-02-04 华为 3Com 机密 未经许可不得扩散 第14页, 共53页
该命令的基本用法如下
ps [选项]
其中常用的选项有
-e 显示所有进程
-f 全格式
-l 长格式
举例
1 在控制台输入 ps 命令 得到类似如下的输出
 PID TTY TIME CMD
12039 pts/0 00:00:00 bash
18710 pts/0 00:00:00 ps
该命令显示当前登录用户的执行进程 显示的项目共分为四项 依次为 PID(进 程 ID) TTY(终端名称) TIME(进程执行时间) CMD(该进程的命令行输入) 2 在控制台输入以下命令
ps –ef
UID PID PPID C STIME TTY TIME CMD
root 1 0 0 Jan14 ? 00:00:05 init
root 2 1 0 Jan14 ? 00:00:00 [keventd]
root 3 1 0 Jan14 ? 00:00:00 [kapmd]
…………………..
该命令将显示所有执行进程的信息 显示的项目依次为 UID 执行进程的用
户 ID PID(进程 ID) PPID(父进程 ID) TTY(终端名称) STIME(进程启 动时间) TIME(进程执行时间) CMD(该进程的命令行输入)
该命令的输出较多 可以使用 grep 命令进行过虑 以方便查看 如
ps –ef|grep oracle
将只显示出包含 oracle 的输出行 可以查询执行进程的用户为 oracle 的所有
进程
2. top
top 命令和 ps 命令的基本作用是相同的 显示系统当前的进程和其他状况
但是 top 是一个动态显示过程 即可以通过用户按交互来不断刷新当前状态
top 的命令参数并不重要 简单的输入 top 命令即可查看系统运行状态
Linux 操作指导专题 文档密级 内部公开
2004-02-04 华为 3Com 机密 未经许可不得扩散 第15页, 共53页
top 命令执行过程中可以使用交互命令 从使用角度来看 熟练的掌握这些命
令比掌握选项还重要一些 这些命令都是单字母的 常用的命令有
<空格> 立即刷新显示
h 或者? 显示帮助画面给出一些简短的命令总结说明
m 切换显示内存信息
t 切换显示进程和 CPU状态信息
c 切换显示命令名称和完整命令行
M 根据驻留内存大小进行排序
P 根据 CPU使用百分比大小进行排序
q 退出
3. kill
kill 命令可以用于终止后台进程 kill 命令是通过向进程发送指定的信号来
结束进程的 kill 命令的语法格式很简单 大致有以下两种方式
1 kill [-s 信号] 进程号
其中 发出的信号既可以是信号名也可以对应数字
如 kill -9 1234 命令 将终止 PID(进程号)为 1234 的进程
2 kill -l 
该命令显示信号列表
4. cron
cron 命令用来实现定时任务的完成 如每日执行一次的任务 进程
cron 命令是不应该手工启动的 一般情况下 cron 命令在系统启动时就由一
个 shell 脚本自动启动 启动后 cron 命令会搜索/var/spool/cron 目录 寻找
以/etc/passwd 文件中的用户名命名的 crontab 文件 被找到的这种文件将载
入内存 例如一个用户名为 user 的用户它所对应的 crontab 文件就应该是
/var/spool/cron/user 也就是说 以该用户命名的 crontab 文件存放在
/var/spool/cron 目录下面 cron 命令还将搜索/etc/crontab 文件 这个文件是
用不同的格式写成的 cron 启动以后它将首先检查是否有用户设置了 crontab
文件 如果没有就转入休眠状态 释放系统资源 它每分钟醒过来一次查看
当前是否有需要运行的命令
Linux 操作指导专题 文档密级 内部公开
2004-02-04 华为 3Com 机密 未经许可不得扩散 第16页, 共53页 可以使用 crontab –l 命令查看目前已经存在的 cron 任务

PATH{
    echo $PATH
    PATH = ""
}
查看{
    cat 第一行开始
    tac 最后一行开始
    nl  带行号
    more 
    less 
    head 头几行
    tail 只看尾巴  tail -f 动态更新
    od   二进制查看
}
目录的默认权限和隐藏权限{
    umask
    chattr [+-] [attr] file
}
## ssh连接服务 安装
* 输入以下命令进行安装远程ssh服务
```
# sudo apt-get install openssh-server
若没有ssh，需要执行
# sudo apt-get install ssh
# service sshd start 服务开启
```
## lrzsz 传文件
    1. rz上传文件
    2. sz下载文件 
* XXX is not in the sudoers file.  This incident will be reported.
    1. step1：用su换为root用户，并输入以下命令进入sudo配置文件  visudo
    2. step2：在配置文件里找到下边的位置，并加入用户权限，保存退出。 Allow root to run any commands anywhere
    3. step3：再次使用sudo命令就不会出现报错信息了。



常用的软件
Putty{
    Telnet
    ssh
    rlogin 
}
linux软件安装{
    压缩包：二进制文件安装：
        常用于归档的编译好的文件压缩包
        jdk安装 解压缩可用
        /etc/profile
        PATH=$":"$Java_Home"/bin"   配置在环境变量之后
        PATH=$Java_Home"/bin:"$PATH 配置在环境变量之前
        tomcat安装配置
        tar -zxvf tomcat...tar.gz
        vim /etc/profile
        CATALINA_HOME = 
        PATH
        ./conf/server.xml端口号

    rpm文件安装包（redhat package manager)
        rpm -qa|grep [keywords]
        rpm -ivh software.rpm  -v
        rpm -e --nodeps software.rpm 
        不检查依赖关系
    yum安装
        yum list installed 已安装列表
        yum search keywords
        yum install software-name
        yum remove software-name
}
4.1.1 RPM 安装操作
命令
    rpm -i 需要安装的包文件名
举例如下
    rpm -i example.rpm 安装 example.rpm包
    rpm -iv example.rpm 安装 example.rpm包 并在安装过程中显示正在安装的文件信息
    rpm -ivh example.rpm 安装 example.rpm包 并在安装过程中显示正在安装的文件信息及安装进度
4.1.2 RPM 查询操作
命令 
    rpm -q …
附加查询命令
    a 查询所有已经安装的包
以下两个附加命令用于查询安装包的信息
    i 显示安装包的信息
    l 显示安装包中的所有文件被安装到哪些目录下
以下两个附加命令用于指定需要查询的是安装包还是已安装后的文件
    p 查询的是安装包的信息
    f 查询的是已安装的某文件信息
    举例如下
    rpm -qa | grep tomcat4 查看 tomcat4 是否被安装
    rpm -qip example.rpm 查看 example.rpm安装包的信息
    rpm -qif /bin/df 查看/bin/df 文件所在安装包的信息
    rpm -qlf /bin/df 查看/bin/df 文件所在安装包中的各个文件分别被安装到哪个目录下
4.1.3 RPM 卸载操作
命令
    rpm -e 需要卸载的安装包
在卸载之前 通常需要使用 rpm -q …命令查出需要卸载的安装包名称
举例如下
    rpm -e tomcat4 卸载 tomcat4 软件包
4.1.4 RPM 升级操作
命令
    rpm -U 需要升级的包
举例如下
    rpm -Uvh example.rpm 升级 example.rpm软件包
4.1.5 RPM 验证操作
命令
rpm -V 需要验证的包
举例如下
rpm -Vf /etc/tomcat4/tomcat4.conf
输出信息类似如下
S.5....T c /etc/tomcat4/tomcat4.conf
其中 S 表示文件大小修改过 T 表示文件日期修改过 限于篇幅 更多的验
证信息请您参考 rpm帮助文件 man rpm
4.1.6 RPM 的其他附加命令
    --force 强制操作 如强制安装 删除等
    --requires 显示该包的依赖关系
    --nodeps 忽略依赖关系并继续操作

软件安装命令
1. tar
    tar 命令用于把多个文件合并于一个档案文件中 并提供分解的合并后的档案
    文件的功能 它独立于压缩工具 因此可以选择在合并前是否压缩 tar 命令
    的基本用法为
    tar [选项] 文件名
    常用的选项包括
    -c 创建一个新的档案文件
    -t 查看档案文件的内容
    -x 分解档案文件的内容
    -f 指定档案文件的名称
    -v 显示过程信息
    -z 采用压缩方式
    举例
[hadoop@localhost /]$ tar -czf oracle.tar.gz /u01/app/oracle /etc/oratab /home/oracle
    该命令将/u01/app/oracle 目录下的所有文件 /etc/oratab 文件和
    /home/oracle 目录下的所有文件合并到 oracle.tar 文件中 并采用压缩方式
[hadoop@localhost /]$ tar -tzf oracle.tar.gz
    该命令列出归档文件 oracle.tar 中的所有文件列表
[hadoop@localhost /]$ tar –xzvf oracle.tar.gz
    该命令将归档文件分解并解压缩到原有文件的路径中
2. rpm
rpm命令的功能有很多 在这里我们只介绍如何利用 rpm安装和查询已安
装的软件
1. 安装 rpm安装软件包的基本语法如下
[hadoop@localhost /]$ rpm -i rpm包名
例如
[hadoop@localhost /]$ rpm -i tomcat4.rpm
该命令将安装 Tomcat 软件并进行相关系统配置
2. 升级 rpm升级软件包的基本语法如下
[hadoop@localhost /]$ rpm -U rpm包名
例如
[hadoop@localhost /]$ rpm –U tomcat4.rpm
该命令将升级 Tomcat 软件并进行相关系统配置

3. 查看已安装的软件有的时候 了解系统中都已经安装了哪些软件包以及它们的用途是很有用
    的RPM的查询参数就可以做到这一点要想列出已经安装的全部软件包 可以通过以下命令
[hadoop@localhost /]$ rpm -qa
    可以使用grep命令指定软件包的名称 或者部分名称
如下所示
[hadoop@localhost /]$ rpm -qa | grep 'tomcat'
    该命令将列出包名中包含 tomcat 的软件包
    此外 要想找出某个特定的文件到底是属于哪个软件包的 可以输入
[hadoop@localhost /]$ rpm -qf filename
    其中 filename 是准备要查找其归属的文件名称
    要想查出某个已经安装的软件包的功能 可以用如下命令
[hadoop@localhost /]$ rpm -qi packagename 其中 packagename 是要查找其用途的软件包名称
4 删除已安装的软件：使用RPM删除软件包就像安装它们一样简单 大多数情况下用户只需要输入命令
[hadoop@localhost /]$ rpm -e packagename 其中 ackagename 是要查删除的软件包名称

# 时钟系统介绍
对于 Linux操作系统 主要有两种时钟系统
1 硬件时钟系统 该时钟系统的运行独立于任何系统控制程序 在 CPU 内部运行 既使系统断电 该时钟系统仍然保持运行 此时钟系统常常被称为
实时时钟系统 RTC BIOS 时钟系统或 CMOS 时钟系统
2 系统时间 该时间为 Linux 内核的时钟系统所维护 并且被定时中断程序所驱动 该时间仅当 Linux系统运行过程中有意义 该系统时间表示为以 UTC
通用协调时间 Universal Time Coordinated 计算自1970年1月1日0时0分0秒起至当前时刻所经过的秒数 该数字不是整数,以小数方式表示精度

在 Linux 系统中 真正起作用的是系统时间 硬件时钟系统的唯一作用是在Linux系统没有运行时,保持时间的运行,当 Linux操作系统启动时 系统会
自动将硬件时钟系统的时间同步到 Linux系统时间 并且在之后的整个 Linux运行过程中 不再使用该硬件时钟系统 这与 DOS 的实现方式完全不同 在
DOS 中 只有硬件时间系统的概念 而在 Linux 操作系统关闭时 系统会自动将当前的 Linux系统时间同步到硬件时钟系统所维护的时间

4.2.2 硬件时钟系统与系统时间的同步
/sbin/hwclock 用于同步硬件时钟系统的时间与 Linux操作系统时间
查看当前硬件时钟系统时间的命令为    /sbin/hwclock --show
将硬件时钟系统时间同步到Linux操作系统时间的命令为/sbin/hwclock --hctosys
将Linux操作系统时间同步到硬件时钟系统时间的命令为/sbin/hwclock --systohc
如果观察系统启动/关闭时执行的初始化脚本”/etc/rc.d/rc.sysinit” 我们不难发现 
系统启动过程中自动调用 /sbin/hwclock --hctosys 将硬件时钟系统时间同步到操作系统时间 
系统关闭过程中自动调用 /sbin/hwclock --systohc 将操作系统时间同步到硬件时钟系统时间

# 网络配置{
	//查看网卡
	(base) [root@localhost yum.repo.d]#     ethtool -i eth0
	driver: vmxnet
	version: 2.1.0.0
	firmware-version: N/A
	bus-info: 0000:02:01.0
	supports-statistics: no
	supports-test: no
	supports-eeprom-access: no
	supports-register-dump: no
	supports-priv-flags: no
	//卸载网卡驱动
	(base) [root@localhost yum.repo.d]#     modprobe -r vmxnet
	//加载网卡驱动
	(base) [root@localhost yum.repo.d]#     modprobe vmxnet

	
	//查看网卡配置
	cat /etc/sysconfig/network-srcipts/ifcfg-eth0
	DEVICE="eth0"		
	BOOTPROTO="dhcp"
	HWADDR="00:0C:29:57:75:8E" 
	IPV6INIT="yes"
	NM_CONTROLLED="yes" 
	ONBOOT="yes"
	TYPE="Ethernet" 
	UUID="0ba5bee2-3fdd-4451-972e-67daea901b92"
	~   
	DEVICE：此配置文件应用到的设备
	HWADDR：对应的设备的MAC地址
	BOOTPROTO：激活此设备时使用的地址配置协议，常用的dhcp, static, none, bootp
	NM_CONTROLLED：NM是NetworkManager的简写，此网卡是否接受NM控制；建议为“no”(NetworkManager:图形界面的网络配置工具，不支持桥接，强烈建议关闭)
	ONBOOT：在系统引导时是否激活此设备
	TYPE：接口类型，常见有的Ethernet, Bridge
	UUID：设备的惟一标识
	IPADDR：指明IP地址
	NETMASK：子网掩码
	GATEWAY: 默认网关
	DNS1：第一个DNS服务器指向
	DNS2：第二个DNS服务器指向
	USERCTL：普通用户是否可控制此设备
	PEERDNS：如果BOOTPROTO的值为“dhcp”，是否允许dhcp server分配的dns服务器指向信息直接覆盖至/etc/resolv.conf文件中
	
    网络命令
ifconfig 查看网络接口信息
ifconfig eth0 特定网卡
    root权限 网卡开关
    ifup   eth0     ifconfig eth0 up
    ifdown eth0     ifconfig eth0 down
    host        解析域名  
    hostname    主机名
    vim /etc/sysconfig/network     
    vim /etc/hosts      本地主机名解析文件
    ping 测试其他主机

    查看网络配置
    

    防火墙
        service 停止和启动服务、临时
        service iptables stop
        
        服务开机自启动的开始和关闭
        chkconfig iptables off 
        chkconfig 
        chkconfig [--level <dengji>] server on off
        查看服务级别
}
DNS服务器
    centOS6
    rpm -qa|grep bind

    yum install bind
    DNS域名服务器IP地址 
    正向区域名
    反向区域名
    正向区域文件名
    反向区域文件名
    正向区域中的相关资源记录
    反向区域中的相关资源记录
[root@bogon named]# rpm -qc bind
/etc/logrotate.d/named
/etc/named.conf
/etc/named.iscdlv.key
/etc/named.rfc1912.zones
/etc/named.root.key
/etc/rndc.conf
/etc/rndc.key
/etc/sysconfig/named
/var/named/named.ca
/var/named/named.empty
/var/named/named.localhost
/var/named/named.loopback

.named.conf文件详解
//
// named.conf
//
// Provided by Red Hat bind package to configure the ISC BIND named(8) DNS
// server as a caching only nameserver (as a localhost DNS resolver only).
//
// See /usr/share/doc/bind*/sample/ for example named configuration files.
//

options {
        listen-on port 53 { 192.168.1.108; };
        listen-on-v6 port 53 { ::1; };
        directory       "/var/named";
        dump-file       "/var/named/data/cache_dump.db";
        statistics-file "/var/named/data/named_stats.txt";
        memstatistics-file "/var/named/data/named_mem_stats.txt";
        allow-query     { any; };
        recursion yes;

        dnssec-enable yes;
        dnssec-validation yes;

        /* Path to ISC DLV key */
        bindkeys-file "/etc/named.iscdlv.key";

        managed-keys-directory "/var/named/dynamic";
};

logging {
        channel default_debug {
                file "data/named.run";
                severity dynamic;
        };
};
#区域文件
zone "." IN {
        type hint;
        file "named.ca";
};
#包含其他文件
include "/etc/named.rfc1912.zones";
include "/etc/named.root.key";

~                                                                                                                    
"/etc/named.conf" 43L, 982C        
mysql安装
    wget -i -c http://
    
    
## Shell 变量
命名只能使用英文字母，数字和下划线，首个字符不能以数字开头。
中间不能有空格，可以使用下划线（_）。
不能使用标点符号。
不能使用bash里的关键字（可用help命令查看保留关键字）

只读变量 readonly 变量
删除变量 unset 变量，不能删除只读变量。

1) 局部变量 局部变量在脚本或命令中定义，仅在当前shell实例中有效，其他shell启动的程序不能访问局部变量。
2) 环境变量 所有的程序，包括shell启动的程序，都能访问环境变量，有些程序需要环境变量来保证其正常运行。必要的时候shell脚本也可以定义环境变量。
3) shell变量 shell变量是由shell程序设置的特殊变量。shell变量中有一部分是环境变量，有一部分是局部变量，这些变量保证了shell的正常运行

1. 单引号
单引号里的任何字符都会原样输出，单引号字符串中的变量是无效的；
单引号字串中不能出现单独一个的单引号（转义符后也不行），字符串拼接使用
2. 双引号：双引号里可以有变量，双引号里可以出现转义字符


* 定义数组 ()
在 Shell 中，用括号来表示数组，数组元素用"空格"符号分割开。定义数组的一般形式为：
数组名=(值1 值2 ... 值n)
array_name=(value0 value1 value2 value3)
或者
array_name=(
value0
value1
value2
value3
)
还可以单独定义数组的各个分量：
array_name[0]=value0
array_name[1]=value1
array_name[n]=valuen
可以不使用连续的下标，而且下标的范围没有限制。

读取数组
读取数组元素值的一般格式是：
${数组名[下标]}  valuen=${array_name[n]}

使用 @ 符号可以获取数组中的所有元素，例如：
echo ${array_name[@]}

获取数组长度的方法与获取字符串长度的方法相同，例如：
# 取得数组元素的个数
length=${#array_name[@]}
或者
length=${#array_name[*]}

# 取得数组单个元素的长度
lengthn=${#array_name[n]}


* Shell 注释

以 # 开头的行就是注释，会被解释器忽略。
通过每一行加一个 # 号设置多行注释，像这样：
#--------------------------------------------
# 这是一个注释
# author：菜鸟教程
# site：www.runoob.com
# slogan：学的不仅是技术，更是梦想！
#--------------------------------------------
##### 用户配置区 开始 #####
#
# 这里可以添加脚本描述信息
#
##### 用户配置区 结束  #####

多行注释
:<<EOF
注释内容...
注释内容...
注释内容...
EOF

$#	传递到脚本的参数个数
$*	以一个单字符串显示所有向脚本传递的参数。
如"$*"用「"」括起来的情况、以"$1 $2 … $n"的形式输出所有参数。
$$	脚本运行的当前进程ID号
$!	后台运行的最后一个进程的ID号
$@	与$*相同，但是使用时加引号，并在引号中返回每个参数。
如"$@"用「"」括起来的情况、以"$1" "$2" … "$n" 的形式输出所有参数。
$-	显示Shell使用的当前选项，与set命令功能相同。
$?	显示最后命令的退出状态。0表示没有错误，其他任何值表明有错误。

# shell 运算
Shell 和其他编程语言一样，支持多种运算符，包括：
算数运算符
关系运算符
布尔运算符
字符串运算符
文件测试运算符

## 数学运算
* 原生bash不支持简单的数学运算，但是可以通过其他命令来实现，例如 awk 和 expr(最常用)
* expr 是一款表达式计算工具，表达式和运算符之间要有空格，完整的表达式要被 ` ` 包含反引号
加法	`expr $a + $b` 
减法	`expr $a - $b` 
乘法	`expr $a \* $b` 
除法	`expr $b / $a` 
取余	`expr $b % $a` 
赋值	a=$b 
相等   [ $a == $b ] 
不相等 [ $a != $b ] 。

## 关系运算符 支持数字，不支持字符串，除非字符串的值是数字。
-eq	==  [ $a -eq $b ] 
-ne	!=  [ $a -ne $b ] 
-gt	>，	[ $a -gt $b ] 
-lt	<，	[ $a -lt $b ]
-ge	>=，[ $a -ge $b ] 
-le	<=，[ $a -le $b ]
## 字符串运算符
=	检测两个字符串是否相等，	[ $a = $b ] 
!=	检测两个字符串是否相等，	[ $a != $b ] 。
-z	检测字符串长度是否为0，   [ -z $a ] 
-n	检测字符串长度是否不为 0，[ -n "$a" ] 。
$	检测字符串是否为空，      [ $a ] 。

## 布尔运算符
!	非运算，[ ! false ] 。
-o	或运算，[ $a -lt 20 -o $b -gt 100 ] 。
-a	与运算，[ $a -lt 20 -a $b -gt 100 ] 

## 逻辑运算符
&&	逻辑的 AND	[[ $a -lt 100 && $b -gt 100 ]] 
||	逻辑的 OR	[[ $a -lt 100 || $b -gt 100 ]] 


## 文件测试运算符 文件测试运算符用于检测 Unix 文件的各种属性。

-b file	是否是块设备文件，	[ -b $file ] 
-c file	是否是字符设备文件，	[ -c $file ] 
-d file	是否是目录，	[ -d $file ] 
-f file	是否是普通文件（既不是目录，也不是设备文件），	[ -f $file ] 。
-g file	是否设置了 SGID 位，	[ -g $file ] 
-k file	是否设置了粘着位(Sticky Bit)，	[ -k $file ] 
-p file	是否是有名管道，	[ -p $file ] 
-u file	是否设置了 SUID 位，	[ -u $file ] 
-r file	是否可读，	[ -r $file ] 。
-w file	是否可写，	[ -w $file ] 。
-x file	是否可执行，	[ -x $file ] 。
-s file	是否为空（文件大小是否大于0），不为空。	[ -s $file ] 。
-e file	（包括目录）是否存在，	[ -e $file ] 。
-S: 判断某文件是否 socket。
-L: 是否存在并且是一个符号链接。


## 流程控制

### if分支
* if 语句语法格式：
if condition then commandN fi 写成一行（适用于终端命令提示符）：
if [ $(ps -ef | grep -c "ssh") -gt 1 ]; then echo "true"; fi

* if else 语法格式：
*if* condition *then* command1 else command fi

* if else-if else 语法格式：
if condition1 then command1 elif condition2 then command2 else commandN fi

### for 循环
for var in item1 item2 ... itemN do commandN done
当变量值在列表里，for循环即执行一次所有命令，使用变量名获取列表中的当前取值。命令可为任何有效的shell命令和语句。in列表可以包含替换、字符串和文件名。

### while 语句 用于不断执行一系列命令，也用于从输入文件中读取数据；命令通常为测试条件

while condition do command done

#!/bin/bash
int=1
while(( $int<=5 ))
do
    echo $int
    let "int++"
done


以上实例使用了 Bash let 命令，它用于执行一个或多个表达式，变量计算中不需要加上 $ 来表示变量，具体可查阅：Bash let 命令


while循环可用于读取键盘信息。下面的例子中，输入信息被设置为变量FILM，按<Ctrl-D>结束循环。

echo '按下 <CTRL-D> 退出'
echo -n '输入你最喜欢的网站名: '
while read FILM
do
    echo "是的！$FILM 是一个好网站"
done
运行脚本，输出类似下面：

按下 <CTRL-D> 退出

* 无限循环
无限循环语法格式：

while :
do
    command
done

while true
do
    command
done
或者
for (( ; ; ))
* until 循环
until 循环执行一系列命令直至条件为 true 时停止。

until 循环与 while 循环在处理方式上刚好相反。

一般 while 循环优于 until 循环，但在某些时候—也只是极少数情况下，until 循环更加有用。

until 语法格式:

until condition
do
    command
done
condition 一般为条件表达式，如果返回值为 false，则继续执行循环体内的语句，否则跳出循环。

以下实例我们使用 until 命令来输出 0 ~ 9 的数字：

#!/bin/bash

a=0

until [ ! $a -lt 10 ]
do
   echo $a
   a=`expr $a + 1`
done
运行结果：

输出结果为：

0
1
2
3
4
5
6
7
8
9

* Shell case语句为多选择语句。可以用case语句匹配一个值与一个模式，如果匹配成功，执行相匹配的命令。case语句格式如下：

case 值 in
模式1)
    command1
    command2
    ...
    commandN
    ;;
模式2）
    command1
    command2
    ...
    commandN
    ;;
esac
case工作方式如上所示。取值后面必须为单词in，每一模式必须以右括号结束。取值可以为变量或常数。匹配发现取值符合某一模式后，其间所有命令开始执行直至 ;;。

取值将检测匹配的每一个模式。一旦模式匹配，则执行完匹配模式相应命令后不再继续其他模式。如果无一匹配模式，使用星号 * 捕获该值，再执行后面的命令。

下面的脚本提示输入1到4，与每一种模式进行匹配：

echo '输入 1 到 4 之间的数字:'
echo '你输入的数字为:'
read aNum
case $aNum in
    1)  echo '你选择了 1'
    ;;
    2)  echo '你选择了 2'
    ;;
    3)  echo '你选择了 3'
    ;;
    4)  echo '你选择了 4'
    ;;
    *)  echo '你没有输入 1 到 4 之间的数字'
    ;;
esac
输入不同的内容，会有不同的结果，例如：

输入 1 到 4 之间的数字:
你输入的数字为:
3
你选择了 3
跳出循环
在循环过程中，有时候需要在未达到循环结束条件时强制跳出循环，Shell使用两个命令来实现该功能：break和continue。

* break命令
break命令允许跳出所有循环（终止执行后面的所有循环）。

下面的例子中，脚本进入死循环直至用户输入数字大于5。要跳出这个循环，返回到shell提示符下，需要使用break命令。

#!/bin/bash
while :
do
    echo -n "输入 1 到 5 之间的数字:"
    read aNum
    case $aNum in
        1|2|3|4|5) echo "你输入的数字为 $aNum!"
        ;;
        *) echo "你输入的数字不是 1 到 5 之间的! 游戏结束"
            break
        ;;
    esac
done
执行以上代码，输出结果为：

输入 1 到 5 之间的数字:3
你输入的数字为 3!
输入 1 到 5 之间的数字:7
你输入的数字不是 1 到 5 之间的! 游戏结束
continue
continue命令与break命令类似，只有一点差别，它不会跳出所有循环，仅仅跳出当前循环。

对上面的例子进行修改：

#!/bin/bash
while :
do
    echo -n "输入 1 到 5 之间的数字: "
    read aNum
    case $aNum in
        1|2|3|4|5) echo "你输入的数字为 $aNum!"
        ;;
        *) echo "你输入的数字不是 1 到 5 之间的!"
            continue
            echo "游戏结束"
        ;;
    esac
done
运行代码发现，当输入大于5的数字时，该例中的循环不会结束，语句 echo "游戏结束" 永远不会被执行。

case ... esac
case ... esac 与其他语言中的 switch ... case 语句类似，是一种多分枝选择结构，每个 case 分支用右圆括号开始，用两个分号 ;; 表示 break，即执行结束，跳出整个 case ... esac 语句，esac（就是 case 反过来）作为结束标记。

* case ... esac 语法格式如下：

case 值 in
模式1)
    command1
    command2
    command3
    ;;
模式2）
    command1
    command2
    command3
    ;;
*)
    command1
    command2
    command3
    ;;
esac
case 后为取值，值可以为变量或常数。

值后为关键字 in，接下来是匹配的各种模式，每一模式最后必须以右括号结束，模式支持正则表达式。



1. 下载内核 linux-2.6.11.10.tar.xz 国外下载缓慢采用国内镜像源
   北京交通大学开源镜像站  https://mirror.bjtu.edu.cn/kernel/linux/kernel/v2.6/
2. 在centos里面解压 
   
gzip: stdin: not in gzip format
tar: Child returned status 1
tar: Error is not recoverable: exiting now

对于 tar.xz结尾的压缩文件，解压有两种方式：

可以先将外层用xz解压方式解压,，然后里层用tar解压方式解压：
    xz -d  *****.tar.xz
    tar  -xvf    *****.tar

2.直接使用如下命令解压：
    tar   xvJf   ***.tar.xz


1.zip命令
zip -r mysql.zip mysql 该句命令的含义是：将mysql文件夹压缩成mysql.zip
zip -r abcdef.zip abc def.txt 这句命令的意思是将文件夹 abc 和文件 def.txt压缩成一个压缩包 abcdef.zip

2.unzip命令
与zip命令相反，这是解压命令，用起来很简单。 如：unzip mysql.zip 在当前目录下直接解压mysql.zip。

3.tar命令
例如：tar -cvf 123.tar file1 file2 dir1 该句命令实现一个tar压缩，它是将两个文件（file1和file2）和一个文件夹(dir1)压缩成一个123.tar文件。
tar -zxvf apache-tomcat-7.0.75.tar.gz 该命令在解压安装tomcat时使用，是将apache-tomcat.7.0.75.tar.gz直接解压到当前目录下。tar同时具有压缩的解压的功能，使用时根据参数和命令结构区分。



编译内核和安装内核.

依次输入这四条语句

sudo make mrproper

sudo make clean

sudo make menuconfig  

问题
> Unable to find the Ncurses libraries.
>>
>> You must install ncurses-devel in order
>> to use 'make menuconfig'

为了解决这个问题

我们在更新CentOS或者Ubuntu的内核时，执行make menuconfig可能看如这样的错误：

*** Unable to find the ncurses libraries or the
*** required header files.
*** ‘make menuconfig’ requires the ncurses libraries.
***
*** Install ncurses (ncurses-devel) and try again.

解决办法如下：
CentOS：
yum install -y ncurses-devel

Ubuntu：
sudo apt-get insatll ncurses-dev

遇到新问题
Error Downloading Packages:
  ncurses-libs-5.7-4.20090207.el6.i686: failure: Packages/ncurses-libs-5.7-4.20090207.el6.i686.rpm from base: [Errno 256] No more mirrors to try.
  ncurses-base-5.7-4.20090207.el6.i686: failure: Packages/ncurses-base-5.7-4.20090207.el6.i686.rpm from base: [Errno 256] No more mirrors to try.
  ncurses-devel-5.7-4.20090207.el6.i686: failure: Packages/ncurses-devel-5.7-4.20090207.el6.i686.rpm from base: [Errno 256] No more mirrors to try.


更换镜像源遇
1、首先备份一下系统原本的镜像配置文件  
[root@localhost ~]# mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup 

2、进入yum源配置文件所在文件夹  
[root@localhost ~]# cd /etc/yum.repos.d/   
需要切换到配置文件所在文件夹，否则会出错
3、确认centos的版本
4、下载yum源配置文件到上面的文件夹中

163镜像：
CentOS7
[root@localhost yum.repos.d]# wget http://mirrors.163.com/.help/CentOS7-Base-163.repo
CentOS6
[root@localhost yum.repos.d]# wget http://mirrors.163.com/.help/CentOS6-Base-163.repo
CentOS5
[root@localhost yum.repos.d]# wget http://mirrors.163.com/.help/CentOS5-Base-163.repo

阿里云镜像（阿里云不太好用，你们可以自己尝试一下，我也不知道什么问题）：
CentOS7
[root@localhost ~]# wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo

CentOS6
[root@localhost ~]# wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-6.repo

CentOS5
[root@localhost ~]# wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-5.repo


5、运行yum makecache生成缓存
[root@localhost ~]# yum makecache
 
6、更新系统，则会显示源信息
[root@localhost ~]# yum -y update


遇到新问题
[root@localhost yum.repos.d]# wget http://mirrors.163.com/.help/CentOS6-Base-163.repo
--2020-07-01 05:14:31--  http://mirrors.163.com/.help/CentOS6-Base-163.repo
Resolving mirrors.163.com... failed: Name or service not known.
wget: unable to resolve host address “mirrors.163.com”
[root@localhost yum.repos.d]# 


错误
Determining IP information for eth0... failed; no link present.  Check cable?
                                                           [FAILED]
RTNETLINK answers: File exists
RTNETLINK answers: File exists
RTNETLINK answers: File exists
RTNETLINK answers: File exists
RTNETLINK answers: File exists
RTNETLINK answers: File exists
RTNETLINK answers: File exists
RTNETLINK answers: File exists
RTNETLINK answers: File exists
[root@localhost yum.repos.d]# ping 192.168.1.1
connect: Network is unreachable


ifconfig 查看配置

[root@localhost yum.repos.d]# ifconfig
eth0      Link encap:Ethernet  HWaddr 00:0C:29:57:75:8E  
          inet6 addr: fe80::20c:29ff:fe57:758e/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:12 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:0 (0.0 b)  TX bytes:936 (936.0 b)
          Interrupt:19 Base address:0x2024 

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:16436  Metric:1
          RX packets:4811 errors:0 dropped:0 overruns:0 frame:0
          TX packets:4811 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:262624 (256.4 KiB)  TX bytes:262624 (256.4 KiB)


内核配置界面

下方框中的内容依次是：

  x x        General setup  --->                                                                    x x  常规设置
  x x    [*] Enable loadable module support  --->                                  x x 允许模块加载支持  
  x x    [*] Enable the block layer  --->                                                      x x  允许块设备支持
  x x        Processor type and features  --->                                            x x  处理器类型和功能
  x x        Power management and ACPI options  --->                         x x  电源管理和ACPI选项
  x x        Bus options (PCI etc.)  --->                                                        x x  总线选项（PCI等）
  x x        Executable file formats / Emulations  --->                              x x  可执行文件格式/仿真
  x x    -*- Networking support  --->                                                          x x  网络支持
  x x        Device Drivers  --->                                                  x x  设备驱动
  x x        Firmware Drivers  --->                                             x x  固件驱动
  x x        File systems  --->                                                    x x  文件系统
  x x        Kernel hacking  --->                                                x x  内核监视
  x x        Security options  --->                                              x x  安全选项
  x x    -*- Cryptographic API  --->                                         x x  密码API
  x x    [*] Virtualization  --->                                                   x x  虚拟化
  x x        Library routines  --->                                              x x  程序库程序
  x x    ---                                                                                   x x  
  x x        Load an Alternate Configuration File                 x x  加载备用配置文件
  x x        Save an Alternate Configuration File                 x x  保存备用配置文件
————————————————
版权声明：本文为CSDN博主「我在全球村」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/julius_lee/java/article/details/10989429



[root@localhost linux-2.6.11.10]# make modules_install
  INSTALL arch/i386/crypto/aes-i586.ko
cp: cannot stat `arch/i386/crypto/aes-i586.ko': No such file or directory
make[1]: *** [arch/i386/crypto/aes-i586.ko] Error 1
make: *** [_modinst_] Error 2
[root@localhost linux-2.6.11.10]# 


1. 下载内核解压
2. 修改内核文件
3. arch/x86/kernel/syscall_table
4. 