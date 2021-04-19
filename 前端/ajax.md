## AJAX

1. 概念 Ajax 即“Asynchronous Javascript And XML”（异步 JavaScript 和 XML），
    创建交互式、快速动态网页应用的网页开发技术，无需重新加载整个网页的情况下，能够更新部分网页的技术。
    通过在后台与服务器进行少量数据交换，Ajax 可以使网页实现异步更新。
    这意味着可以在不重新加载整个网页的情况下，对网页的某部分进行更新。
1. 同步   客户端等待服务器响应
2. 异步   客户端不用等待，服务的响应
1. 不刷新网页，从服务器拉取数据
2. js动态修改dom
3. xmlHttpRequest 

##实现方式
###1. 原生的Js实现方式
1. 创建XMLHttpRequest对象
2. 向服务器请求
3. 响应函数
4. 响应事件
5. Parse Json 数据格式 更新DOM

### XMLHttpRequest 对象 所有现代浏览器均支持 XMLHttpRequest 对象（IE5 和 IE6 使用 ActiveXObject）。
XMLHttpRequest 用于在后台与服务器交换数据。这意味着可以在不重新加载整个网页的情况下，对网页的某部分进行更新。

1. 创建 XMLHttpRequest 对象 
浏览器（IE7+、Firefox、Chrome、Safari 以及 Opera）均内建 XMLHttpRequest 对象 variable=new XMLHttpRequest();
老版本的（IE5 和 IE6）使用 ActiveX 对象：variable=new ActiveXObject("Microsoft.XMLHTTP");
```
    var xmlhttp;
    if (window.XMLHttpRequest) 
    // code for IE7+, Firefox, Chrome, Opera, Safari
    {
        xmlhttp=new XMLHttpRequest();
    }
    else // code for IE6, IE5
    {
      xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
```
### XMLHttpRequest 对象用于和服务器交换数据。
向服务器发送请求
使用 XMLHttpRequest 对象的 open() 和 send() 方法：

xmlhttp.open("GET","test1.txt",true);
xmlhttp.send();

1. open(method,url,async)	规定请求的类型、URL 以及是否异步处理请求。
 open() method: GET/POST
### GET 还是 POST？
与 POST 相比，GET 更简单也更快，并且在大部分情况下都能用。
然而，在以下情况中，请使用 POST 请求：
   * 无法使用缓存文件（更新服务器上的文件或数据库）
   * 向服务器发送大量数据（POST 没有数据量限制）
   * 发送包含未知字符的用户输入时，POST 比 GET 更稳定也更可靠
* GET: 将参数放在URL后面，使用&和?的方式拼写，
          http://www.taobao.com?key1=value1&key2=value&key3=value3
          局限：最长2048；
          特殊字符需要编码 urlencode
          有可能会缓存，为了避免这种情况，请向 URL 添加一个唯一的 ID：
          xmlhttp.open("GET","demo_get.asp?t=" + Math.random(),true);
          xmlhttp.send();
* POST: 先发HTTP头，再发送参数，参数被放在后续的数据包中，没有长度限制，不会缓存
* 
a: true,异步：调用返回，数据包来的时候会触发事件。false,同步。
method：请求的类型；GET 或 POST
url：文件在服务器上的位置
async：true（异步）或 false（同步）

2. send(string)	将请求发送到服务器。
string：仅用于 POST 请求




如果您希望通过 GET 方法发送信息，请向 URL 添加信息：

xmlhttp.open("GET","demo_get2.asp?fname=Bill&lname=Gates",true);
xmlhttp.send();

POST 请求
一个简单 POST 请求：

xmlhttp.open("POST","demo_post.asp",true);
xmlhttp.send();

如果需要像 HTML 表单那样 POST 数据，请使用 setRequestHeader() 来添加 HTTP 头。然后在 send() 方法中规定您希望发送的数据：

xmlhttp.open("POST","ajax_test.asp",true);
xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
xmlhttp.send("fname=Bill&lname=Gates");

