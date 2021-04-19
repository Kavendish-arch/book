###1.jsp
1. 指令
	* 作用：用于配置jsp页面，导入资源文件
	* 格式：<%@ 执行名称 属性名=属性值 属性名=属性值 %>
	* 分类: 
1. page:配置jsp页面 
	* contentType: response.setContentType()页面的编码 pageEnconding, language:语言java,buffer:
	* import:导包
	* errorPage,    错误跳转到 
	* isErrorPage,  标识当前是错误页面
2. include：页面包含，导入资源文件
	* <%@include file="top.jsp"%>
3. taglib：导入资源
	* <%@ taglib prefix="" uri="路径" %>
    * prefix 前缀，自定义
2. 注释
		<!----> html注释
		<%%>
		<%----%> jsp注释
3. *九大内置对象* 在jsp内置不需要创建，9类 
		变量名			
	* pageContext 		pageContext			当前页面共享数据，包括其他八个
	* request			HttpServletRequest	一次请求多个资源，转发
	* sessioin			HttpSession			一次会话多个请求间
	* application		ServletContext		多个用户间共享数据
	* 域对象
	* response			HttpServletResponse	响应对象
	* page				Object				当前页面（servlet）对象
	* out				JspWriter			输出对象，对象输出到页面上
	* config			ServletConfig		Servlet的配置对象
	* exception isErrorpage true Throwable	异常对象
    request     请求对象　 类型 javax.servlet.ServletRequest 作用域 Request
    response    响应对象 类型 javax.servlet.SrvletResponse 作用域 Page
    pageContext 页面上下文对象 类型 javax.servlet.jsp.PageContext 作用域 Page
    session     会话对象 类型 javax.servlet.http.HttpSession 作用域 Session
    application 应用程序对象 类型 javax.servlet.ServletContext 作用域 Application
    out         输出对象 类型 javax.servlet.jsp.JspWriter 作用域 Page
    config      配置对象 类型 javax.servlet.ServletConfig 作用域 Page
    page        页面对象 类型 javax.lang.Object 作用域 Page
    exception   例外对象 类型 javax.lang.Throwable 作用域 page
## Jsp生命周期
JSP编译 当浏览器请求JSP页面时，JSP引擎会首先去检查是否需要编译这个文件。如果这个文件没有被编译过，或者在上次编译后被更改过，则编译这个JSP文件。
* 编译的过程包括三个步骤：
    解析JSP文件
    将JSP文件转为servlet
    编译servlet
1. JSP初始化 容器载入JSP文件后，它会在为请求提供任何服务前调用jspInit()方法。
2. 如果您需要执行自定义的JSP初始化任务，复写jspInit()方法就行了，就像下面这样：

public void jspInit(){
  // 初始化代码
}
一般来讲程序只初始化一次，servlet也是如此，通常情况下您可以在jspInit()方法中初始化数据库连接、打开文件和创建查询表。

2. JSP执行 这一阶段描述了JSP生命周期中一切与请求相关的交互行为，直到被销毁。
当JSP网页完成初始化后，JSP引擎将会调用_jspService()方法。
_jspService()方法需要一个HttpServletRequest对象和一个HttpServletResponse对象作为它的参数，就像下面这样：
void _jspService(HttpServletRequest request,
                 HttpServletResponse response)
{
   // 服务端处理代码
}
_jspService()方法在每个request中被调用一次并且负责产生与之相对应的response，并且它还负责产生所有7个HTTP方法的回应，比如GET、POST、DELETE等等。

3. JSP清理
JSP生命周期的销毁阶段描述了当一个JSP网页从容器中被移除时所发生的一切。
jspDestroy()方法在JSP中等价于servlet中的销毁方法。当您需要执行任何清理工作时复写jspDestroy()方法，比如释放数据库连接或者关闭文件夹等等。
jspDestroy()方法的格式如下：
public void jspDestroy()
{
   // 清理代码
}
###2.MVC开发模式
1. jsp演变
		1. servlet，使用response输出标签数据
		2. jsp简化了servlet的开发 过量java代码，html代码
		3. MVC 开发模式
			M:Model,模型 javaBean 具体的业务操作，查询数据库，封装对象
			V:View视图 JSP 展示数据
			C:Controller控制器 Servlet 
				获取用户输入 调用模型 数据交给视图展示
3. EL表达式
    1. 概念  Expression Language 表达式
    2. 作用 替换，简化jsp 中 java 代码书写
    3. 语法 ${}
    4. 注意： jsp默认支持el表达式，
        1. 设置 jsp 中的 isElIgnored="true" 忽略el表达式
        2. \${} 忽略当前el表达式
    5. 使用
        1. 运算
            1. 算数运算 
            2. 比较运算
            3. 逻辑运算
            4. 空运算符 判断字符串，集合，数组 是否为空 ，长度是否为0
                ${empty list}
        2. 获取值
            1. 从域对象中获取值，
            2. 语法：
                1. ${域名，键名} 从指定的域中获取指定键的值
                    域名称： pageScope pageContext
                    requestScope request
                    sessionScope session
                    applicationScope application(ServletContext)
                
4. JSTL标签 jsp standard tab libraries
    * 核心标签库
    * 格式化标签库
    分页功能
5. 三层架构


