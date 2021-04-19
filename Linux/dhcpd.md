
# dhcpd
```
[root@linux-a ~]# vim /etc/dhcpd.conf

/dhcpd.conf
ddns-update-style interim;
ignore client-updates;
subnet 192.168.124.0 netmask 255.255.255.0 {
# --- default gateway
        option routers                  192.168.124.1;
        option subnet-mask              255.255.255.0;

        option time-offset              -18000; # Eastern Standard Time
#       option ntp-servers              192.168.1.1;
#       option netbios-name-servers     192.168.1.1;
# --- Selects point-to-point node (default is hybrid). Don't change this unless
# -- you understand Netbios very well
#       option netbios-node-type 2;

        range dynamic-bootp 192.168.124.200 192.168.124.230;
        default-lease-time 21600;
        max-lease-time 43200;

        # we want the nameserver to appear at a fixed address
        host www {
                hardware ethernet 12:34:56:78:AB:CD;
                fixed-address 207.175.42.254;
        }
}
```
dhcpd.conf参数说明
---------------------------------------------------
/etc/dhcpd.conf通常包括三部分：parameters、declarations 、option。
1. DHCP配置文件中的parameters（参数）：表明如何执行任务,是否要执行任务,或将哪些网络配置选项发送给客户
ddns-update-style,配置DHCP-DNS 互动更新模式。 
default-lease-time,指定确省租赁时间的长度,单位是秒。 
max-lease-time,指定最大租赁时间长度,单位是秒。 
hardware,指定网卡接口类型和MAC地址。 
server-name,通知DHCP客户服务器名称。 
get-lease-hostnames flag,检查客户端使用的IP地址。 
fixed-address ip,分配给客户端一个固定的地址。 
authritative,拒绝不正确的IP地址的要求。

2. DHCP配置文件中的declarations （声明）：用来描述网络布局、提供客户的IP地址等
shared-network,用来告知是否一些子网络分享相同网络。 
subnet,描述一个IP地址是否属于该子网。 
range,起始IP 终止IP 提供动态分配IP 的范围。 
host,主机名称 参考特别的主机。 
group,为一组参数提供声明。 
allow unknown-clients;deny unknown-client,是否动态分配IP给未知的使用者。 
allow bootp;deny bootp,是否响应激活查询。 
allow booting;deny booting,是否响应使用者查询。 
filename, 开始启动文件的名称. 应用于无盘工作站。 
next-server,设置服务器从引导文件中装如主机名,应用于无盘工作站。

3. DHCP配置文件中的option（选项）：用来配置DHCP可选参数,全部用option关键字作为开始
subnet-mask,为客户端设定子网掩码。 
domain-name,为客户端指明DNS名字。 
domain-name-servers,为客户端指明DNS服务器IP地址。 
host-name,为客户端指定主机名称。 
routers,为客户端设定默认网关。 
broadcast-address,为客户端设定广播地址。 
ntp-server,为客户端设定网络时间服务器IP地址。 
time－offset,为客户端设定和格林威治时间的偏移时间,单位是秒。
注意：如果客户端使用的是视窗操作系统,不要选择"host-name"选项,即不要为其指定主机名称

 

# 启动和检查DHCP服务器
使用命令启动DHCP服务器：
#service dhcpd start

关闭DHCP服务器：
#service dhcpd stop

重启DHCP服务器：
#service dhcpd restart
使用ps命令检查dhcpd进程：
#ps -ef | grep dhcpd
root      2402     1 0 14:25 ?        00:00:00 /usr/sbin/dhcpd
root      2764 2725 0 14:29 pts/2    00:00:00 grep dhcpd
使用检查dhcpd运行的端口：
# netstat -nutap | grep dhcpd
udp   0 0 0.0.0.0:67         0.0.0.0:*              2402/dhcpd

配置DHCP客户端

通常网管员使用选择手工配置 DHCP 客户,需要修改 /etc/sysconfig/network 文件来启用联网；
并修改 /etc/sysconfig/network-scripts 目录中每个网络设备的配置文件。
在该目录中,每个设备都有一个叫做 ifcfg-eth？ 的配置文件,eth？是网络设备的名称。
 如eth0等。如果你想在引导时启动联网,NETWORKING 变量必须设为 yes。 
除了此处之外/etc/sysconfig/network 文件应该包含以下行：

NETWORKING=yes
DEVICE=eth0
BOOTPROTO=dhcp
ONBOOT=yes

#启动失败的原因是dhcp服务器配置的IP地址和默认配置文件里定义的地址段不相同。

#在启动DHCP服务之前，需要给DHCP Server配置一个静态的IP地址

# 配置网卡IP地址命令:

Usage: ifconfig <EthernetName> <IPADDR>[/<prefixlen>]

例如:ifconfig eth2 192.168.1.1/24

DHCP服务,添加开机自启动:

chkconfig dhcpd on #添加开机自启动

chkconfig --list dhcpd #检查

主配置文件参数说明:

可以看出整个配置文件分成全局和局部两个部分。但是并不容易看出哪些属于参数，哪些属于声明和选项。

注释信息 以#开头 

配置信息 每行以;结束,大括号所在行除外

--- /usr/share/doc/dhcp/dhcpd.conf ---

# 定义全局配置，通用于所有支持的网络选项.

option domain-name "example.org"; #定义客户端所属域

