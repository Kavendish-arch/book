## HTML DOM 定义了访问和操作 HTML 文档的标准方法。

DOM 将 HTML 文档表达为树结构。

### 什么是 DOM？
DOM 是 W3C（万维网联盟）的标准。
DOM 定义了访问 HTML 和 XML 文档的标准：
“W3C 文档对象模型 （DOM） 是中立于平台和语言的接口，它允许程序和脚本动态地访问和更新文档的内容、结构和样式。”
W3C DOM 标准被分为 3 个不同的部分：

核心 DOM - 针对任何结构化文档的标准模型
XML DOM - 针对 XML 文档的标准模型
HTML DOM - 针对 HTML 文档的标准模型
DOM 是 Document Object Model（文档对象模型）的缩写。

什么是 XML DOM？
XML DOM 定义了所有 XML 元素的对象和属性，以及访问它们的方法。

什么是 HTML DOM？
HTML DOM 是：
HTML 的标准对象模型
HTML 的标准编程接口
W3C 标准
HTML DOM 定义了所有 HTML 元素的对象和属性，以及访问它们的方法。
换言之，HTML DOM 是关于如何获取、修改、添加或删除 HTML 元素的标准。
在 HTML DOM 中，所有事物都是节点。DOM 是被视为节点树的 HTML。

## DOM 节点 根据 W3C 的 HTML DOM 标准，HTML 文档中的所有内容都是节点：

* 整个文档是一个文档节点
* 每个 HTML 元素是元素节点
* HTML 元素内的文本是文本节点
* 每个 HTML 属性是属性节点
* 注释是注释节点

## HTML DOM 节点树 HTML DOM 将 HTML 文档视作树结构。这种结构被称为节点树：

通过 HTML DOM，树中的所有节点均可通过 JavaScript 进行访问。
所有 HTML 元素（节点）均可被修改，也可以创建或删除节点。

### 节点父、子和同胞 节点树中的节点彼此拥有层级关系。

父（parent）、子（child）和同胞（sibling）等术语用于描述这些关系。
父节点拥有子节点。同级的子节点被称为同胞（兄弟或姐妹）。

* 在节点树中，顶端节点被称为根（root）
* 每个节点都有父节点、除了根（它没有父节点）
* 一个节点可拥有任意数量的子
* 同胞是拥有相同父节点的节点

警告！
DOM 处理中的常见错误是希望元素节点包含文本。

### 编程接口
可通过 JavaScript （以及其他编程语言）对 HTML DOM 进行访问。
所有 HTML 元素被定义为对象，而编程接口则是对象方法和对象属性。
HTML DOM 对象 - 方法和属性
* 方法 是您能够执行的动作（比如添加或修改元素）
    1. getElementById(id) - 获取带有指定 id 的节点（元素）
    2. appendChild(node) - 插入新的子节点（元素）
    3. removeChild(node) - 删除子节点（元素）
* 属性 是您能够获取或设置的值（比如节点的名称或内容）
    1. innerHTML - 节点（元素）的文本值
    2. parentNode - 节点（元素）的父节点
    3. childNodes - 节点（元素）的子节点
    4. attributes - 节点（元素）的属性节点
    5. 
### 一些 DOM 对象方法
这里提供一些您将在本教程中学到的常用方法：

方法	                描述
getElementById()	返回带有指定 ID 的元素。
getElementsByTagName()	返回包含带有指定标签名称的所有元素的节点列表（集合/节点数组）。
getElementsByClassName()	返回包含带有指定类名的所有元素的节点列表。
appendChild()	把新的子节点添加到指定节点。
removeChild()	删除子节点。
replaceChild()	替换子节点。
insertBefore()	在指定的子节点前面插入新的子节点。
createAttribute()	创建属性节点。
createElement()	创建元素节点。
createTextNode()	创建文本节点。
getAttribute()	返回指定的属性值。
setAttribute()	把指定属性设置或修改为指定的值。

