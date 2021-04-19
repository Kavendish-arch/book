# Step 2 How to Serve HTML or other Static Files
#angelapper/teaching/万门/JavaEE

### Add Folder 
/WebApp/resource/file
/WebApp/resource/static
![](Step%202%20How%20to%20Serve%20HTML%20or%20other%20Static%20Files/7627F93E-68C6-4CC1-B075-60E84AC406A1.png)

### Add Static Files under WebApp folder
try in root
try in file and static folder
and WEB-INF folder

### \src\main\webapp\WEB-INF\web.xml  change home page
```
<!-- webapp/WEB-INF/web.xml -->
<web-app xmlns="http://java.sun.com/xml/ns/javaee" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://java.sun.com/xml/ns/javaee/web-app_3_0.xsd"
	version="3.0">

	<display-name>To do List</display-name>

	<welcome-file-list>
		<welcome-file>index.html</welcome-file>
	</welcome-file-list>

</web-app>
```
