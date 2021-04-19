# Step 8 Try to make it Better
#angelapper/teaching/万门/JavaEE
### Product
```
package webapp;

public class Product {
    int id;
    String title, detail, thumbnail;
    double price;
    
    public Product(int id, String title, String detail, String thumbnail, double price){
    	this.id = id;
    	this.title = title;
    	this.detail = detail;
    	this.thumbnail = thumbnail;
    	this.price = price;
    }
    public int getId() {
        return id;
    }
    
    public void setId(int id) {
        this.id = id;
    }
}
```

### Product Service
```
package webapp;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.*;

public class ProductService {
	public  List<Product> getAllProduct() {
	  List<Product> allProduct = new ArrayList<Product>();
	  
      try{
 		 //loading drivers for mysql
         Class.forName("com.mysql.jdbc.Driver");

    	 //creating connection with the database 
         String connectionString = "jdbc:mysql://localhost:3306/ecommerce?user=root&password=wanmen123";
         Connection con=DriverManager.getConnection(connectionString);
         try{
	         PreparedStatement ps =con.prepareStatement("select * from product");
	         try{
		         ResultSet rs =ps.executeQuery();
		         try{
		             while (rs.next()) {
		            	 int id = Integer.parseInt(rs.getString("id"));
		            	 String title = rs.getString("title");
		            	 String thumbnail = rs.getString("thumbnail");
		            	 String detail = rs.getString("detail");
		            	 double price = Double.parseDouble(rs.getString("detail"));
		            	 allProduct.add(new Product(id, title, detail, thumbnail,price));
		               }		        	 
		         }finally{
		        	 rs.close(); // release resultSet
		         }
	         }finally{
	          ps.close(); // release the statement
	         }
         }finally{
        	 con.close(); // release the connection
         }
	   }catch(Exception e){
	          e.printStackTrace();
       }
       return allProduct;
	}
}
```

### Product Servlet
```
package webapp;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet(urlPatterns = "/products")
public class ProductServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
	private ProductService productService = new ProductService();

	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws IOException, ServletException {
		response.setContentType("text/html;charset=utf-8");
		request.setAttribute("products", productService.getAllProduct());
		request.getRequestDispatcher("/WEB-INF/views/products.jsp").forward(request, response);
	}
}

```


### Missing Jar
```
HTTP Status 500 - The absolute uri: http://java.sun.com/jsp/jstl/core cannot be resolved in either web.xml or the jar files deployed with this application

```

### Product JSP
```
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<html>
<head>
<title>Data Apllication Lab!!</title>
</head>
<body>
<H1>Welcome ${name}</H2>
<div>
Here is Products
<ol>
<c:forEach items="${products}" var="product">
   <li>${product.title}:${product.price}</li>
</c:forEach>
</ol>
</div>
</body>
</html>
```

### Make Login forward to Product
```
request.getRequestDispatcher("/WEB-INF/views/products.jsp").forward(request, response);
```

### ERROR
HTTP method POST is not supported by this URL

how to solve it?
and  the url is still http://localhost:8080/login.do
add post duplicate code?

```
@WebServlet(urlPatterns = "/products")
public class ProductServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
	private ProductService productService = new ProductService();

	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws IOException, ServletException {
		response.setContentType("text/html;charset=utf-8");
		request.setAttribute("products", productService.getAllProduct());
		request.getRequestDispatcher("/WEB-INF/views/products.jsp").forward(request, response);
	}
	
	@Override
	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws IOException, ServletException {
		response.setContentType("text/html;charset=utf-8");
		request.setAttribute("products", productService.getAllProduct());
		request.getRequestDispatcher("/WEB-INF/views/products.jsp").forward(request, response);
	}
}
```

or we redirect to 

but there is something wrong, we are missing products list…. interesting~
request.getRequestDispatcher vs response.sendRedirect

#### forward
Control can be forward to resources available within the server from where the call is made.

#### redirect
Control can be redirect to resources to different servers or domains.


### But after that we are missing NAME!!