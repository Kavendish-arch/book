1.打开文件

vi filename

以下所有输入均在命令模式下： 

2.转到文件结尾

G 

或转到第9行

9G 

3.删除所有内容(先用G转到文件尾) ，使用：

:1,.d 

或者删除第9行到第200行的内容(先用200G转到第200行) ，使用

:9,.d

4.删除光标所在处字符

x

5.删除光标所在前字符（大写 X ）

X

6.删除到下一个单词开头

dw

7.删除到本单词末尾

de

8.删除到本单词末尾包括标点在内

dE

9.删除到前一个单词

db

10.删除到前一个单词包括标点在内

dB

11.删除一整行

dd

12.删除光标位置到本行结尾

D d$

13.删除光标位置到本行开头

d0


Python字典遍历删除特定值

初始代码（此代码执行错误）：

#coding=utf-8
D={'Google':'www.google.com','Bairu':'www.baidu.com','Taobao':'www.taobao.com'}
for key,value in D.items():
    if value=='www.google.com':
        D.pop('Google')
    else:
        continue
print(D)
错误指示如下：
RuntimeError: dictionary changed size during iteration

分析原因：
遍历时不能修改字典元素，即不能在迭代的时候添加或删除属性, 只能更改属性值. 

解决方案：
因为在python3中dict.keys()是一个迭代器。迭代器在操作过程中，是不允许被修改的。
所以我们要把迭代器（data.keys()），改为一个list（非迭代器），这样我们就可以对字典操作了。
其实这里我们通过list()已经把for循环迭代的对象，由原来的data.keys()变为了一个由data.keys()组成的一个list()数据了。

代码修改如下
#coding=utf-8
D={'Google':'www.google.com','Bairu':'www.baidu.com','Taobao':'www.taobao.com'}
for key in list(D.keys()):
    if D[key]=='www.google.com':
        del D[key]
        continue
print(D)
#输出：{'Bairu': 'www.baidu.com', 'Taobao': 'www.taobao.com'}
细心的朋友会发现，这里我们对data.keys()做了一个list（）操作，请大家想想为什么要做这样的一个操作呢？

因为在python3中dict.keys()是一个迭代器。迭代器在操作过程中，是不允许被修改的。所以我们要把迭代器（data.keys()），改为一个list（非迭代器），这样我们就可以对字典操作了。 
其实这里我们通过list()已经把for循环迭代的对象，由原来的data.keys()变为了一个由data.keys()组成的一个list()数据了。
