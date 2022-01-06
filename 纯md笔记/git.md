## 安装 Git
### Mac系统安装Git bash
* 安装Xcode软件
### Windows系统安装Git bash
*  Git官网：https://git-scm.com/
• 测试
*  $ git –version
*  $ cd Desktop
*  $ mkdir projects
*  $ cd projects
*  $ touch 1.txt
*  $ ls

### Linux Debian或Ubuntu Linux，
通过一条sudo apt-get install git 直接安装
其他Linux版本，可以直接通过源码安装。
先从Git官网下载源码，然后解压，
依次输入：./config，make，sudo make install这几个命令安装就好了。
安装完成后，配置用户名，邮箱
$ git config --global user.name "Your Name"
$ git config --global user.email "email@example.com"


## 配置SSH。
生成密匙
ssh-keygen -C "邮箱" -t rsa
~.ssh目录
第1步：创建SSH Key。在用户主目录下，看看有没有.ssh目录，
如果有，再看看这个目录下有没有id_rsa和id_rsa.pub这两个文件，如果已经有了，可直接跳到下一步。
如果没有，打开Shell（Windows下打开Git Bash），创建SSH Key：
$ ssh-keygen -t rsa -C "youremail@example.com"
你需要把邮件地址换成你自己的邮件地址，然后一路回车，使用默认值即可，由于这个Key也不是用于军事目的，所以也无需设置密码。
如果一切顺利的话，可以在用户主目录里找到.ssh目录，里面有id_rsa和id_rsa.pub两个文件，
这两个就是SSH Key的秘钥对，id_rsa是私钥，不能泄露出去，id_rsa.pub是公钥，可以放心地告诉任何人。

第2步：登陆GitHub，打开“Account settings”，“SSH Keys”页面：
然后，点“Add SSH Key”，填上任意Title，在Key文本框里粘贴id_rsa.pub文件的内容：
点“Add Key”，你就应该看到已经添加的Key：
为什么GitHub需要SSH Key呢？因为GitHub需要识别出你推送的提交确实是你推送的，
而不是别人冒充的，而Git支持SSH协议，所以，GitHub只要知道了你的公钥，就可以确认只有你自己才能推送。

当然，GitHub允许你添加多个Key。假定你有若干电脑，你一会儿在公司提交，一会儿在家里提交，
只要把每台电脑的Key都添加到GitHub，就可以在每台电脑上往GitHub推送了。

现在，我们根据GitHub的提示，在本地的learngit仓库下运行命令：
$ git remote add origin github路径
$ git remote add origin github路径


添加后，远程库的名字就是origin，这是Git默认的叫法，也可以改成别的，但是origin这个名字一看就知道是远程库。
下一步，就可以把本地库的所有内容推送到远程库上：
$ git push -u origin master
好啦，静静等待git把你的代码Push上去吧~是不是很简单？

## 配置用户名和邮箱
• 命令
* git config –global user.name “米斯特吴” 
* git config –global user.email 27732357@qq.com
* git config –list
* git config user.name
* git help

## 管理git项目
• 命令
* git init
* git init [name]
* git add [filename]
* git add .

放弃追踪命令
* git rm --cached <file>

commit的作用是什么
• 命令
* git commit
* git commit -m 
* git commit -am

log追踪
• 命令
* git log
* git log –p -2 * git log --author
* git log --online
* git log --graph
* git log --pretty=online
* git log --pretty=format

追踪文件修改前后的区别
• 命令
* git diff
* git diff --stage


文件删除、重命名、移动
• 命令
*  git rm [filename] 文件删除
*  git mv [oldname] [newname] 文件重命名
*  git mv [filename] stuff/pretty.txt 文件移动

文件忽略
• 命令
*  .gitignore
*  /node_modules 忽略node_modules文件夹下所有文件
*  *.log 忽略.log结尾的文件
*  *.zip 忽略.zip结尾的文件
*  git rm –r --cached.

项目演练
• 命令
* git init
* git status
* git add .
* git commit -m ‘描述’ 
* .gitignore

一键还原 项目拉取
命令 切换分支
* git checkout - - [filename] 恢复到上一次的状态
 
撤销追踪操作与文件还原
 
• 命令
* git reset HEAD [filename] 撤销当前文件的追踪
* git checkout - - [filename]

版本回退
git restore 取消修改 
• 命令
* git reset - -hard HEAD^ 回退到上一个版本
* git reset - -hard HEAD^^ 回退到上上个版本
* git reset - -hard HEAD [hash号] 回退到指定hash的版本
* git reflog 指针理解
 
回到旧版本
版本回退   v1 -> v2 -> v3 不保留后面的版本
回到旧版本 v1 -> v2 -> v3 -> v4(v2) 保留版本
• 命令
* git log
* git checkout [hash] - - [filename]


## 建立切换删除分支
• 命令
* git branch [name]              创建分支
* git checkout [branch name]     切换分支
* git checkout –b [branch name]  新建切换
* git branch [name] -d           删除分支
* git branch [name] -D

理解分支到底是什么
• 分支概述
*  什么是分支
*  分支的作用是什么

如何正确的合并分支
• 命令
* git merge [branch name]


如何解决合并时发生的冲突
• 解决冲突
* git merge [branch name]
* git status 查看冲突原因
* git merge -abort 忽略合并
* 手动选择正确内容
*  git commit 


如何通过命令查看版本线图

• 命令
* git log
* git log -oneline
* git log -oneline -graph
* git log -oneline -graph -all
* git log -oneline -graph -[number]

快转机制的意义
• 快转机制的意义
* 快转实际就是当前master的将来时
* git merge branchname -no-ff

更多合并的方法
• 命令
* git merge -no-ff -no-commit [branchname] 
* git merge -no-ff -squash [branchname] 
* git merge -squash [branchname] 
* git reset –hard ORIG_HEAD

一次性删掉所有不想要的分支
• 命令
*  git branch -- merged | egrep -v "(^*|master|develop)" | xargs git branch -d
*  


创建和删除远端仓库
• 仓库信息
* 创建仓库
* 删除仓库

本地仓库推送到远端仓库
• 远端仓库
* git remote add origin url
* git remote
* git push -u origin master



主仓库作为服务器
• 仓库信息
* 主仓库做服务器
* 仓库配置

如何获取远端项目
• 命令
* git clone [远端仓库地址] * git clone --no-checkout
* git clone --bare [远端仓库地址]


