# redis 安装
1. yum apt 安装
sudo apt-get install redis-server
2. 服务端启动
sudo /etc/init.d/redis-server status | start | stop | restart
3. 客户端连接
redis-cli -h IP地址 -p 端口
redis-cli 默认连接本机的6379端口
127.0.0.1:6379>ping
PONG

4. 常用命令
* 切换库 select number
* 查看键 keys * 
* 键类型 TYPE key
* 键是否存在 exists key
* 删除键 del key
* 键重命名 rename key newkey
* 返回旧值并设置新值（如果键不存在，就创建并赋值）getset key value
* 清除当前库中所有数据（慎用）flushdb
* 清除所有库中所有数据（慎用）flushall

序号	命令及描述
1	DEL key         该命令用于在 key 存在时删除 key。
2	DUMP key        序列化给定 key ，并返回被序列化的值。
3	EXISTS key      检查给定 key 是否存在。
4	EXPIRE key seconds                      为给定 key 设置过期时间，以秒计。
5	EXPIREAT key timestamp EXPIREAT         的作用和 EXPIRE 类似，都用于为 key 设置过期时间。不同在于EXPIREAT命令接受的时间参数是UNIX时间戳(unix timestamp)。
6	PEXPIRE key milliseconds                设置 key 的过期时间以毫秒计。
7	PEXPIREAT key milliseconds-timestamp    设置 key 过期时间的时间戳(unix timestamp) 以毫秒计
8	KEYS pattern    查找所有符合给定模式( pattern)的 key 。
9	MOVE key db     将当前数据库的 key 移动到给定的数据库 db 当中。
10	PERSIST key     移除 key 的过期时间，key 将持久保持。
11	PTTL key        以毫秒为单位返回 key 的剩余的过期时间。
12	TTL key         以秒为单位，返回给定 key 的剩余生存时间(TTL, time to live)。
13	RANDOMKEY       从当前数据库中随机返回一个 key 。
14	RENAME key newkey 修改 key 的名称
15	RENAMENX key newkey 仅当 newkey 不存在时，将 key 改名为 newkey 。
16	TYPE key        返回 key 所储存的值的类型。

1. 设置一个key-value    set key value
2. 获取key的值  get key
3. key不存在时再进行设置(nx)     set key value nx
4. 设置过期时间(ex)   set key value ex seconds
5. 同时设置多个key-value mset key1 value1 key2 value2 key3 value3
6. 同时获取多个key-value mget key1 key2 key3 

> 整数操作
INCRBY key 步长
DECRBY key 步长
INCR key : +1操作
DECR key : -1操作
* 应用场景: 抖音上有人关注你了，是不是可以用INCR呢，如果取消关注了是不是可以用DECR

* 浮点数操作: 先转为数字类型，然后再进行相加减，不能使用append
incrbyfloat key step

4、列表
## 列表常用操作
* 增
1、LPUSH     key value1 value2 
2、RPUSH     key value1 value2
3、RPOPLPUSH source destination
4、LINSERT   key after|before value newvalue
* 查
5、LRANGE key start stop
6、LLEN key
* 删
7、LPOP key
8、RPOP key
9、BLPOP key timeout
10、BRPOP key timeout
11、LREM key count value
12、LTRIM key start stop
* 改
13、LSET key index newvalue

 
# python使用

import redis
r = redis.Redis(host='192.168.43.49',port=6379,db=0)
* ['mysql','redis']
r.lpush('pylist','redis','mysql')
* ['mysql','redis','django','spider']
r.rpush('pylist','django','spider')
* ['mysql','redis','django','spider','AI']
r.linsert('pylist','after','spider','AI')
* 5
print(r.llen('pylist'))
* ['redis','django','spider']
r.lpop('pylist')
r.rpop('pylist')
* ['redis','django','spider']
print(r.lrange('pylist',0,-1))
* ['redis','spider']
r.lrem('pylist',0,'django')
* 返回True，['redis']
r.ltrim('pylist',0,0)
* 返回True，['spiderman']
r.lset('pylist',0,'spiderman')
r.delete('pylist')

## 字符串代码示例
import redis
r = redis.Redis(host='192.168.43.49',port=6379,db=0)
r.set('mystring','python')
* b'python'
print(r.get('mystring'))
* False
print(r.setnx('mystring','socket'))
* mset：参数为字典
r.mset({'mystring2':'mysql','mystring3':'mongodb'})
* mget：结果为一个列表
print(r.mget('mystring','mystring2','mystring3'))
* mystring长度：6
print(r.strlen('mystring'))
* 数字类型操作
r.set('number',10)
r.incrby('number',5)
r.decrby('number',5)
r.incr('number')
r.decr('number')
r.incrbyfloat('number',6.66)
r.incrbyfloat('number',-6.66)
* b'10'
print(r.get('number'))


6、Hash散列
6.1基本命令操作

