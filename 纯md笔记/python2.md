# Python

## 配环境
Python Anaconda
Mysql WorkBench
PyCHarm
GitHub桌面

### Anaconda 虚拟环境
没有安装的

安装的

* 最近更新Anaconda遇到了更新下载速度慢的问题，于是从网上找了一些资料顺利解决，现在总结一下。
解决办法就是标题显示的“更换源”，这里更换成清华源，在清华大学开源镜像站里面是可以找到相应的源，以及使用帮助，这里再唠叨一下，做个搬运工。
在命令行输入：
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes
到这里，帮助结束，但是在CSDN等一些网站上看到，还要修改一下生成的.condarc文件，防止更新再次使用默认的国外源，具体如下：
conda config --show-sources
出现的第一行的文件路径就是控制镜像源的文件所在。（.condarc文件——conda配置文件）

显示如下：
==> C:\Users\username\.condarc <==
channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  - defaults
show_channel_urls: True
将其中的- defaults删除并保存即可。
可以执行conda info，检查是否修改成功

* Anaconda常用命令
1. 创建环境
>>>conda create --name newpy36 python=3.6
>>>conda create --name opencv python=3.6

2. 切换环境
>>>conda activate newpy36     #进入
>>>source activate newpy36
>>>conda deactivate newpy36   #脱出

3. 显示已安装环境
conda info --envs
conda info -e
conda env list
conda create --name new _env_name --clone copied_env_name复制环境
4. 删除安装环境
conda remove --name env_name --all 
5. 查找安装环境
conda search --full-name  pkg-name 
conda search pkg-name 
conda list 
conda install --name env_name pkg-name 

### tensorflow环境安装
conda create  -n tensorflow python=3.6
activate tensorflow 
pip --upgrade --ignore-installed tensorflow

import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))

### ubuntu 启动anaconda图形界面
source ~/anaconda3/bin/activate root
anaconda-navigator

conda install  -c anaconda anaconda-navigator
anaconda-navigator

* 如何设置Jupyter 登录密码  
1. 生成jupyter的配置文件：jupyter notebook --generate-config
2. 控制台继续输入：jupyter notebook password （会输入两次密码，用来验证）
3. 密码设置成功， 登录服务器： jupyter notebook   
在linux系统中，一些软件安装后没有桌面的快捷方式，我们可以直接输入命令来打开这些软件
1. Anaconda
打开终端输入 anaconda-navigator
2. IDEA 打开终端输入 idea


# 数组是什么

    以0开始开始索引
    连续的存储空间
    数组长度固定
    边界检查
    访问速度 O(1) 
    记录数组的第一个数据的地址，存放相同的数据所以所需空间相同sizeof(int)-> 快速计算出地址

linux 磁盘清理
apt-get autoremove 自动清理


### 数据库服务
    MySQL server
数据库客户端

## Python语法
## 变量
* 命名规则
1. 变量的命名 字母数字下划线
2. 保留字，表点，区分大小写
3. 大驼峰 类
4. 小驼峰 函数
5. 下划线 变量
6. 不用0o

* 变量基础操作
1. len() 长度
2. type() 判断类型
3. id() 输出地址
4. [0:10] 切片 只有可迭代类型才能切割，字典除外

### 数据类型
* 字符串，String 以及操作
1. 字符串 函数
    title() 首字符大写 upper() 大写 lower() 小写
2. 转义符 \t \n 
3. 字符串合并 + 连接字符串，加法
4. 字符串空白是有意义的，除非你声明 rstrip() 
* 数字 整数 浮点数 数字和字符串使用时 str()
    ag: "hello i'm" + str(age) + "years old"
以上加上元组：不可变型
变量名 : 内存地址 内存存储

### 变量转换
> str str() 转换为字符
> int int() 转换为整数
> float float() 转换为浮点
* 变量计算
* + - * / 
* //商， %余数 **幂

### 占位符
name =‘zhengzheng’
age = 28

