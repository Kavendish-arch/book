# MVC
 M:模型
 V:视图
 C:控制
 
## 三大框架: 
    其他：
        Bootstrap
        JQuery
        node.js

IE:Trident
Chrome: Webkit
FireFox:Gecko
Opera:Presto

编译原理
    解释型语言：跨平台，重新编译 JavaScript，python
    编译型语言：运行速度快
2001 IE6 内核剥离js引擎
2008 V8 js引擎 js不只是在浏览器运行
Jit技术：

JavaScript只支持单线程

## 基础
### 变量:
    var num = 1;
    var str = "hello ";
    document.write("hello2 world");
    数据类型只有 number and string
    和python类似，只有文本和数字
    细分: 整型、浮点型、字符、字符串、布尔
    重复声明 JavaScript 变量
    如果再次声明某个 JavaScript 变量，将不会丢它的值。
    实例
    var carName = "porsche";
    var carName; 
    在这两条语句执行后，变量 carName 的值仍然是 "porsche"

### 运算: 
    + - * / % 
    字符和数字之间 + 

+   两个作用：数字相加和字符拼接{
        // + 数字加法
        类比：(在python中 数字需要转换字符串 str())
    
        var iNum = 3 + 3;
        document.write('[+] iNum = ' + iNum + '<br>');

        // + 字符串的拼接，字符和数字变成字符串
        var str = '5' + 2;
        var sToken = 'abc' + 'edf';
        document.write('[+] sToken = ' + sToken + '<br>');

        //////////////////////////////////////////////////////////
        var sToken = '5' - 5;  = 0
        document.write('[-] sToken = ' + sToken + '<br>');
}
    // - 数字减法
    // * 数字乘法
    // / 数字除法
    // % 取模
    s++ s-- 不应该写在表达式里，可读性变差
    // ++
    // --
    // += -= *= /= %=

    比较运算符：
        == === < > <= >= !=
        数字比较：

        字符比较：
        document.write('[>] \'25\' < 4 ? ' + ('25' < 4) + '<br>');
        document.write('[>] \'aaa\' > 4 ? ' + ('aaa' > 4) + '<br>');
    三元运算符
        25 > 5 ? 'l' : 's'
        document.write('[?:] 25>4?' + (25>4 ? 'l' : 's') + '<br>');
条件循环{
    if else
    if else if else 
    switch
    for
    while
}
类型转换
 toInt
 toString
 toBool

### 数组:{
    JavaScript数组是弱类型
    var arr = [];          =  arr6 = new Array();
    var arr2 = [1,2,3,4];  =  arr7 = new Array(1, 2, 3, 4);
    var arr3 = [,,,];
    var arr4 = [0,'accc',undefined,null,true,{}];
    声明
    
    arr = new Array();
    访问数组元素
    console.log(arr1[1]);
    console.log(arr1[1]);
    console.log(arr4[3]);

    如果一个下标位置原来不存在，会添加， 如果必须，还会增加length
    arr[3] = 5;
    console.log(arr2);
    arr2[2] = 2;
    console.log(arr2);

    如果下标存在，覆盖
    arr2[0] = 'ab';
    console.log(arr2);

    数组有长度 length
    console.log(arr.length);
    var arr = [];
    var arr1 = [1, 2, 3, 4];

    var arr2 = [true, null, 'a', 234]
    console.log(arr1[1]);

    arr6 = new Array();
    arr7 = new Array(1, 2, 3, 4);

    //稀疏数组、矩阵
    var larr = new Array(1000);

    larr[3] = 5;
    larr[1.5] = 7;
    //数组可以当作map使用
    //key-value 
    var a4 = [];

    a4['China'] = "满汉全席";
    a4['American'] = "火鸡";
    console.log(a4);

    //那如何判定数组
    var ar = [];
    console.log(ar.constructor.name == 'Array');

    var arr = [1, 2, , , 3, 4];
    arr["China"] = "大餐";
    //轮询数组 
    //1.for() 使用数组的方式 如果中间有空值 返回 undefined
    for(var i = 0; i < arr.length; i++){
        console.log(arr[i]);
    }
    //2.for(in) 使用map的方式返回所有非稀疏的节点的key。
    for(var i in arr){
        console.log(arr[i]);
    }
    //3.forEach() 返回所有数字的且非稀疏的节点的value。

    arr.forEach(function(x){
        console.log(x);
    });

    //concat连接
    var arr8 = arr1.concat(arr);
    console.log(arr8);

    //join() 

    //sort() 1.数字的sort()
    console.log(arr8.sort());
    //2.字符串的sort() 对比字符的ASCII码
    arr2 = ["bda", 'bbb', 'acc'];
    console.log(arr2.sort());
    // 三个需要记忆的ASCII码：0 30h，A 41h，a 61h

}

