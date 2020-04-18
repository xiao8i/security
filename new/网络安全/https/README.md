# SSL、TSL(SSL存在POODLE漏洞，请使用TSL)在会话层，专为应用层HTTP协议提供加密、认证以及校验。可以看出不能保护TCP协议（因为在TCP的上层），保护TCP、UDP等传输层需要用到IPsec
POODLE漏洞，SSL3.0在CBC模式下当填充数据长度为分组长度时，通过把加密分组数据替换到填充数据可以解析加密分组数据的最后一字节，造成cookie泄露，注意TSL1.1，1.2可降级为ssl3.0
http://g.xker.com/148273.html
https://blog.csdn.net/Ping_Fani07/article/details/40350113?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task
Heartbleed心血漏洞，是一个出现在加密程序库OpenSSL的安全漏洞，该程序库广泛用于实现互联网的传输层安全（TLS）协议。实现TLS的心跳扩展时没有对输入进行适当验证（缺少边界检查），因此漏洞的名称来源于“心跳”（heartbeat）。在攻击场景中,请求的长度字段远大于请求本身的数据长度，造成服务端缓冲区过读，即应答的数据比应该允许读取的还多。
在memcpy()调用用户输入内容作为长度参数之前未能正确进行边界检查