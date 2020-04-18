# 前端 nginx (可以作为一个 HTTP 服务器进行网站的发布处理，另可以作为反向代理进行负载均衡的实现)抗并发，后端 apache 集群，配合起来会更好。apache 是同步多进程模型，一个连接对应一个进程，而 nginx 是异步的，多个连接（万级别）可以对应一个进程(应用epoll)https://www.cnblogs.com/changning0822/p/7844004.html
数据库mysql、oracle、nosql(便于扩展)等
web前端（html、css、js）框架Jquery、Bootstrap	web后端PHP、Java、python对应框架ThinkPHP、Spring、Django/Flask  Web数据库MongoDB（采用ORM，Nosql类型）

中间件tomcat(服务器)、redis（数据结构服务器，日志型Key-Value数据库）、RabbitMQ  	
WSGI(python)https://www.liaoxuefeng.com/wiki/897692888725344/923057027806560
如今java中三大框架有两套：SSM SSH

SSM：Spring+SpringMVC+Mybatis

SSH：Spring+Struts+Hibernate

AMP:Apache + Mysql +PHP