* 1、设置单个字段
HSET key field value
HSETNX key field value
* 2、设置多个字段
HMSET key field value field value
* 3、返回字段个数
HLEN key
* 4、判断字段是否存在（不存在返回0）
HEXISTS key field
* 5、返回字段值
HGET key field
* 6、返回多个字段值
HMGET key field filed
* 7、返回所有的键值对
HGETALL key
* 8、返回所有字段名
HKEYS key
* 9、返回所有值
HVALS key
* 10、删除指定字段
HDEL key field 
* 11、在字段对应值上进行整数增量运算
HINCRBY key filed increment
* 12、在字段对应值上进行浮点数增量运算
HINCRBYFLOAT key field increment

6.2phthon基本方法

* 1、更新一条数据的属性，没有则新建
hset(name, key, value)
* 2、读取这条数据的指定属性， 返回字符串类型
hget(name, key)
* 3、批量更新数据（没有则新建）属性,参数为字典
hmset(name, mapping)
* 4、批量读取数据（没有则新建）属性
hmget(name, keys)
* 5、获取这条数据的所有属性和对应的值，返回字典类型
hgetall(name)
* 6、获取这条数据的所有属性名，返回列表类型
hkeys(name)
* 7、删除这条数据的指定属性
hdel(name, *keys)
7、集合
7.1特点
1、无序、去重
2、元素是字符串类型
3、最多包含2^32-1个元素

7.2基本命令
* 1、增加一个或者多个元素,自动去重
SADD key member1 member2
* 2、查看集合中所有元素
SMEMBERS key
* 3、删除一个或者多个元素，元素不存在自动忽略
SREM key member1 member2
* 4、元素是否存在
SISMEMBER key member
* 5、随机返回集合中指定个数的元素，默认为1个
SRANDOMMEMBER key [count]
* 6、返回集合中元素的个数，不会遍历整个集合，只是存储在键当中了
SCARD key
* 7、把元素从源集合移动到目标集合
SMOVE source destination member
* 8、差集(number1 1 2 3 number2 1 2 4)
SDIFF key1 key2 
* 9、差集保存到另一个集合中
SDIFFSTORE destination key1 key2
* 10、交集
SINTER key1 key2
SINTERSTORE destination key1 key2
* 11、并集
SUNION key1 key2
SUNIONSTORE destination key1 key2

7.3 python操作set
* 1、给name对应的集合中添加元素
sadd(name,values)
r.sadd("set_name","tom")
r.sadd("set_name","tom","jim")
* 2、获取name对应的集合的所有成员: 集合
smembers(name)
* 3、获取name对应的集合中的元素个数
scard(name)
r.scard("set_name")
* 4、检查value是否是name对应的集合内的元素:True|False
sismember(name, value)

* 5、随机删除并返回指定集合的一个元素
spop(name)

* 6、删除集合中的某个元素
srem(name, value) 
r.srem("set_name", "tom")

* 7、获取多个name对应集合的交集
sinter(keys, *args)

r.sadd("set_name","a","b")
r.sadd("set_name1","b","c")
r.sadd("set_name2","b","c","d")

print(r.sinter("set_name","set_name1","set_name2"))
#输出:｛b'b'｝

* 8、获取多个name对应的集合的并集
sunion(keys, *args)
r.sunion("set_name","set_name1","set_name2")

8、有序集合
8.1python操作sorted set

import redis
r = redis.Redis(host='192.168.43.49',port=6379,password='123456',db=0)
* 注意第二个参数为字典
r.zadd('salary',{'tom':6000,'jim':8000,'jack':12000})
* 结果为列表中存放元组[(),(),()]
print(r.zrange('salary',0,-1,withscores=True))
print(r.zrevrange('salary',0,-1,withscores=True))
* start:起始值,num:显示条数
print(r.zrangebyscore('salary',6000,12000,start=1,num=2,withscores=True))
* 删除
r.zrem('salary','tom')
print(r.zrange('salary',0,-1,withscores=True))
* 增加分值
r.zincrby('salary',5000,'jack')
print(r.zrange('salary',0,-1,withscores=True))
* 返回元素排名
print(r.zrank('salary','jack'))
print(r.zrevrank('salary','jack'))
* 删除指定区间内的元素
r.zremrangebyscore('salary',6000,8000)
print(r.zrange('salary',0,-1,withscores=True))
* 统计元素个数
print(r.zcard('salary'))
* 返回指定范围内元素个数
print(r.zcount('salary',6000,20000))
* 并集
r.zadd('salary2',{'jack':17000,'lucy':8000})
r.zunionstore('salary3',('salary','salary2'),aggregate='max')
print(r.zrange('salary3',0,-1,withscores=True))
* 交集
r.zinterstore('salary4',('salary','salary2'),aggregate='max')
print(r.zrange('salary4',0,-1,withscores=True))


9、数据持久化
9.1 服务器执行客户端发送的SAVE或者BGSAVE命令

