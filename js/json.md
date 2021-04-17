### string -> object 三种方法
1. eval() 你自己产生一个string 当做JS脚本，交由JS引擎运行、加括号变成表达式
var strJSON2 = '(' + strJSON + ')';
console.log(typeof(strJSON2),strJSON2);

var obj1 = eval(strJSON2);
console.log(typeof(obj1), obj1)
console.log(eval('('+strJSON+')'))
var obj2 = {
	'name': 'Albad',
	'age': 25
}
console.log(typeof(obj2), obj2)

2. JSON.parse()
var obj2 = JSON.parse(strJSON);
console.log("JSON.parse() : ",typeof(obj2), obj2)

3. jQuery.parseJSON()
var obj3 = jQuery.parseJSON(strJSON);
console.log("jQuery.parseJSON() : ",typeof(obj3), obj3)

### object -> string
1. JSON.stringigy()
var strJSON3 = JSON.stringify(obj1);
console.log("JSON.stringigy() ",typeof(strJSON3),strJSON3);

2. jQuery.toJSON()
var strJSON4 = jQuery.toJSON(obj1);
console.log("jQuery.toJSON()",typeof(strJSON4), strJSON4);


把一张学生成绩单，放入JSON然后解析
学生的信息，包括：name，birthday, gender, class, {course, scale}

var oStdTable = {};
oStdTable.students = [];

var student = {
	'name': '小明',
	'birthday': '1988-03-08',
	'class': '一班',
	'scales': [
		{
			'course': '语文',
			'scale': 92
		},
		{
			'course': '数学',
			'scale': 97
		},
		{
			'course': '英语',
			'scale': 88
		}
	]
};
oStdTable.students.push(student);

var student = {
	'name': '小红',
	'birthday': '1987-09-05',
	'class': '二班',
	'scales': [
		{
			'course': '物理',
			'scale': 92
		},
		{
			'course': '化学',
			'scale': 97
		}
	]
};
oStdTable.students.push(student);

var student = {
	'name': '小齐',
	'birthday': '1990-05-01',
	'class': '一班',
	'scales': [
		{
			'course': '历史',
			'scale': 92
		},
		{
			'course': '地理',
			'scale': 97
		}
	]
};
oStdTable.students.push(student);


var sStdTable = JSON.stringify(oStdTable);
console.log(sStdTable);

var jsonTable = JSON.parse(sStdTable);
for(var x in jsonTable.students){
	console.log(jsonTable.students[x].name);
	console.log(jsonTable.students[x].birthday);
	console.log(jsonTable.students[x].class);
	
	var scales = jsonTable.students[x].scales;
	for(var y in scales){
		console.log('    ' + scales[y].course + ':' + scales[y].scale );
	}
}
