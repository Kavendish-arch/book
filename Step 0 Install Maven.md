# Step 0 Install Maven
#angelapper/teaching/万门/JavaEE

### Download Maven
change Other mirrors: to http://mirrors.tuna.tsinghua.edu.cn/apache/
http://maven.apache.org/download.cgi

Binary zip archive:	apache-maven-3.5.4-bin.zip

### Unzip to target foldr
例如：F:\java零基础特训班\eclipse-standard-kepler-SR2-win32-x86_64\apache-maven-3.5.4

### 创建新的环境变量
MAVEN_HOME = F:\java零基础特训班\eclipse-standard-kepler-SR2-win32-x86_64\apache-maven-3.5.4
MAVEN_OPTS = -Xms256m -Xmx512m

### 给Path添加
%MAVEN_HOME%\bin