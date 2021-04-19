## 安装ros install
apt-get install python-rosinstall
rosdep init
rosdep update

Catkin建立ROS程序包
mkdir -p ~/catkin_ws/src
cd catkin_ws/src
catkin_init_workspace 建立工作空间
cd ~/catkin_ws && catkin_make
source devel /setup.bash写入环境变量

catkin 清除命令
    rosmake --target = clean

    \rm -rf devel build install 
    不要删除src目录会导致catkin源文件丢失
    
重新构建
    catkin_make
单独构建一个包
    catkin_make -- pkg package_name 


(base) root@ubuntu:/home/chen# rospack profile
Full tree crawl took 0.127184 seconds.
Directories marked with (*) contain no manifest.  You may
want to delete these directories.
To get just of list of directories without manifests,
re-run the profile with --zombie-only
-------------------------------------------------------------
0.124354   /opt/ros/kinetic/share
0.002301   /home/chen/catkin_ws/src
0.000891 * /opt/ros/kinetic/share/OpenCV-3.3.1-dev
0.000367 * /opt/ros/kinetic/share/doc
0.000039 * /opt/ros/kinetic/share/OpenCV-3.3.1-dev/haarcascades
0.000014 * /opt/ros/kinetic/share/OpenCV-3.3.1-dev/lbpcascades
0.000008 * /opt/ros/kinetic/share/doc/liborocos-kdl


-------------------------------------------------------------
    my_package/
      CMakeLists.txt
      package.xml

在catkin工作空间中的程序包
开发catkin程序包的一个推荐方法是使用catkin工作空间，但是你也可以单独开发(standalone)catkin 软件包。一个简单的工作空间也许看起来像这样：

    workspace_folder/        -- WORKSPACE
      src/                   -- SOURCE SPACE
        CMakeLists.txt       -- 'Toplevel' CMake file, provided by catkin
        package_1/
          CMakeLists.txt     -- CMakeLists.txt file for package_1
          package.xml        -- Package manifest for package_1
        ...
        package_n/
          CMakeLists.txt     -- CMakeLists.txt file for package_n
          package.xml        -- Package manifest for package_n
-------------------------------------------------------------

创建一个catkin程序包

本部分教程将演示如何使用catkin_create_pkg命令来创建一个新的catkin程序包以及创建之后都能做些什么。
首先切换到之前通过创建catkin工作空间教程创建的catkin工作空间中的src目录下：
# You should have created this in the Creating a Workspace Tutorial
$ cd ~/catkin_ws/src
现在使用catkin_create_pkg命令来创建一个名为'beginner_tutorials'的新程序包，这个程序包依赖于std_msgs、roscpp和rospy：
$ catkin_create_pkg beginner_tutorials std_msgs rospy roscpp
这将会创建一个名为beginner_tutorials的文件夹，这个文件夹里面包含一个package.xml文件和一个CMakeLists.txt文件，
这两个文件都已经自动包含了部分你在执行catkin_create_pkg命令时提供的信息。
catkin_create_pkg命令会要求你输入package_name，如果有需要你还可以在后面添加一些需要依赖的其它程序包：
# This is an example, do not try to run this
# catkin_create_pkg <package_name> [depend1] [depend2] [depend3]
catkin_create_pkg命令也有更多的高级功能，这些功能在catkin/commands/catkin_create_pkg中有描述。 
(base) root@ubuntu:/home/chen/catkin_ws# cd src/
(base) root@ubuntu:/home/chen/catkin_ws/src# catkin_create_pkg beginner_tutorials std_msgs rospy roscpp
Created file beginner_tutorials/CMakeLists.txt
Created file beginner_tutorials/package.xml
Created folder beginner_tutorials/include/beginner_tutorials
Created folder beginner_tutorials/src
Successfully created files in /home/chen/catkin_ws/src/beginner_tutorials. Please adjust the values in package.xml.
(base) root@ubuntu:/home/chen/catkin_ws/src# ls
beginner_tutorials  CMakeLists.txt
(base) root@ubuntu:/home/chen/catkin_ws/src# cd beginner_tutorials/
(base) root@ubuntu:/home/chen/catkin_ws/src/beginner_tutorials# ls
CMakeLists.txt  include  package.xml  src
(base) root@ubuntu:/home/chen/catkin_ws/src/beginner_tutorials# 