* %占位符 适合简单的且有循序的占位
print(‘我的名字是%s，我的年龄是%d’%(name,age) 

* {} 和 format占位符  依次占位多个
print(‘我的名字是{0}，我的年龄是 {1}’.format(name,age) 

* f{name} 适合有明确对应关系的变量
print(f‘我的名字是{name}，我的年龄是 {age}’) 

## 数学函数
import math
abs() min max() ceil()向上取整 floor()向下取整 sqrt()开根号

## 注释 #

## 集合 列表 字典，可变型变量
## 特定元素(字符串、整数、浮点数、布尔、列表、元组、字典)组成的集合
    key = [] 列表 相当于数组
    key = () 元组 不可修改的列表
    key = {} 字典 key 对应 value

1. 列表内的每个元素（数据），遵守该数据类型的原有规则。比如字符串类型是要加引号‘’
2. 可以有多层嵌套，每一层嵌套为一个独立体存在
* 添加
    insert() 插入 append() 追加
* 删除 
    del 批量删除 , pop() 基于索引, remove() 基于值, clear() 清空列表
    1. 修改数据和查询数据“一线间”
    2. 圈定范围修改列表数据时，需要保证添加的数据为可迭代对象
    3. 注意pop ()默认为删除最后一位，可指定索引位置,并返回被删除的值
    4. remove() 基于值/数据删除数据，删除的是第一个匹配的数据，并非所有
* 修改、查询 使用下标
    list[0] = 
    list[2:4] = [] 基于索引范围修改数据
* 合并 
    +， extend 特别注意-extend()会直接改变当前变量内的值
* 排序
    sort() 特别注意-sort()会直接改变当前变量内的值, 
    sort(reverse=True) 倒序
    sorted(), reverse() 列表反转
* 长度 len() 长度， count() 数量统计

* 切片：
    players[0:3]
    copy_players = players[:] #复制列表
* 复制 copy(), deepcopy() 
    copy_players = players * 3 复制3遍
> 一组数据里有高度、有宽度可以叫做
    1. 矩阵
    2. 二维数组

2. 元组
注意列表和元组之间一个有趣的关系
列表 -> 元组 加锁
元组 -> 列表 解锁
列表和元组对比 
list VS tuple
声明      [ ]     ( )
索引      YES     YES
切片      YES     YES
追加元素    YES    NO
修改元素    YES    NO
删除元素    YES    NO
基于值反查索引 YES NO
包含关系查询 YES YES
3. 字典
    key - value 键和值对
不可变、不可重复：key
* 增加键（KEY）和值（Value
* 删除键（KEY）和值（Value）
* 基于键（KEY）改变值（Value）
* 基于键（KEY）查询值（Value）
* 注意：只能使用不可变类型作为键 
* 通常不使用数字 （int/float）作为键
————嵌套
    列表(字典)
    字典(列表)

## 运算
* 比较运算 == != > >= <= <
* 逻辑运算 and or not
* 成员运算 in, not in
* 身份运算 is, is not
## 布尔变量
逻辑运算得有可比性结果：true false 0,1

## 循环语句
* for magican in magicans(可迭代对象):
* for i in range(开始，截止，步长): 生成可迭代对象

* while 条件判断:
    break
    continue

## 条件语句
    if car == 'bus': python 比较时区分大写小写
    and 和 or
    if car == 'bus' and car
    if-else
    if-elif-else 

## 函数：
1. 形式参数 参数的名字 （类似变量名）- parameter
2. 实际参数 该参数的具体值(变量的那个值) - argument
3. 位置参数 按照参数位置取值 - positional
4. 关键字参数 就是一个标准的变量赋值的过程 5.默认参数 为函数预设的参数值
6. 参数组 可变参数和可变关键字-传入结构化数据类型（列表、元组、字典）
def function_name ():
    1.位置参数 不可以改变位置
    2.关键字参数
    3.默认值
    return 返回值
        1.简单值
        2.字典、列表
参数传递问题：
    可变变量和不可变量
    不建议对可变变量在函数内部进行更改，使用函数返回值重新赋值
def test( grade gender=‘男’ *args name **subject ) :




