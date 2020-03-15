# 跨站脚本攻击，将<script>标签作为内容进行get、post
反射型XSS：将<script>内容放入url中，通过点击链接执行脚本。
存储型XSS：post将<script>内容存储到服务器，例如留言、bbs、图片都是可以存储的，此时再访问页面便会执行脚本。
DOM型XSS：客户端的漏洞。
防御：对用户输入做转义处理，这样就不会执行脚本，例如htmlspecialchars和htmlentities函数。
https://www.jianshu.com/p/4fcb4b411a66