127.0.0.1:6379> SAVE
OK
* 特点
1、执行SAVE命令过程中，redis服务器将被阻塞，无法处理客户端发送的命令请求，在SAVE命令执行完毕后，服务器才会重新开始处理客户端发送的命令请求
2、如果RDB文件已经存在，那么服务器将自动使用新的RDB文件代替旧的RDB文件
* 工作中定时持久化保存一个文件

127.0.0.1:6379> BGSAVE
Background saving started
* 执行过程如下
1、客户端 发送 BGSAVE 给服务器
2、服务器马上返回 Background saving started 给客户端
3、服务器 fork() 子进程做这件事情
4、服务器继续提供服务
5、子进程创建完RDB文件后再告知Redis服务器

* 配置文件相关操作
/etc/redis/redis.conf
263行: dir /var/lib/redis * 表示rdb文件存放路径
253行: dbfilename dump.rdb  * 文件名


9.1 设置配置文件条件满足时自动保存（使用最多）

* 命令行示例
redis>save 300 10
  表示如果距离上一次创建RDB文件已经过去了300秒，并且服务器的所有数据库总共已经发生了不少于10次修改，那么自动执行BGSAVE命令
redis>save 60 10000
  表示如果距离上一次创建rdb文件已经过去60秒，并且服务器所有数据库总共已经发生了不少于10000次修改，那么执行bgsave命令

* redis配置文件默认
218行: save 900 1
219行: save 300 10
220行: save 60 10000
  1、只要三个条件中的任意一个被满足时，服务器就会自动执行BGSAVE
  2、每次创建RDB文件之后，服务器为实现自动持久化而设置的时间计数器和次数计数器就会被清零，并重新开始计数，所以多个保存条件的效果不会叠加


9.3 数据持久化分类之 - AOF（AppendOnlyFile，默认未开启）
9.3.1特点

1、存储的是命令，而不是真实数据
2、默认不开启
* 开启方式（修改配置文件）
1、/etc/redis/redis.conf
  672行: appendonly yes * 把 no 改为 yes
  676行: appendfilename "appendonly.aof"
2、重启服务
  sudo /etc/init.d/redis-server restart

 

9.3.2RDB缺点

1、创建RDB文件需要将服务器所有的数据库的数据都保存起来，这是一个非常消耗资源和时间的操作，所以服务器需要隔一段时间才创建一个新的RDB文件，也就是说，创建RDB文件不能执行的过于频繁，否则会严重影响服务器的性能
2、可能丢失数据

  
9.3.3AOF持久化原理及优点**

* 原理
   1、每当有修改数据库的命令被执行时，服务器就会将执行的命令写入到AOF文件的末尾
   2、因为AOF文件里面存储了服务器执行过的所有数据库修改的命令，所以给定一个AOF文件，服务器只要重新执行一遍AOF文件里面包含的所有命令，就可以达到还原数据库的目的

* 优点
  用户可以根据自己的需要对AOF持久化进行调整，让Redis在遭遇意外停机时不丢失任何数据，或者只丢失一秒钟的数据，这比RDB持久化丢失的数据要少的多


10、主从复制
10.1 定义

1、一个Redis服务可以有多个该服务的复制品，这个Redis服务成为master，其他复制品成为slaves
2、master会一直将自己的数据更新同步给slaves，保持主从同步
3、只有master可以执行写命令，slave只能执行读命令

  

10.2实现方式
10.2.1 方式一（命令行实现1）

   redis-server --slaveof <master-ip> <master-port>


* 从服务端
redis-server --port 6300 --slaveof 127.0.0.1 6379
* 从客户端
redis-cli -p 6300
127.0.0.1:6300> keys * 
* 发现是复制了原6379端口的redis中数据
127.0.0.1:6380> set mykey 123
(error) READONLY You can't write against a read only slave.
127.0.0.1:6380> 
* 从服务器只能读数据，不能写数据


10.2.2 方式二(修改配置文件)

* 修改配置文件
vi redis_6300.conf
slaveof 127.0.0.1 6379
port 6300
* 启动redis服务
redis-server redis_6300.conf
* 客户端连接测试
redis-cli -p 6300
127.0.0.1:6300> hset user:1 username guods
(error) READONLY You can't write against a read only slave.


问题总结

1、一个Master可以有多个Slaves
2、Slave下线，只是读请求的处理性能下降
3、Master下线，写请求无法执行
4、其中一台Slave使用SLAVEOF no one命令成为Master，其他Slaves执行SLAVEOF命令指向这个新的Master，从它这里同步数据
* 以上过程是手动的，能够实现自动，这就需要Sentine哨兵，实现故障转移Failover操作

redis分布式锁

def test(request):
	* 解决方法二:redis分布式锁
    import redis
    pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
    r = redis.Redis(connection_pool=pool)
    while True:
        try:
            with r.lock('guoxiaonao', blocking_timeout=3) as lock:
                u = UserProfile.objects.get(username='guoxiaonao')
                u.score += 1
                u.save()
            break
        except Exception as e:
            print('lock is failed')
    
    return HttpResponse('HI HI HI')