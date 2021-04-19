# Step 5 New Friend JSP
#angelapper/teaching/万门/JavaEE

### Jsp
### test.jsp
```
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=US-ASCII">
<title>Test!</title>
</head>
<%@ page import="java.util.Date" %>
<body>
<h3>Hi Joshua</h3><br>
<strong>Current Time is</strong>: <%=new Date() %>

</body>
</html>
```

### another way    LoginServlet.java 转发和重定向
```
package webapp;

import javax.servlet.http.HttpServlet;
import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet(urlPatterns = "/login.do")
public class LoginServlet extends HttpServlet {
	private LoginService service = new LoginService();
	
	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws IOException, ServletException {
		request.getRequestDispatcher("/WEB-INF/views/login.jsp").forward(request, response);
	}
```


## 转发和重定向 getRequestDispatcher()与sendRedirect()的区别
1. request.getRequestDispatcher()是请求转发，前后页面共享一个request，这个是在服务端运行的，对浏览器来说是透明的。
#### forward方式 转发 请求体
```request.getRequestDispatcher("/路径（可以是jsp路径也可以是servlet）") .forward(request, response);```
如：```request.getRequestDispatcher("/2.jsp）") .forward(request, response);```
request.getRequestDispatcher("/servlet/HomeServlet）") .forward(request, response);
　　Servlet页面跳转的路径是相对路径。forward方式只能跳转到本web应用中的页面上。
　　跳转后浏览器地址栏不会变化。
　　使用这种方式跳转，传值可以使用三种方法：url, request, session 
    url中带parameter，session，request.setAttribute
2. response.sendRedirect()是重新定向，前后页面不是一个request，而这个是在浏览器端运行的。
#### redirect 重定向方式 响应体
```response.sendRedirect("/a.jsp");```
页面的路径是相对路径: sendRedirect可以将页面跳转到任何页面，不一定局限于本web应用中，如：
response.sendRedirect("URL");
跳转后浏览器地址栏变化。
这种方式要传值出去的话，只能在url中带parameter或者放在session中，无法使用request.setAttribute来
传递。所以该方式只适用于无传值跳转


