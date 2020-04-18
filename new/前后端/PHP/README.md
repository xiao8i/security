# PHP-Personal HomePage超文本预处理器，脚本语言，用于动态页面开发。
<html>
<body>
	<?php
		……
	?> 
</body>
</html>
不需要关键字来定义变量，但是需要以$开头(其实是指针)，$$a=$b若$a='b'(替换即可)
$a=$b;值传递
$a=&$b;引用传递(把b指向的内容取地址传递给a，正好a也指向了相同的内容。)
.拼接字符串，并用.=拼接并赋值
@错误抑制符，不显示报错
function f(&$args){}，加上&修饰的实参是引用传值，否则是复制传值
注意PHP中的全局变量并不能在函数内部访问，但是可以通过超全局变量(PHP的预定义变量)$GLOBALS['全局变量名']来访问，也可以通过global关键字修饰global $a；$a = '';global会使得全局和局部使用同一块内存地址保存，从而实现共有。
静态变量：在函数内部使用static定义的变量，编译时初始化，每次调用共享。
可变函数 $f = '函数名'；则可以$f()调用函数
匿名函数：闭包用到，$inner = function() use($name){}; return $inner;
''字符串只能识别\'而""字符串只不能识别\',所以"{$a}"可以解析变量
数组$arr=[];也可以$arr[key]=value;等价$arr=array['key'=>value];注意PHP是键值对数组
操作mysql	mysql_connect(库，用户名，密码)和mysql_query(mysql语句)
