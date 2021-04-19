# Step 9 Many Problems
#angelapper/teaching/万门/JavaEE

### What if 新的认证方式，链接数据库。
```
package webapp;

import java.sql.*;

public class DBAuthService {
	public boolean validateUser(String user, String password) {
		boolean st =false;
	      try{
		 //loading drivers for mysql
	         Class.forName("com.mysql.jdbc.Driver");

	 	 //creating connection with the database 
	         Connection con=DriverManager.getConnection
	                        ("jdbc:mysql://localhost:3306/ecommerce","root","wanmen123");
	         PreparedStatement ps =con.prepareStatement
	                             ("select * from users where name=? and password=?");
	         ps.setString(1, user);
	         ps.setString(2, password);
	         ResultSet rs =ps.executeQuery();
	         st = rs.next();
	        
	      }catch(Exception e)
	      {
	          e.printStackTrace();
	      }
	         return st;
	}
}
```


### 可以通过定义接口
```
package webapp;

public interface AuthService {
	boolean validateUser(String userName, String Password);
}
```

### 想办法在构造函数中传递
```
	//how to pass in the constructor method 
	//private AuthService service;
	//public LoginServilet(AuthService service){
	//    this.service = service;
	//}

//TextEditor class directly depends on the SpellChecker class.
public class TextEditor {

    private SpellChecker checker;

    public TextEditor() {
        this.checker = new SpellChecker();
    }
}

//call the dependency then pass it to the TextEditor class public class TextEditor {

    private IocSpellChecker checker;

    public TextEditor(IocSpellChecker checker) {
        this.checker = checker;
    }

SpellChecker (new SpellChecker())

```

http://dotnetslackers.com/articles/designpatterns/InversionOfControlAndDependencyInjectionWithCastleWindsorContainerPart1.aspx


认证？ 
Session, Cookie, Request


request.getSession():
"or if the request does not have a session, creates one"

request.getSession(true):
"if there is no current session, returns a new session"

### servlet 生命周期
### 
### spring核心概念
### JavaBean 书写标准
    实现java.io.Serializable interface
    使用public的没有argument的构造函数
    所有properties都是私有的 使用getter和setter
    
    java 配置里面
    重构造
    直接
    
### xml配置


### log功能
log4j

### Design pattern 设计模式
### 单例模式
### 
### IOC 控制反转
### AOP设计原理
### Dependency Injection 依赖注入