3. setRequestHeader(header,value)	向请求添加 HTTP 头
header: 规定头的名称
value: 规定头的值
url - 服务器上的文件
open() 方法的 url 参数是服务器上文件的地址：

xmlhttp.open("GET","ajax_test.asp",true);
该文件可以是任何类型的文件，比如 .txt 和 .xml，或者服务器脚本文件，比如 .asp 和 .php （在传回响应之前，能够在服务器上执行任务）。

### 异步 - True 或 False
AJAX 指的是异步 JavaScript 和 XML（Asynchronous JavaScript and XML）。
XMLHttpRequest 对象如果要用于 AJAX 的话，其 open() 方法的 async 参数必须设置为 true：
xmlhttp.open("GET","ajax_test.asp",true);
对于 web 开发人员来说，发送异步请求是一个巨大的进步。很多在服务器执行的任务都相当费时。AJAX 出现之前，这可能会引起应用程序挂起或停止。

通过 AJAX，JavaScript 无需等待服务器的响应，而是：

在等待服务器响应时执行其他脚本
当响应就绪后对响应进行处理
### 异步 Async = true
当使用 async=true 时，请规定在响应处于 onreadystatechange 事件中的就绪状态时执行的函数：

xmlhttp.onreadystatechange=function()
  {
  if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
    document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
    }
  }
xmlhttp.open("GET","test1.txt",true);
xmlhttp.send();

### 同步Async = false
xmlhttp.open("GET","test1.txt",false);
不需要onreadystatechange
我们不推荐使用 async=false，但是对于一些小型的请求，也是可以的。

请记住，JavaScript 会等到服务器响应就绪才继续执行。如果服务器繁忙或缓慢，应用程序会挂起或停止。
```
    xmlhttp.open("GET","test1.txt",false);
    xmlhttp.send();
    document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
```

### 获得来自服务器的响应，
### 使用 XMLHttpRequest 对象的 responseText 或 responseXML 属性
### 
1. responseText	获得字符串形式的响应数据。
2. responseXML	获得 XML 形式的响应数据。

### onreadystatechange 事件
当请求被发送到服务器时，我们需要执行一些基于响应的任务。
每当 readyState XMLHttpRequest 的状态信息 改变时，就会触发 onreadystatechange 事件。

XMLHttpRequest 对象的三个重要的属性：
1. onreadystatechange	回调函数 每当 readyState 属性改变时，就会调用该函数。
2. readyState 存有 XMLHttpRequest 的状态：从 0 到 4 发生变化
    0: 请求未初始化
    1: 服务器连接已建立
    2: 请求已接收
    3: 请求处理中
    4: 请求已完成，且响应已就绪
3. status Http状态码:	200: "OK"、404: 未找到页面
```
在 onreadystatechange 事件中，我们规定当服务器响应已做好被处理的准备时所执行的任务。
xmlhttp.onreadystatechange=function()
{
  //当 readyState 等于 4 且状态为 200 时，表示响应已就绪：
  if (xmlhttp.readyState==4 && xmlhttp.status==200)
  {
    document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
   }
}
```
注释：onreadystatechange 事件被触发 5 次（0 - 4），对应着 readyState 的每个变化。

### 使用 Callback 函数 一种以参数形式传递给另一个函数的函数。
如果您的网站上存在多个 AJAX 任务，那么您应该为创建 XMLHttpRequest 对象编写一个标准的函数，并为每个 AJAX 任务调用该函数。
该函数调用应该包含 URL 以及发生 onreadystatechange 事件时执行的任务（每次调用可能不尽相同）：
```
function myFunction()
{
    loadXMLDoc("ajax_info.txt",function()
    {
        if (xmlhttp.readyState==4 && xmlhttp.status==200)
        {
            document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
        }
     });
}
```
##2. JQeury实现方式
1. $.ajax()
* $.ajax({键值对});
2. $.get()
    $.get({
        "test/ajaxTest", {username:"jack"}, function 
    })
