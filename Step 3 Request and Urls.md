# Step 3 Request and Urls
#angelapper/teaching/万门/JavaEE

```
package webapp;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.ServletOutputStream;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet(urlPatterns = "/urls")
public class UrlServlet extends HttpServlet {
	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException {
		StringBuffer requestURL = request.getRequestURL();
		if (request.getQueryString() != null) {
		    requestURL.append("?").append(request.getQueryString());
		}

		String name = request.getParameter("name");
		String apperance = request.getParameter("apperance");

		// Getting servlet request URL
        String url = request.getRequestURL().toString();

        // Getting servlet request query string.
        String queryString = request.getQueryString();

        // Getting request information without the hostname.
        String uri = request.getRequestURI();

        // Below we extract information about the request object path
        // information.
        String scheme = request.getScheme();
        String serverName = request.getServerName();
        int portNumber = request.getServerPort();
        String contextPath = request.getContextPath();
        String servletPath = request.getServletPath();
        String pathInfo = request.getPathInfo();
        String query = request.getQueryString();
		
		response.setContentType("text/html");
        PrintWriter pw = response.getWriter();
        pw.print("Url: " + url + "<br/>");
        pw.print("Uri: " + uri + "<br/>");
        pw.print("Scheme: " + scheme + "<br/>");
        pw.print("Server Name: " + serverName + "<br/>");
        pw.print("Port: " + portNumber + "<br/>");
        pw.print("Context Path: " + contextPath + "<br/>");
        pw.print("Servlet Path: " + servletPath + "<br/>");
        pw.print("Path Info: " + pathInfo + "<br/>");
        pw.print("Query: " + query + "<br/>");
        pw.print("Name: " + name + "<br/>");
        pw.print("Apperance: " + apperance);
	}

}
```

### Question Can we submit password by using Parameters?
easy to see and  plain text ?
