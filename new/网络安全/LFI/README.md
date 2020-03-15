# LFI本地文件包含
php中引起文件包含漏洞的4个函数：include()、require()、file()、readfile().
例如<?php
    $file = $_GET['file'];
    include $file;
?>
通过访问.php?file=xxx 即可获取本地文件，还可以通过本地文件包含漏洞来getshell，例如包含日志及环境文件、PHP wrapper和phpinfo。https://www.jianshu.com/p/8803aff98bfa
包含日志及环境文件：例如在请求url后面加上<?php @eval($_POST[c]);?>会在error.log中记录这段php代码，再通过本地文件包含打开日志文件即可运行这段代码拿到shell。
php Wrappers：使用php wrapper例如php://input、php://filter、data://等包含文件，包装器wrapper可以用来绕过某些安全过滤器。
phpinfo：当PHP设置file_uploads=on时，PHP将会接收上传到任何PHP页面的文件，这些文件会存储为临时文件直到页面请求处理完毕。可以将webshell写入文件上传，通过包含临时文件获得shell。
RFI远程文件包含，PHP的配置选项allow_url_include为ON。RFI能够获取远程服务器上的文件并执行，隐患很大，一般不会开启。