option domain-name-servers ns1.example.org, ns2.example.org;#为客户端指定DHS服务器地址,有多个dns服务器时,使用,间隔

default-lease-time 600; #定义默认租约时长

当租约时长过去50%时:发送续约请求。(续不上继续用)

当租约时长过去87.5%:再次发送续约请求。(续不上找别人)

DHCP工作站除了在开机的时候发出 DHCPrequest 请求之外，在租约期限一半的时候也会发出 DHCPrequest ，如果此时得不到 DHCP服务器的确认的话，工作站还可以继续使用该IP；当租约期过了87.5%时，如果客户机仍然无法与当初的DHCP服务器联系上，它将与其它 DHCP服务器通信。如果网络上再没有任何DHCP协议服务器在运行时，该客户机必须停止使用该IP地址，并从发送一个Dhcpdiscover数据包开始，再一次重复整个过程。要是您想退租，可以随时送出 DHCPRELEASE 命令解约，就算您的租约在前一秒钟才获得的。

max-lease-time 7200;  #定义最大时长(当客户端没有想DHCP Server续约成功时,客户机可以使用这个IP的最大时间)

作用：定义客户端IP租约时间的最大值，当客户端超过租约时间，却尚未更新IP 时，最长可以使用该IP 的时间；

比如，机器在开机获得IP地址后，然后关机了。这时，当时间过了default-lease-time 600秒后，没有机器向DHCP续约，DHCP会保留7200秒，保留此IP地址不用于分配给其它机器。 当超过7200秒后，将不再保留此IP地址给此机器。

注意:default-lease-time 和 max-lease-time都是以秒为单位的租约时间，该项参数可以作用在全局配置中，也可以作用在局部配置中。

# 使用如下设置启动/关闭全面的动态域名更新

#ddns-update-style none; #dns更新样式none --> 不更新

#authoritative; #当DHCP服务器是本地局域网唯一时,需取消此行备注

log-facility local7; #日志类型local7

# 没有服务将在这个子网,但宣称它帮助DHCP服务器理解网络拓扑。
subnet 10.152.187.0 netmask 255.255.255.0 {

}

# This is a very basic subnet declaration.
# 基本的作用域声明
subnet 10.254.239.0 netmask 255.255.255.224 {

  range 10.254.239.10 10.254.239.20;

  option routers rtr-239-0-1.example.org, rtr-239-0-2.example.org;

}

# A slightly different configuration for an internal subnet.

# 配置内部子网 通用模块

subnet 10.5.5.0 netmask 255.255.255.224 { #定义作用域

  range 10.5.5.26 10.5.5.30; #地址池

  option domain-name-servers ns1.internal.example.org; #dns地址

  option domain-name "internal.example.org"; #域名

  option routers 10.5.5.1; #网关

  option broadcast-address 10.5.5.31; #广播地址

  default-lease-time 600; #租约时长

  max-lease-time 7200; #租约最大时长

}

Sub net：

声明一般用来指定IP 作用域、定义为客户端分配的IP 地址池等等

声明格式如下：

subnet 网络号 netmask 子网掩码 {

选项或参数

}

注意：网络号必须与DHCP 服务器的网络号相同

range 起始IP 地址 结束IP 地址

作用：指定动态IP 地址范围

注意：可以在subnet（子网） 声明中指定多个range，但多个range 所定义IP 范围不能重复

option routers IP 地址

作用：为客户端指定默认网关

如：option routers 10.5.5.1;

option domain-name

作用：为客户端指定默认的域

option domain-name-servers IP 地址

作用：为客户端指定DNS 服务器地址

注意：option routers、option domain-name、option domain-name-servers选项可以用在全局配置中，也可以用在局部配置中。

# 为特定的主机分配专一的描述信息

host passacaglia {

  hardware ethernet 0:0:c0:5d:bd:95;

  filename "vmunix.passacaglia";

  server-name "toccata.fugue.com";

}

# 为特定主机绑定固定IP

host fantasia { #定义作用的主机名是fantasia

hardware ethernet 08:00:07:26:c0:a5;#主机网卡mac地址

  fixed-address fantasia.fugue.com; #绑定的IP地址或域名

}

# 为foo的组分配IP地址10.17.224.0网段,为其他的组分配10.0.29.0网段

class "foo" {

match if substring (option vendor-class-identifier, 0, 4) = "SUNW";

} #这行,没看懂!!!substring (option vendor-class-identifier, 0, 4)

shared-network 224-29 {

  subnet 10.17.224.0 netmask 255.255.255.0 {

    option routers rtr-224.example.org;

  }

subnet 10.0.29.0 netmask 255.255.255.0 {
option routers rtr-29.example.org;

}
pool {
    allow members of "foo";
    range 10.17.224.10 10.17.224.250;
}

pool {
    deny members of "foo";
    range 10.0.29.10 10.0.29.230;
  }
}
实战:使用DHCP服务,为客户端分配IP地址,并实现IP绑定

注释:在实验过程中,使用xshell进行实验,为了避免xshell断开连接,对两台虚拟机分别添加了一块新的网卡,并保证两块网卡在一个局域网中.
xiaogan120.cn  ---> ifconfig eth1 192.168.1.1/24
xiaogan121.cn  ---> 添加一块网卡后,需要对新的网卡建立一个配置文件,修改mac地址等信息