roscore
{
    (base) root@ubuntu:/opt/ros/kinetic/lib# roscore
    ... logging to /root/.ros/log/adf036dc-0f67-11ea-ad17-000c29e937a4/roslaunch-ubuntu-4684.log
    Checking log directory for disk usage. This may take awhile.
    Press Ctrl-C to interrupt
    Done checking log file disk usage. Usage is <1GB.

    started roslaunch server http://ubuntu:44335/
    ros_comm version 1.12.14


    SUMMARY
    ========

    PARAMETERS
    * /rosdistro: kinetic
    * /rosversion: 1.12.14

    NODES

    auto-starting new master
    process[master]: started with pid [4694]
    ROS_MASTER_URI=http://ubuntu:11311/

    setting /run_id to adf036dc-0f67-11ea-ad17-000c29e937a4
    process[rosout-1]: started with pid [4708]
    started core service [/rosout]
        
}
rosrun
{
打开一个新的终端, 可以使用 rosnode 像运行 roscore 一样看看在
运行什么...
注意: 当打开一个新的终端时，你的运行环境会复位，同时你的~/.bashrc
文件会复原。如果你在运行类似于rosnode的指令时出现一些问题，也许你需要添加
一些环境设置文件到你的~/.bashrc或者手动重新配置他们。
rosnode 显示当前运行的ROS节点信息。rosnode list 指令列出活跃的节点:
(base) root@ubuntu:/home/chen/catkin_ws/build# rosnode list
/rosout
    你会看到:
这表示当前只有一个节点在运行: rosout。因为这个节点用于收集和记录节点调
试输出信息，所以它总是在运行的。
rosnode info 命令返回的是关于一个特定节点的信息。
$ rosnode info /rosout
这给了我们更多的一些有关于rosout的信息, 例如，事实上由它发布
/rosout_agg.
    ------------------------------------------------------------------------
    Node [/rosout]
    Publications:
     * /rosout_agg [rosgraph_msgs/Log]

    Subscriptions:
     * /rosout [unknown type]

    Services:
     * /rosout/set_logger_level
     * /rosout/get_loggers

    contacting node http://machine_name:54614/ ...
    Pid: 5092
    现在，让我们看看更多的节点。为此，我们将使用rosrun 弹出另一个节点。 
}



{
    rosrun 允许你使用包名直接运行一个包内的节点(而不需要知道这个包的路径)。

用法:

$ rosrun [package_name] [node_name]

现在我们可以运行turtlesim包中的 turtlesim_node。

然后, 在一个 新的终端:

$ rosrun turtlesim turtlesim_node

你会看到 turtlesim 窗口:

    turtlesim.png 

注意: 这里的 turtle 可能和你的 turtlesim 窗口不同。别担心，这里有许多版本的turtle ，而你的是一个惊喜!（一个可爱的小彩蛋～）

在一个 新的终端:

$ rosnode list

你会看见类似于:

    /rosout
    /turtlesim

ROS的一个强大特性就是你可以通过命令行重新配置名称。

关闭 turtlesim 窗口停止运行节点 (或者回到rosrun turtlesim终端并使用`ctrl

-C`)。现在让我们重新运行它，但是这一次使用Remapping Argument改变节点名称:

$ rosrun turtlesim turtlesim_node __name:=my_turtle

现在，我们退回使用 rosnode list:

$ rosnode list

    你会看见类似于:

    /rosout
    /my_turtle

注意: 如果你仍看到 /turtlesim在列表中，这可能意味着你在终端中使用ctrl-C停

止节点而不是关闭窗口，或者你没有$ROS_HOSTNAME环境变量，这在

Network Setup - Single Machine Configuration中有定义。你可以尝试清除rosnode

列表，通过: $ rosnode cleanup

我们可以看到新的/my_turtle 节点。使用另外一个 rosnode 指令, ping, 来

测试:

$ rosnode ping my_turtle

    rosnode: node is [/my_turtle]
    pinging /my_turtle with a timeout of 3.0s
    xmlrpc reply from http://aqy:42235/     time=1.152992ms
    xmlrpc reply from http://aqy:42235/     time=1.120090ms
    xmlrpc reply from http://aqy:42235/     time=1.700878ms
    xmlrpc reply from http://aqy:42235/     time=1.127958ms

回顾

本节所涉及的内容:

roscore = ros+core : master (provides name service for ROS) + rosout 
(stdout/stderr) + parameter server (parameter server will be introduced

later)

    rosnode = ros+node : ROS tool to get information about a node.
    rosrun = ros+run : runs a node from a given package. 

到这里，您已经了解了ROS节点是如何工作的，下一步，我们来了解一下
关闭turtlesim_node，请按下“Ctrl-C” 
}



  27 #include "ros/ros.h"
  28 #include "std_msgs/String.h"
  30 #include <sstream>

  35 int main(int argc, char **argv)
  36 {

  47   ros::init(argc, argv, "talker");

  54   ros::NodeHandle n;
  73   ros::Publisher chatter_pub = n.advertise<std_msgs::String>("chatter", 1000);
  75   ros::Rate loop_rate(10);
  81   int count = 0;
  82   while (ros::ok())
  83   {
  87     std_msgs::String msg;
  89     std::stringstream ss;
  90     ss << "hello world " << count;
  91     msg.data = ss.str();
  93     ROS_INFO("%s", msg.data.c_str());
 101     chatter_pub.publish(msg);
 103     ros::spinOnce();
 105     loop_rate.sleep();
 106     ++count;
 107   }

 110   return 0;
 111 }
    