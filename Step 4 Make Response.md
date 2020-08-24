# Step 4 Make Response
#angelapper/teaching/万门/JavaEE

### HtmlServlet.java
```
package webapp;
/**
 * 
 */

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.nio.file.Paths;
import java.nio.file.Files;
import java.nio.file.NoSuchFileException;

import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.ServletOutputStream;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
/**
 * www..com/{path}
 
 */
@WebServlet(urlPatterns = "/html/*")
public class HtmlServlet extends HttpServlet {
	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException {

        // Getting request information without the host name.
        String[] uri = request.getRequestURI().trim().split("/");
		
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = response.getWriter(); 
		
		String content = "sorry we did not found the page";
//		if(uri.length > 2){
		try {
			String contextPath = getServletContext().getRealPath(File.separator);
			content = new String(Files.readAllBytes(Paths.get(contextPath+"/resource/static/"+uri[2])));		
		} catch (NoSuchFileException e) { 
			content = "sorry we did not found the page";
	    }
	      catch (Exception e) {
		  content = "other exception " +  e.toString();
	    }
//		}
		out.print(content);
	}
}
```
www.. com/{path}/{path}
getRequestURI()
### FilesServlet.java
```
package webapp;

import javax.servlet.http.HttpServlet;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.OutputStream;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet(urlPatterns = "/files")
public class FilesServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
	
	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		performTask(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException,
			IOException {
		performTask(request, response);
	}

	private void performTask(HttpServletRequest request, HttpServletResponse response) throws ServletException,
			IOException {

		String pdfFileName = "javawanmen.pdf";
		String contextPath = getServletContext().getRealPath(File.separator);
		File pdfFile = new File(contextPath+"/resource/file/" + pdfFileName);

		response.setContentType("application/pdf");
		response.addHeader("Content-Disposition", "attachment; filename=" + pdfFileName);
		response.setContentLength((int) pdfFile.length());

		FileInputStream fileInputStream = new FileInputStream(pdfFile);
		OutputStream responseOutputStream = response.getOutputStream();
		int bytes;
		while ((bytes = fileInputStream.read()) != -1) {
			responseOutputStream.write(bytes);
		}

	}
}
```