### 属性是节点（HTML 元素）的值，您能够获取或设置。
* innerHTML 属性
    获取元素内容的最简单方法是使用 innerHTML 属性。
    innerHTML 属性对于获取或替换 HTML 元素的内容很有用。
* nodeName 属性
    nodeName 属性规定节点的名称。
    nodeName 是只读的
    元素节点的 nodeName 与标签名相同
    属性节点的 nodeName 与属性名相同
    文本节点的 nodeName 始终是 #text
    文档节点的 nodeName 始终是 #document
    注释：nodeName 始终包含 HTML 元素的大写字母标签名。

* nodeValue 属性
    nodeValue 属性规定节点的值。
    元素节点的 nodeValue 是 undefined 或 null
    文本节点的 nodeValue 是文本本身
    属性节点的 nodeValue 是属性值
    获取元素的值

* nodeType 属性
    nodeType 属性返回节点的类型 nodeType 是只读的。
    比较重要的节点类型有：
    元素类型	NodeType
        元素	1
        属性	2
        文本	3
        注释	8
        文档	9

### 访问 HTML DOM - 查找 HTML 元素。
   * 访问 HTML 元素（节点）
   * 访问 HTML 元素等同于访问节点
    1. 通过使用 getElementById() 方法
    2. 通过使用 getElementsByTagName() 方法
    3. 通过使用 getElementsByClassName() 方法
    注释：getElementsByClassName() 在 Internet Explorer 5,6,7,8 中无效。

### 修改 HTML = 改变元素、属性、样式和事件。
修改 HTML 元素
修改 HTML DOM 意味着许多不同的方面：
1. 改变 HTML 内容 改变元素内容的最简答的方法是使用 innerHTML 属性。
2. 改变 CSS 样式 通过 HTML DOM，您能够访问 HTML 元素的样式对象。
3. 改变 HTML 属性  先必须创建该元素（元素节点），然后追加到已有的元素上。
4. 创建新的 HTML 元素
5. 删除已有的 HTML 元素
6. 改变事件(处理程序)

### 创建 HTML 元素

<script>
var para=document.createElement("p");
var node=document.createTextNode("This is new.");
para.appendChild(node);
var element=document.getElementById("d1");
</script>

### 改变 HTML 内容
改变元素内容的最简单的方法是使用 innerHTML 属性。

<script>
document.getElementById("p1").innerHTML="New text!";
</script>

### 改变 HTML 样式
通过 HTML DOM，您能够访问 HTML 对象的样式对象。

<script>
document.getElementById("p2").style.color="blue";
</script>

### 使用事件
HTML DOM 允许您在事件发生时执行代码。
当 HTML 元素”有事情发生“时，浏览器就会生成事件：
在元素上点击
加载页面
改变输入字段

下面两个例子在按钮被点击时改变 <body> 元素的背景色：

<script>
function ChangeBackground()
{
document.body.style.backgroundColor="lavender";
}
function ChangeText()
{
document.getElementById("p1").innerHTML="New text!";
}
</script>

### 添加、删除和替换 HTML 元素。
1. 如需向 HTML DOM 添加新元素，您首先必须创建该元素，然后把它追加到已有的元素上。
    * ppendChild() 方法，将新元素作为父元素的最后一个子元素进行添加。
    * insertBefore() 方法：
    1. 这段代码创建了一个新的 <p> 元素：
        var para=document.createElement("p");
    2. 如需向 <p> 元素添加文本，您首先必须创建文本节点。这段代码创建文本节点：
        var node=document.createTextNode("This is a new paragraph.");
    3. 然后您必须向 <p> 元素追加文本节点：
        para.appendChild(node); 
    4. 最后，您必须向已有元素追加这个新元素。查找到一个已有的元素， 追加新元素：
        var element=document.getElementById("div1");
        element.appendChild(para);

