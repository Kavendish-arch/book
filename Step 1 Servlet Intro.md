# Step 1 Servlet Intro
#angelapper/teaching/万门/JavaEE

## Servlet 
 
### \src\main\java\webapp\HomeServlet.java
```
package webapp;
/**
 * we create our first servlet application 
 * https://jcp.org/aboutJava/communityprocess/mrel/jsr245/index2.html
 * https://jcp.org/aboutJava/communityprocess/final/jsr369/index.html
 * https://kodejava.org/how-do-i-define-a-servlet-with-webservlet-annotation/
 * 
 * @WebServlet(
 *       name = "HomeServlet",
 *       description = "This is my first annotated servlet",
 *       urlPatterns = "/home.do"
 * 
 * )
 * 精确匹配 /home,扩展名匹配 *.jsp,路径匹配 /home/*
 */
//Java Platform, Enterprise Edition (Java EE) 
//Servlet ?
//a request-response programming model.

//1. extends javax.servlet.http.HttpServlet
//2. @WebServlet(urlPatterns = "/home.do")
//3. doGet(HttpServletRequest request, HttpServletResponse response)
//4. response?

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet(urlPatterns = "/home.do")
public class HomeServlet extends HttpServlet {

	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException {
		//response.setContentType("text/html;charset=utf-8");
		PrintWriter out = response.getWriter(); // ISO8859-1
		out.println("<html>");
		out.println("<head>");
		out.println("<title>Data Application Lab!!!!!!!!</title>");
		out.println("</head>");
		out.println("<body>");
		out.println("My First Servlet 中文");
		out.println("</body>");
		out.println("</html>");
	}

}
```

### POM
```
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.dataapplab</groupId>
  <artifactId>dal-servlet</artifactId>
  <version>0.0.1-SNAPSHOT</version>
  <packaging>war</packaging>
	<dependencies>
		<dependency>
			<groupId>javax</groupId>
			<artifactId>javaee-web-api</artifactId>
			<version>8.0</version>
			<scope>provided</scope>
		</dependency>
	</dependencies>
	
	<build>
		<pluginManagement>
			<plugins>
				<plugin>
					<groupId>org.apache.maven.plugins</groupId>
					<artifactId>maven-compiler-plugin</artifactId>
					<version>3.2</version>
					<configuration>
						<verbose>true</verbose>
						<source>1.8</source>
						<target>1.8</target>
						<showWarnings>true</showWarnings>
					</configuration>
				</plugin>
				<plugin>
					<groupId>org.apache.tomcat.maven</groupId>
					<artifactId>tomcat7-maven-plugin</artifactId>
					<version>2.2</version>
					<configuration>
						<path>/</path>
						<contextReloadable>true</contextReloadable>
					</configuration>
				</plugin>
			</plugins>
		</pluginManagement>
	</build>	  
</project>
```

### \src\main\webapp\WEB-INF\web.xml
```
<!-- webapp/WEB-INF/web.xml -->
<web-app xmlns="http://java.sun.com/xml/ns/javaee" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
	version="4.0">

	<display-name>Data Application Lab</display-name>

	<welcome-file-list>
	    <welcome-file>home.do</welcome-file>
	</welcome-file-list>
</web-app>
```

http无状态
会话技术 cookies 浏览器缓存