3. $.post()
。 

### JQuery封装AJAX

### 文件上传


　@Resource的作用相当于@Autowired，只不过@Autowired按byType自动注入，而@Resource默认按 byName自动注入罢了。@Resource有两个属性是比较重要的，分是name和type，Spring将@Resource注解的name属性解析为bean的名字，而type属性则解析为bean的类型。所以如果使用name属性，则使用byName的自动注入策略，而使用type属性时则使用byType自动注入策略。如果既不指定name也不指定type属性，这时将通过反射机制使用byName自动注入策略。
　　@Resource装配顺序
　　1. 如果同时指定了name和type，则从Spring上下文中找到唯一匹配的bean进行装配，找不到则抛出异常
　　2. 如果指定了name，则从上下文中查找名称（id）匹配的bean进行装配，找不到则抛出异常
　　3. 如果指定了type，则从上下文中找到类型匹配的唯一bean进行装配，找不到或者找到多个，都会抛出异常
　　4. 如果既没有指定name，又没有指定type，则自动按照byName方式进行装配；如果没有匹配，则回退为一个原始类型进行匹配，如果匹配则自动装配；

@Autowired 与@Resource的区别：

 

1、 @Autowired与@Resource都可以用来装配bean. 都可以写在字段上,或写在setter方法上。

2、 @Autowired默认按类型装配（这个注解是属业spring的），默认情况下必须要求依赖对象必须存在，如果要允许null值，可以设置它的required属性为false，如：@Autowired(required=false) ，如果我们想使用名称装配可以结合@Qualifier注解进行使用，如下：

1
2
@Autowired()@Qualifier("baseDao")
privateBaseDao baseDao;
3、@Resource（这个注解属于J2EE的），默认按照名称进行装配，名称可以通过name属性进行指定，如果没有指定name属性，当注解写在字段上时，默认取字段名进行安装名称查找，如果注解写在setter方法上默认取属性名进行装配。当找不到与名称匹配的bean时才按照类型进行装配。但是需要注意的是，如果name属性一旦指定，就只会按照名称进行装配。

1
2
@Resource(name="baseDao")
privateBaseDao baseDao;



简介
在日常开发中，经常关注核心的业务或者核心的架构手法，往往忽略了一些小的点点滴滴
今天就记录下在SpringBoot开发中 @RequestMapping 注解中的常见参数简单说明。

说到这两个参数，不得不先回顾一下HTTP协议Header中的两个东西 ContentType 和Accept。

ContentType： 告诉服务器当前发送的数据是什么格式
Accept ： 用来告诉服务器，客户端能认识哪些格式,最好返回这些格式

consumes 用来限制ContentType
produces 用来限制Accept


value， method；
value：   指定请求的实际地址，指定的地址可以是URI Template 模式（后面将会说明）；
method：  指定请求的method类型， PUT、GET、DELETE、POST 分别对应注解@PutMapping @GetMapping @DeleteMapping @PostMapping；

consumes，produces；
consumes： 指定处理请求的提交内容类型（Content-Type），例如application/json, text/html;
produces:  指定返回的内容类型，仅当request请求头中的(Accept)类型中包含该指定类型才返回；

params，headers；
params： 指定request中必须包含某些参数值是，才让该方法处理。
headers： 指定request中必须包含某些指定的header值，才能让该方法处理请求。

/**
* consumes 标识处理request Content-Type为“application/json”类型的请求.
* produces标识处理request请求中Accept头中包含了"application/json"的请求.
* 同时暗示了返回的内容类型为application/json;
*/
  @ApiOperation(value = "保存用户")
  @PostMapping(value = "/execute",produces = MediaType.APPLICATION_JSON_VALUE,consumes = MediaType.APPLICATION_JSON_VALUE)
  public String saveUser(@RequestBody User userl){
        //TO DO
        return "保存成功";
  }


作者：高先森你别走
链接：https://www.jianshu.com/p/f78b43f048e6
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。