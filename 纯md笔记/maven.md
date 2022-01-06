
maven仓库
maven中有中央仓库，本地仓库，私服三个概念
	1.中央仓库是maven给你提供的所有jar包的下载地址.网址：http://mvnrepository.com/
	2.本地仓库是你在中央仓库里下载好的jar包所保存的文件夹。
	3.私服相当于一个大型的本地仓库，一般在规模庞大的公司里才会有自己的私服。(阿里巴巴)
 
安装配置maven  官网:http://maven.apache.org/
1.解压你在maven下载到的压缩包，一般把它和jdk放在一起。
2.安装maven在电脑上(配置环境变量)
	鼠标右键点击计算机>点击属性>点击高级系统设置之后会弹出
	然后再点击环境变量会弹出：                                           
	这个时候你就可以点击新建配置maven_home,注意maven_home的变量值是你maven的压缩包的解压地址。
	配置完maven_home之后记得还需要修改path：在path的变量值最后加上%MAVEN_HOME%\bin
	但是在配置maven_home时，你得保证你的环境变量里面存在JAVA_HOME（配置jdk)。
	没有配置JAVA_HOME测试时会报错
	测试你的maven有没有安装成功。打开cmd，输入mvn -v
	如果出现的是：
		Apache Maven 3.6.1 (d66c9c0b3152b2e69ee9bac180bb8fcc8e6af555; 2019-04-05T03:00:29+08:00)
		Maven home: D:\Program Files\apache-maven-3.6.1-bin\apache-maven-3.6.1\bin\..
		Java version: 1.8.0_131, vendor: Oracle Corporation, runtime: C:\Program Files\Java\jdk1.8.0_131\jre
		Default locale: zh_CN, platform encoding: GBK
		OS name: "windows 10", version: "10.0", arch: "amd64", family: "windows"

二、在Eclipse上安装maven
	打开Eclipse点击window>prferences之后会弹出设置界面
	选择Maven
		installations:设置maven地址
	4.连接本地仓库
	第一步：你首先需要找到你的maven解压文件夹，然后打开conf子文件夹，然后编辑settings.xml
	第二步：回到eclipse中点击window再点击preferences                                         
	UserSettings:设置maven本地仓库位置
	
	Idea 
	File /Setting/Maven Maven home directory User setting file Local repository

三、tomcat
2. 安装Tomcat和配置：http://tomcat.apache.org/
在tomcat官网上下载tomcat安装版本，然后安装tomcat软件。http://tomcat.apache.org/download-80.cgi#8.5.5

（1）将下载的zip包解压到C盘：apache-tomcat-8.5.5
	目录结构
		Tomcat安装完成后的目录有
		bin------存放启动和关闭的tomcat脚本
		conf-----包含不同的配置文件
		work----存放jsp编译后产生的class文件
		webapp存放应用程序的目录
		log-----存放日志文件
		lib------存放tomcat所需要的jar文件
		doc-----存放各种Tomcat文档
（2）环境变量CATALINA_HOME、CATALINA_BASE、CATALINA_TMPDIR、path的设置。
		JAVA_HOME            E:\Java\jdk1.6.0_10
		CATALINA_BASE        E:\Java\apache-tomcat-6.0.29
		CATALINA_HOME        E:\Java\apache-tomcat-6.0.29
		TOMCAT_HOME          E:\Java\apache-tomcat-6.0.29


	到底CATALINA_HOME和CATALINA_BASE有什么区别呢，之前因为都是小打小闹的在服务器上安装一个tomcat就得了，
	然后根据前人的配置，将CATALINA_HOME和CATALINA_BASE两个值设为了tomcat的目录（其实此处描述很不精确），
	今天无意间看到了公司的安装文档说明，里面提到了多个tomcat实例运行的配置，才弄明白到底这两者之间有什么区别。

	我们可以从Tomcat 5.5的配置文档（http://tomcat.apache.org/tomcat-5.5-doc/config/host.html） 中找到答案：

	The description below uses the variable name $CATALINA_HOME to refer to the directory into which you have installed Tomcat 5, and is the base directory against which most relative paths are resolved. However, if you have configured Tomcat 5 for multiple instances by setting a CATALINA_BASE directory, you should use $CATALINA_BASE instead of $CATALINA_HOME for each of these references.

	从这段描述可以看出CATALINA_HOME和CATALINA_BASE的区别。简单的说，CATALINA_HOME是Tomcat的安装目录，
	CATALINA_BASE是Tomcat的工作目录。如果我们想要运行Tomcat的多个实例，但是不想安装多个Tomcat软件副本。
	那么我们可以配置多个工作目录，每个运行实例独占一个工作目录，但是共享同一个安装目录。
	Tomcat每个运行实例需要使用自己的conf、logs、temp、webapps、work和shared目录，因此CATALINA_BASE就 指向这些目录。 
	而其他目录主要包括了Tomcat的二进制文件和脚本，CATALINA_HOME就指向这些目录。
	如果我们希望再运行另一个Tomcat实例，那么我们可以建立一个目录，把conf、logs、temp、webapps、work和shared拷贝到该目录下，然后让CATALINA_BASE指向该目录即可。
	在一台服务器上，可以运行多个tomcat实例，不需要安装多个tomcat，可以采用不同的用户，以test用户为例，拷贝/usr/local/apache-tomcat-6.0.18目录到/home/test下，删除/home/test/apache-tomcat-6.0.18/bin子目录（此目录不需要），编辑/home/test/.bash_profile文件,设置CATALINA_HOME指向刚才的安装目录/usr/local/apache-tomcat-6.0.18,设置JAVA_HOME指向刚才的安装目录/usr/java/jdk1.6.0_11。设置CATALINA_BASE指向/home/test/apache-tomcat-6.0.18，设置CATALINA_OPTS跟/root/.bash_profile的一致（jmx管理端口用不同的端口号）

（3）启动Tomcat。

“开始”->“运行”->输入cmd，在命令提示符中输入 startup.bat，之后会弹出tomcat命令框，输出启动日志；
常见错误
	The CATALINA_HOME environment variable is not defined correctly This environment variable is needed 
	Neither the JAVA_HOME nor the JRE_HOME environment variable is defined
	At least one of these environment variable is needed to run this program
	打开tomcat/bin/ setclasspath.bat(win) setclasspath.sh(linux) 
	添加JAVA_HOME JRE_HOME(手动添加Java环境)
	set JAVA_HOME=
	set JRE_HOME=
	export JAVA_HOME=
	export JRE_HOME=

运行tomcat
	找到Tomcat安装路径，找到bin文件夹，手动点击startup.bat文件。
	打开浏览器输入http://localhost:8080/ ，如果进入tomcat欢迎界面，配置成功。

参照资料：
http://jingyan.baidu.com/article/870c6fc33e62bcb03fe4be90.html
http://www.jb51.net/article/51909.htm
http://jingyan.baidu.com/article/86f4a73e5be03237d65269ef.html

（4）软件发布
如果使用软件的话，他们默认的是把工程发布到tomcat的webapp文件夹下
C:\apache-tomcat-8.5.5\webapps
该部分暂时未使用。

四、Eclipse配置tomcat
	Windows/ Preferences/ Server/ Runtime Environments/Add/tomcat版本/路径、运行环境
	Idea
	run/edit Configurations/ Defualt/Tomcat Server/ Local