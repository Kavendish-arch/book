### 跨域调用
#### 跨域问题的原理
* 浏览器
* 跨域：
> 同源策略即：同一协议，同一域名，同一端口号。当其中一个不满足时，我们的请求即会发生跨域问题。
* XmlHttpRequest
#### 解决方法
1. 指定参数改动 浏览器
2. XHR改变成 JSONP

3. 跨域
    1. 被调用方允许跨域：支持跨域
    2. 调用方通过代理，域名转换 ：隐藏跨域


1. jsonp
2. document.domain + iframe
3. location.hasj + iframe
4. window.name + iframe
5. postMessage跨域
6. 跨域资源共享(Cors)
7. nginx代理跨域
8. node.js中间件代理跨域
9. webSocket协议跨域

