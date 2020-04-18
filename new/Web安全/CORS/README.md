# CORS是一个W3C标准，全称是"跨域资源共享"（Cross-originresource sharing）。https://www.mi1k7ea.com/2019/08/18/CORS%E8%B7%A8%E5%9F%9F%E6%BC%8F%E6%B4%9E%E6%80%BB%E7%BB%93/
浏览器的同源策略的本质是：一个域名的JS(XMLHttpRequest())，在未经允许的情况下是不得读取另一个域名的内容，但浏览器并不阻止向另一个域名发送请求。
CORS跨域漏洞的本质是服务器配置不当，即Access-Control-Allow-Origin设置为*（貌似ACAO字段设置为*时，浏览器会阻止我们获取响应报文的内容，因为这是浏览器最后一道防线对用户最后的保护TT）或是直接取自请求头Origin字段，Access-Control-Allow-Credentials设置为true（使用cookie）。
CORS攻击点，恶意网站给浏览器的返回中存在XMLHttpRequest()或者$.get(url)的脚本进行CORS，当服务器配置不当时就会通过CORS从而使浏览器继续执行AJAX泄露隐私信息。
防御：若非必需则不开启CORS；若业务必需开启CORS，需严格限制外域白名单，禁止使用通配符*，同时尽量避免使用Access-Control-Allow-Credentials头字段。