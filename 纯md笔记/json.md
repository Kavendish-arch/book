### json 
1. JavaScript Object Notation javascript 对象表示法
        java :
           Person p = new Person
           
        javascript
            var Per = {"name": " ", "age":" "}
            
        json 用于存储，交换文本信息 进行数据传输 比xml 更小，更快容易解析
2. 语法
    1. 数据以键值对存储 
            键：引号，或不加
            值：1. 数字 2. 字符串 3. 逻辑值 4. 数组 5. 对象 6. null
3. json 和 java 对象互换
    1. java对象转json
        * json 解析器：jsonlib, Gson, fastjson, jackson
        jackson:
            1. 导入jar包
            2. 创建jackson 核心对象 objectMapper
            3. 调用objectMapper 相关方法进行转换
        @JsonIgnore：排除属性
        @JsonFormat：属性格式化
        复杂对象的转换
        List 集合 数组
        Map  
```
    User user = new User("jack","sdds", new Date());
    ObjectMapper mapper = new ObjectMapper();
    String u = mapper.writeValueAsString(user);
    System.out.println(" " + u);    
```	
    2. json 转 java
        1. 导入jar包
        2. 创建jackson 核心对象 objectMapper
        3. 调用objectMapper 相关方法进行转换
```
    String user = "{\"username\" :\"JOSHsd\", \"password\" : \"sdhdkslhd\"}";
    ObjectMapper mapper = new ObjectMapper();
    User u = mapper.readValue(user, User.class);
    System.out.println(" " + u);    
```
Jackson 的核心模块由三部分组成。
* jackson-core，核心包，提供基于"流模式"解析的相关 API，它包括 JsonPaser 和 JsonGenerator。 Jackson 内部实现正是通过高性能的流模式 API 的 JsonGenerator 和 JsonParser 来生成和解析 json。
* jackson-annotations，注解包，提供标准注解功能；
* jackson-databind ，数据绑定包， 提供基于"对象绑定" 解析的相关 API （ ObjectMapper ） 和"树模型" 解析的相关 API （JsonNode）；基于"对象绑定" 解析的 API 和"树模型"解析的 API 依赖基于"流模式"解析的 API。
清单 1.在 pom.xml 的 Jackson 的配置信息
<dependency> 
<groupId>com.fasterxml.jackson.core</groupId> 
<artifactId>jackson-databind</artifactId> 
<version>2.9.1</version> 
</dependency>
jackson-databind 依赖 jackson-core 和 jackson-annotations，当添加 jackson-databind 之后， jackson-core 和 jackson-annotations 也随之添加到 Java 项目工程中。在添加相关依赖包之后，就可以使用 Jackson。

* Jackson 根据它的默认方式序列化和反序列化 java 对象，若根据实际需要，灵活的调整它的默认方式，可以使用 Jackson 的注解。常用的注解及用法如下。

* Jackson 的 常用注解

@JsonProperty	用于属性，把属性的名称序列化时转换为另外一个名称。示例： 
@JsonProperty("birth_ d ate") 
private Date birthDate;

@JsonFormat	用于属性或者方法，把属性的格式序列化时转换成指定的格式。示例： 
@JsonFormat(timezone = "GMT+8", pattern = "yyyy-MM-dd HH:mm") 
public Date getBirthDate()

@JsonPropertyOrder	用于类， 指定属性在序列化时 json 中的顺序 ， 示例： 
@JsonPropertyOrder({ "birth_Date", "name" }) 
public class Person

@JsonCreator	用于构造方法，和 @JsonProperty 配合使用，适用有参数的构造方法。 示例： 
@JsonCreator 
public Person(@JsonProperty("name")String name) {…}

@JsonAnySetter	用于属性或者方法，设置未反序列化的属性名和值作为键值存储到 map 中 
@JsonAnySetter 
public void set(String key, Object value) { 
map.put(key, value); 
}
@JsonAnyGetter	用于方法 ，获取所有未序列化的属性 
public Map<String, Object> any() { return map; }