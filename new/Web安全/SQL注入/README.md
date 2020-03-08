#  输入设计的非正常的SQL语句，例如输入 1 OR 1=1 --
例如SELECT * FROM USER WHERE ID=$id and PWD=$pwd;输入后变成SELECT * FROM USER WHERE ID=1 OR 1=1 --and PWD=$pwd;实现了USER表的提出
使用sqlmap可以方便测试 