2. 删除已有的 HTML 元素
    如需删除 HTML 元素，您必须清楚该元素的父元素：
    1. 查找 id="div1" 的元素：
    var parent=document.getElementById("div1");
    2. 查找 id="p1" 的 <p> 元素：
    var child=document.getElementById("p1");
    3. 从父元素中删除子元素：
    parent.removeChild(child);
    提示：能否在不引用父元素的情况下删除某个元素？
    很抱歉。DOM 需要了解您需要删除的元素，以及它的父元素。
    这里提供一个常用的解决方法：找到您需要删除的子元素，然后使用 parentNode 属性来查找其父元素：
        var child=document.getElementById("p1");
        child.parentNode.removeChild(child);

3. 替换 HTML 元素
    如需替换 HTML DOM 中的元素，请使用 replaceChild() 方法：
<script>
var para=document.createElement("p");
var node=document.createTextNode("This is new.");
para.appendChild(node);
var parent=document.getElementById("div1");
var child=document.getElementById("p1");
parent.replaceChild(para,child);
</script>

### 事件 HTML DOM 允许 JavaScript 对 HTML 事件作出反应
1. 对事件作出反应
当事件发生时，可以执行 JavaScript，比如当用户点击一个 HTML 元素时。
如需在用户点击某个元素时执行代码，请把 JavaScript 代码添加到 HTML 事件属性中：
onclick=JavaScript
* HTML 事件的例子：
    1. 当用户点击鼠标时
    2. 当网页已加载时
    3. 当图片已加载时
    4. 当鼠标移动到元素上时
    5. 当输入字段被改变时
    6. 当 HTML 表单被提交时
    7. 当用户触发按键时
2. HTML 事件属性
如需向 HTML 元素分配事件，您可以使用事件属性。
向 button 元素分配一个 onclick 事件：
<button onclick="displayDate()">试一试</button>
在上面的例子中，当点击按钮时，会执行名为 displayDate 的函数。

3. 使用 HTML DOM 来分配事件
HTML DOM 允许您使用 JavaScript 向 HTML 元素分配事件：
<script>
    document.getElementById("myBtn").onclick = function(){displayDate()};
</script>

4. onload 和 onunload 事件 当用户进入或离开页面时，会触发 onload 和 onunload 事件。
onload 事件可用于检查访客的浏览器类型和版本，以便基于这些信息来加载不同版本的网页。
onload 和 onunload 事件可用于处理 cookies。
<body onload="checkCookies()">
5. onchange 事件 onchange 事件常用于输入字段的验证。
下面的例子展示了如何使用 onchange。当用户改变输入字段的内容时，将调用 upperCase() 函数。
<input type="text" id="fname" onchange="upperCase()">

6. onmouseover 和 onmouseout 事件 
onmouseover 和 onmouseout 事件可用于在鼠标指针移动到或离开元素时触发函数。

7. onmousedown、onmouseup 以及 onclick 事件
onmousedown、onmouseup 以及 onclick 事件是鼠标点击的全部过程。
当某个鼠标按钮被点击时，触发 onmousedown 事件，
当鼠标按钮被松开时，会触发 onmouseup 事件，
当鼠标点击完成时，触发 onclick 事件


### 通过 HTML DOM，您能够使用节点关系在节点树中导航。
* HTML DOM 节点列表 getElementsByTagName() 方法返回节点列表。节点列表是一个节点数组。
下面的代码选取文档中的所有 <p> 节点：
可以通过下标号访问这些节点
HTML DOM 节点列表长度
length 属性定义节点列表中节点的数量。
使用 length 属性来循环节点列表：
x=document.getElementsByTagName("p");
for (i=0;i<x.length;i++)
{
    document.write(x[i].innerHTML);
    document.write("<br />");
}
* 三个节点属性：parentNode、firstChild 以及 lastChild ，在文档结构中进行导航。
* DOM 根节点 这里有两个特殊的属性，可以访问全部文档：
document.documentElement - 全部文档
document.body - 文档的主体

* childNodes 和 nodeValue
除了 innerHTML 属性，您也可以使用 childNodes 和 nodeValue 属性来获取元素的内容。

