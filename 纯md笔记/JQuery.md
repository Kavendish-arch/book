### JQuery
1. 概念
    1.x 
    2.x
    3.x
2. 使用
3. JQuery 对象
## 元素选取 *选择器*
## Jquery选择器允许对HTML元素组或者单个元素进行操作
Jquery选择器基于id，类（class属性），类型（Tag），属性（Attr），属性值等进行查找或者选择HTML元素。

1. 基本选择器 
* 表示所有
* 标签选择器： $("标签名") 所有元素
* id选择器 ： $("#id") 
    3. 类选择器： $(".class")
    4. 并集选择器：$("选择器1， 选择器2")
2. 属性选择器
    1. 属性名：$("A[属性名]")
*    2. *属性选择器 $("A[属性名=属性值]")
    3. 复合属性选择器 $("A[属性名=属性值][ ]")
3. 层级选择器
    1. 后代选择器 ： $(" A B ")
*    2. *子选择器：$("A > B")
4. 过滤选择器
    1. 首元素 first
*    2. *尾元素 last
    3. 非元素 not(selecter)
    4. 偶数选择： even 
    5. 技术选择： odd
    6. 等于 eq(index)
    7. 大于 gt(index)
    8. 小于 lt(index)
    9. 标题 Header获取标题
5. 表单选择器
    1. 可用元素选择器 enabled
*    2. *不可用元素选择器 disabled
    3. 选中元素选择器 checked
    4. 选中元素选择器 selected

## DOM操作 *DOM操作*
1. 内容操作
    1. html() 标签体内容
*    2. *text() 文本内容 不包括子标签
    3. val()
2. 属性操作
    1. 通用属性
        1. attr()  固有属性
    *    2. *removeAttr()
        3. prop    自定义属性
        4. removeProp()
*    2. *对class属性操作
        1. addClass()
    *    2. *removeClass()
        3. toggleClass()
3. CRUD操作
    1. append() 父元素追加到末尾
*    2. *prepend() 父元素追加到开头
    3. appendTo() 追加到内部末尾
    4. prependTo() 追加到内部开头
    5. after() 添加到元素后边
    6. before() 添加到元素前面
    7. insert() 插入
    8. insertBefore() 插入
    9. remove() 移除
    10. empty 清空
    click 	    keypress 	submit 	    load
    dblclick 	keydown 	change 	    resize
    mouseenter 	keyup 	    focus 	    scroll
    mouseleave 	blur 	    unload
    hover

### JQuery 高级
1. 动画
    1. 三种显示和隐藏
    1. 默认显示和隐藏
        1. show([speed, [easing],[fn]])
    *    2. *hide( [speed, [easing], [fn]] )
        3. toggle( [speed], [easing], [fn])
*    2. *滑动显示和隐藏方式
        1. slipdeDown( [speed], [easing], [fn]);
    *    2. *slideup ( [speed], [easing], [fn]);
        3. fadeToggle ( [speed], [easing], [fn])
    3. 淡入，淡出显示，和隐藏方式
        1. fadeIn ( [speed], [easing], [fn]);
    *    2. *fadeOut ( [speed], [easing], [fn]);
        3. fadeToggle ( [speed], [easing], [fn]);
    