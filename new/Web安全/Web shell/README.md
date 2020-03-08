# 上传Web shell并通过url方式运行shell控制Web服务器
通常服务器禁止上传可运行的文件，例如.php此时可以上传.html文件，.html文件中的php代码也能运行，但更严格的安全环境下可能失败，需要测试文件拓展名
放入特殊字符%空格*/\等
重复拓展名webshell.txt.php   webshell.txt.txt.txt.php
编码（使用迂回方法）webshell.php.kr  webshell.php.iso8859-8


