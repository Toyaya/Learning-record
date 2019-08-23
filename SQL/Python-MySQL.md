# Python MySQL
```
import pymysql
```
###### 1、# 连接database
```
conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='mxx951130',
    db='new_schema',
)

```
###### 2、# 得到一个可以执行SQL语句的光标对象
```
cursor = conn.cursor()  
# 执行完毕返回的结果集默认以元组显示
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# 得到一个可以执行SQL语句并且将结果作为字典返回的游标
```

###### 3、# 定义要执行的SQL语句
```
sql = """
select * from new_schema.blog
"""
```

###### 4、# 执行SQL语句
```
cursor.execute(sql)  
cuisor.execute(sql,[name])
```

###### 5、#打印输出SQL语句
```
rs=cursor.fetchall()
for r in rs:
    print(r)
```

###### 6、# 关闭光标对象
```
cursor.close()
```

###### 7、# 关闭数据库连接
```
conn.close()
```

###### 8、# 涉及写操作要注意提交
```
conn.commit()
```

###### 9、# 获取最新的那一条数据的ID
```
last_id = cursor.lastrowid
```

###### 10、# 可以获取指定数量的数据
```
cursor.fetchmany(3)
```

###### 11、# 有异常就回滚
```
conn.rollback()
```