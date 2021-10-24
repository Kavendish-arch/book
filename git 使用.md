*  Git官网：https://git-scm.com/
• 测试
*  $ git –version
*  $ cd Desktop
*  $ mkdir projects
*  $ cd projects
*  $ touch 1.txt
*  $ ls


## 配置用户名和邮箱
• 命令
* git config –global user.name 
* git config –global user.email
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
* git log –p -2 
* git log --author
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