堆栈、栈{
    先进后出
//栈 stack push() pop()
function Wang(){

}
//push pop 尾进尾出

```
var arr = ['a', 'b', 'c'];
//console.log(arr.join(','));
arr.push('s');
console.log(arr);
//console.log(arr.join('-'));
console.log(arr.pop());
//console.log(arr.join('-'));
//unshift-shift 头进头出
console.log("--------");
arr = ['a','b','c'];
console.log(arr.join(','));
arr.unshift('z');
console.log("join " + arr.join('-'));
console.log(arr.shift());
console.log(arr.join(','));
```
// 队列：先进先出：queue
// 尾进头出
```
arr = ['a','b','c'];
console.log(arr.join("--"));
arr.push('z');
console.log(arr.join(','));
console.log(arr.shift());
console.log(arr.join(','));
```

//// 头进尾出
```
arr =['a','b','c'];
console.log(arr.join("--"));
arr.unshift('z');
console.log(arr.join(','));
console.log(arr.pop());
console.log(arr.join(','));
```


### (底层c++)
java C++ 同

值类型和引用类型
number 数值number string boolean
等

引用类型
对象 object function array(容器)

栈和堆
数值存储在栈之中
对象存储在堆之中

引用类型，对象由于内存未确定存储在堆，把对象引用存储在栈中
var x = 10; key x, value key
var x = []  key x, value [](引用)
var arr = []; 存储在栈
数组[] 存储在堆里 但事地址存储在arr里
key(栈) - value(堆) 
垃圾收集 GC 堆内存计数器
MS COM 
作用域
超出作用域，栈内存内数据将会销毁
函数的栈
//栈内存
001 a,5
002 arr,001
003 arr2,001
004 b， a4
变量销毁、指向其他对象，引用的对象计数器减一
当引用的计数为零(没有变量引用这个对象，该对象称为孤儿)
垃圾回收只处理堆内存中的数据
1.堆内存达到上限
2.定期回收时间到
内存泄露：循环引用
{
    var arr = []
    var arr2 = []
    arr[0] = arr2
    arr2[0] = arr
    循环引用,没有栈内存引用堆内存
    循环检测
}
//堆内存
001 [0],(2)
002 [1]
003 [2]
004 [3]


// 函数可以有形参，也可以没有
// 函数可以有返回值，也可以没有，
没有的时候函数返回undefined
 函数的立即调用
 嵌套函数
 函数调用(形参和实参)
x = [1,2,3,4,5,NaN,undefined,null,'abc'];
function sum(arr){
	var iRet = 0;
	for(var i in arr){
		if(typeof(i) == 'number'){
			if(!isNaN(i) && isFinite(i)){
				iRet += i;
			}
		}
	}
	return iRet;
}
console.log("-----");
console.log(sum(x));
console.log("-----");
x = [1,2,3,4,5,NaN,undefined,null,'abc'];
// 所给参数不符合要求的处理方法：
//   第一，发现不合格，拒绝服务，保证自己的代码不崩溃。
//   第二，发现不合格，把合格部分处理，返回。
//函数声明
// 函数的声明
function <函数名>([<形式上的参数>]){
    函数体
}
function sum(array){
    var ret = 0;
    for(var i in array){
        ret += i;
    }
    return ret;
};
function sum(arr){
	var iRet = 0;
	
	for(var i = 0; i < arr.length; i++){
		if(typeof(arr[i]) == 'number'){
			if(!isNaN(arr[i]) && isFinite(arr[i])){
				iRet += arr[i]
			}
		}
	}
	//console.log(iRet);
	return iRet;
}
console.log("-----");
console.log(sum(x));
console.log("-----");
// 12345,54321，用函数实现。

function reverseNumber(num){
	if(typeof num != 'number'){
		return '';
	}
	
	if(!isFinite(num) || isNaN(num)){
		return '';
	}
	return +num.toString().split('').reverse().join('');
}
console.log(typeof(12.4));
console.log(typeof("23"));
console.log(reverseNumber(12345));
console.log("----- 函数表达式------");

//函数表达式 和函数声明有极大的不同
//(函数名系统无记录)
/**1. */
// (function f(){})
/**2. */
// var f = function ff(){};
/**3. */
// ff(a, function fff(){},b);
// var f = function fact(x){
// 	if(x <= 1){
// 		return 1;
// 	}else{
// 		return x * fact(x-1);
// 	}
// };
var f = function(x){
	if(x <= 1){
		return 1;
	}else{
		return x * arguments.callee(x-1);
		//函数表达式作用域只有在函数中
		//使用arguments.callee代替自己
	}
};
console.log(" 阶乘 " + f(8));
/**
 * f(5)
 * 5 * f(4)
 *	   f(4)
 * 	   4 * f(3)
 * 		   f(3)
 * 		   3 * f(2)
 * 			   f(2)
 * 			   2 * f(1)
 *  		       2 * 1
 */
//函数作为参数传递给其他函数
function f1(f){

	console.log(f);
	console.log("调用")
	console.log(f());
}
function f2(){
	console.log("im f2 function");
	return "f2 see you"
}
f1(f2);
var f3 = function(){
	console.log("i am f3");
	return "f3 is here";
};
f1(f3);
//立即执行函数 一次性函数
// var a = (function(){
// 	console.log("im 立即函数");
// 	return "f3";
// })();
console.log((function(){
	console.log("im 立即函数");
	return "f3";
})("wangli")) ;

/**
 * 值类型函数调用：赋值
 * 引用类型：传递地址
 */
var x = [1];
var y = [3];
function change(x,y){
	var temp = x[0];
	x[0] = y[0];
	y[0] = temp;
}
console.log(x,y)
console.log(change(x,y))
console.log(x,y)
/**
 * 函数嵌套
 */
// function hypotenuse(a,b){
// 	function square(x){
// 		return x * x;
// 	}
// 	return Math.sqrt(square(x) + square(y));
// }
// console.log(" 嵌套 " + hypotenuse(3,3));

//函数调用方式
/**
 * 1.函数方式
 * 2.作为方法
 */
// var obj = {
// 	add:function(a,b){
// 		return a + b;
// 	}
// };
var obj = {};
obj.add = function(a,b){
	return a + b;
};
console.log(obj.add(1,2));
console.log(obj['add'](1,2));
/**3.构造函数 */
var arr = new Array();
//构造函数
/**4.间接调用 
 * 简介调用和直接调用绑定指针this
*/
function hypotenuse(a,b){
	function square(x){
		return x * x;
	}
	return Math.sqrt(square(a) + square(b));
}

console.log(this.hypotenuse(2, 2));
console.log(hypotenuse(this, 3, 4));
console.log(hypotenuse(this,[2,3]));

//形参和实参
/**
 * 在C/C++ java 中参数少或多会报错
 * 函数重载(参数类型改变)
 * JavaScript 无函数重载，第二个重名函数会覆盖
 * JavaScript function(a,b,c) 形参和实参
 * 数量、类型都可以不同
 * 形参和实参会绑定、动态关联
 */
function foo(a,b,c){ //a b c 形参
	console.log(foo.length);
	console.log(arguments);//arguments 实参的数组

	arguments[1] = -1;
	console.log("a=" + a);
	console.log("b=" + b);
	b = 0;
	console.log("b=" + b);
	console.log(arguments[1]);
}
foo(1);
foo(1,2,3,4,5,6);
//函数递归
/**
 * f(1)成立
 * f(n) 和 f(n-1) 成立
 */
function fe(x){
	if(x < 0)
		return 0;
	console.log('begin' + x);
	foo(--x);
	console("end" + x);
}
/**
 * 1) f(3)
 * 2) f(3)
 * 	  f(2)
 * 3) f(3)
 * 	  f(2)
 * 	  f(1) = 1
 * 
 * 返回

 * 3) f(3)
 * 	  f(2)
 * 2) f(3) 	  
 * 
 * 
 */
function step(x){
	switch(x){
		case 1:
			return 1;
			break;
		case 2:
			return 2;
	}
}
//对象
// 对象
// 对象的创建

var obj1 = {};
var obj2 = new Object();
// 两个方法都可以。

var objBook = {
	name: 'Book Name', // 原始成员
	pageNumber: 300,
	author: { // 引用成员
		firstname: 'aaa',
		lastname: 'bbb'
	},
	query: function(){ // 成员函数
		console.log('query');
	},
	addPage: function(){
		this.pageNumber++;
		console.log('addPage');
	}
};

console.log(++objBook['pageNumber']);
objBook.query();
objBook['query']();


var students = {
	name: 'Students Name',
	No: 'StudentsNo',
	teacher: {
		name:"xx",
		class:"cc"
	},
	study:function(){
		console.log("i'm studying");
	},
	goBack: function(){
		console.log("go back");
	}
};

students.goBack();
students['study'];
students['parents'] = "fff";

console.log("-------------");
// 对象属性可以增删改查
// 增加一个属性？

var obj = {};
// alert(obj.a);
/**和字典类似 */
obj.a = 'aaa';
obj['1'] = 'bbb';
// alert(obj.a);
/**增加函数 */
obj.f1 = function(){
	console.log('ff.........');
};
obj['f2'] = function(){
	console.log("f2 add");
}
obj['f2'];

/**window 是一个内置对象
 * document
 */
function f2(){
	fun = '函数内定义的全局变量';
	/**无 var 会被认为window对象 */
	//window.aa = 5; // 等价于 aa = 5
};
f2();
// alert(fun);

//var arr = [];
//arr[0] = 'aaa';
//arr[1] = 'bbb';

// 删除一个属性
// 查询一个属性是否存在？
// 1. in
console.log("----------");
console.log('a' in obj);

// 2. hasOwnProperty()
console.log(obj.hasOwnProperty('a'));

// delete
delete obj.a;
console.log('a' in obj);
console.log(obj.hasOwnProperty('a'));

var arr = [];
arr['a'] = 'c';
console.log(arr);
delete arr['a'];
console.log(arr);

// // 修改一个属性
// obj.a = 123;

// // 枚举
// for(var p in obj){
// 	console.log(p);
// }

// obj.a
// obj.toString();

// console.log(obj.propertyIsEnumerable('a'));
// console.log(obj.propertyIsEnumerable('toString()'));

// 构造函数
/**
 * 使用构造函数、构造出对象，
 */
// 我们需要一种函数，能够每次以相同的方式构造对象；
// 同时，改动这个函数，所有的对象都能跟着改变。
// 构造函数，名称已大写字母开头（约定俗成）
/**
 * 构造函数：属性name age gender
 * @param {*} name 
 * @param {*} age 
 * @param {*} gender 
 */
function Student(name, age, gender){
	this.name = name;
	this.age = age;
	this.gender = gender;
}

var std = new Student('Wangli', 30, 'male');
//构造函数有无返回值
//无 new
//有 
function Student2(name, age, gender){
	var object = {};

	object.name = name;
	object.age = age;
	object.gender = gender;
	
	return object;
}

var std2 = Student2('Wangli', 30, 'male');
/**
 * 代码命名规则
 * 匈牙利命名规则 
 * 属性+类型+对象 
 * 	m_成员
 * 	s_静态
 * 类型：i, a,
 * 对象描述：
 * 大驼峰命名规则
 * 
 * 小驼峰命名规则
 * sumSort() getAge()
 */
// 包装类

var n1 = 123;
var n2 = new Number(123);

console.log(typeof(n1));
console.log(typeof(n2));

var s1 = 'aaa';
var s2 = new String('aaa');

console.log(typeof(s1));
console.log(typeof(s2));

var b1 = true;
var b2 = new Boolean(true);

console.log(typeof(b1));
console.log(typeof(b2));

var arr = [1,2,3,4];
arr.length = 2;
console.log(arr);

var str = '1234';
//str.length = 2;
var strTmp = new String(str);
strTmp.length = 2;
// strTmp摧毁
console.log(str);

var iNum = 123;
//iNum.toString();
var iTmp = new Number(iNum);
iTmp.toString();
// iTmp摧毁
console.log(iNum);

true.toString();

// 脚本的预编译
/**
 * 预编译(扫描)
 * 脚本
 *      加载全局变量GO(windows) 上下文
 *      加载脚本文件
 *      预编译
 *          变量申明 var
 *          函数声明 function
 *          非申明
 *      解释执行
 */
// 1, 没有var的变量，都不是变量声明，全部认为是window的全局变量，不参与预编译
//console.log(aa);
//aa = 5;
//console.log(aa);

// 2，即使在函数中，aa也是全局变量
//    是运行时，不是定义时。
//test();
//function test(){
//	a = 5;
//}
//
//console.log(a);

// 3. 脚本中，所有变量声明，在脚本的预编译阶段完成，所有变量的声明与实际的书写位置无关。
//console.log(aa);
//var aa = 5;
//console.log(aa);

// 4. 脚本中，所有函数声明，在脚本的预编译阶段完成，所有函数的声明与实际的书写位置无关。
//console.log(haha);
//function haha(){
//	console.log('h1');
//}

// 5. 脚本中，如果变量与函数同名，那么，函数将覆盖变量。
//console.log(haha);
//
//var haha = 123;
//function haha(){
//	console.log('h1');
//}

// 6. 脚本中，只有函数能够覆盖变量，变量无法覆盖函数。
//console.log(haha);
//function haha(){
//	console.log('h1');
//}
//var haha = 123;

// 7. 脚本中，后面的函数声明会覆盖前面的函数声明，并且，忽略参数。

//console.log(haha);
//
//function haha(a){
//	console.log('haha1');
//}
//
//function haha(a,b){
//	console.log('haha2');
//}
覆盖规则：
    函数覆盖函数(后面覆盖前面 和参数无关)
    函数覆盖变量 
    变量覆盖变量(后面覆盖前面)

// 函数的预编译

// 8. 函数中，所有变量声明，在函数的预编译阶段完成，所有变量的声明与实际的书写位置无关。
//function f(){
//	console.log(aa);
//	var aa = 5;
//	console.log(aa);
//}
//f();

// 9. 函数中，所有函数声明，在函数的预编译阶段完成，所有函数的声明与实际的书写位置无关。
//function f(){
//	console.log(haha);
//	function haha(){
//		console.log('h1');
//	}
//}
//f();

// 10. 函数中，如果变量与函数同名，那么，函数将覆盖变量。
//function f(){
//	console.log(haha);
//	
//	var haha = 123;
//	function haha(){
//		console.log('h1');
//	}
//}
//f();

// 11. 函数中，只有函数能够覆盖变量，变量无法覆盖函数。
//function f(){
//	console.log(haha);
//	function haha(){
//		console.log('h1');
//	}
//	var haha = 123;
//}
//f();

// 12. 函数中，后面的函数声明会覆盖前面的函数声明，并且，忽略参数。
//function f(){
//	console.log(haha);
//	
//	function haha(a){
//		console.log('haha1');
//	}
//	
//	function haha(a,b){
//		console.log('haha2');
//	}
//}
//f();

// 13, 当函数预编译后，遇到需要访问的变量或者函数，优先考虑自己AO中定义的变量和函数
//     如果找不到，才会在其定义的上一层AO中寻找，直到到达GO。
//var scope = 'global';
//function t(){
//	console.log(scope);// undefined
//	var scope = 'local';
//	console.log(scope);// local
//}
//t();
//console.log(scope); // global
//
//GO:
//scope:'global'
//t:function

//console.log(scope);  // undefined
//var scope = 'global';
//function t(){
//	var scope = 't-local';
//	function t2(){
//		console.log(scope); // undefined
//		var scope = 't2-local';
//		console.log(scope); // t2-local
//	}
//	t2();
//	console.log(scope);// t-local
//}
//t();
//console.log(scope); // global

//GO:
//scope: 'global'
//t: function

习题1
//function test(x,x){
//	console.log(x); // function
//	x = 5;
//	console.log(arguments); // [12,5]
//	function x(){}
//}
//test(12,13);
GO:
test: function
test-AO 
    x:undefined
    
//GO:
//test: function

//b = 'cba';
//function a(a, a){
//	console.log(a);// function
//	console.log(b);// undefined
//	var b = 'abc';
//	
//	a();
//	function a(){
//		console.log(a); // function
//		console.log(b); // abc
//	}
//}
//
//a(5,10);

//GO:
//this: window
//a: function
//b: 'cba'
//
//
//a-AO:
//arguments: [5,function]
//a-arguments[1]: function
//b: 'abc'
//this: window
//
//a.a-AO:
//arguments: []
//this: window

//var str = 'aaa';
//str += 1;
//var test = typeof(str);
//if(test.length == 6){
//	test.newproperty = 'string';
////	var obj = new String(test);
////	obj.newproperty = 'string';
////	摧毁 obj
//	
//}
//
//console.log(test.newproperty); // undefined

//var x = 1, y = z = 0;
//function add(n){
//	return n = n + 1;
//}
//
//y = add(x);
//function add(n){
//	return n = n + 3;
//}
//z = add(x);
// 问x: 1
//   y: 4
//   z: 4

// 哪个可以输出：[1,2,3,4,5]
//function foo(x){
//	console.log(arguments);
//	return x;
//}
//foo(1,2,3,4,5);

//function foo(x){
//	console.log(arguments);
//	return x;
//}[1,2,3,4,5]

//function foo(x){
//	console.log(arguments);
//	return x;
//}(1,2,3,4,5);

function test(x, y, a){
	arguments[2] = 10;
	alert(a);
}
test(1,2,3); // 10


正则表达式
做一个可以伸长的div





