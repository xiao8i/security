#  XXE （XML External Entity injection）XML 外部实体注入漏洞		DTD的外部声明：<!ENTITY content SYSTEM "filename">
防御：使用xml外部实体非常不安全，可以读取文件，也可以执行命令。
禁止使用DTD的外部声明；
对用户提交过来的XML数据进行过滤（仍然不安全，最好禁用）
