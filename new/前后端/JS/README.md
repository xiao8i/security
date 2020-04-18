# JavaScript 	https://www.liaoxuefeng.com/wiki/1022910821149312/1023021250770016
不要使用==比较，始终坚持使用===比较。
另一个例外是NaN这个特殊的Number与所有其他值都不相等，包括它自己：
如果一个变量没有通过var申明就被使用，那么该变量就自动被申明为全局变量：修正加'use strict';
区分·'\x41';和0x41；
需要特别注意的是，字符串是不可变的，如果对字符串的某个索引赋值，不会有任何错误，但是，也没有任何效果：
大多数其他编程语言不允许直接改变数组的大小，越界访问索引会报错。然而，JavaScript的Array却不会有任何错误。在编写代码时，不建议直接修改Array的大小，访问索引时要确保索引不会越界。
`如果字符串中有${变量}` /+变量+
JavaScript的函数内部如果调用了this,以对象的方法形式调用正常，单独调用函数this指向全局对象，也就是window。
JavaScript的Date对象月份值从0开始，牢记0=1月，1=2月，2=3月，……，11=12月。
正则：两种写法是一样的：var re1 = /ABC\-001/;和var re2 = new RegExp('ABC\\-001');

JSON是JavaScript Object Notation的缩写，它是一种数据交换格式。在JSON出现之前，大家一直用XML(一种纯文本格式)来传递数据。把任何JavaScript对象变成JSON，就是把这个对象序列化成一个JSON格式的字符串，只需要把它反序列化成一个JavaScript对象，就可以在JavaScript中直接使用这个对象了。
在JavaScript中，可以用关键字new来调用函数，并返回一个对象：
window对象不但充当全局作用域，而且表示浏览器窗口。
location对象表示当前页面的URL信息。可以用location.href获取。
document对象表示当前页面。由于HTML在浏览器中以DOM形式表示为树形结构，document对象就是整个DOM树的根节点。JavaScript可以通过document.cookie读取到当前页面的Cookie,设定了httpOnly的Cookie将不能被JavaScript读取。
修改innerText或textContent属性而不是innerHTML属性，这样可以自动对字符串进行HTML编码，保证无法设置任何HTML标签：避免innerHTML可能带来的XSS
id用来标记标签，form中value对应输入值，name对应value提交的键，没有name的value不会提交。
执行JavaScript代码时，总是以单线程模式执行，执行多任务实际上都是异步调用。
在HTML表单中，可以上传文件的唯一控件就是<input type="file">，HTML5的File API提供了File和FileReader两个主要对象，可以获得文件信息并读取文件。
AJAX：Asynchronous JavaScript and XML，意思就是用JavaScript执行异步网络请求。Web的运作原理：一次HTTP请求对应一个页面，但是AJAX可以使页面保留，配合XMLHttpRequest()，Promise类。
请求外域url：
一是通过Flash插件发送HTTP请求；
二是通过在同源域名下架设一个代理服务器来转发，JavaScript负责把请求发送到代理服务器，代理服务器再把结果返回，这样就遵守了浏览器的同源策略，'/proxy?url=http://www.sina.com.cn'
第三种方式称为JSONP，它有个限制，只能用GET请求，并且要求返回JavaScript。这种方式跨域实际上是利用了浏览器允许跨域引用JavaScript资源（其实拥有"src"这个属性的标签都拥有跨域的能力(注意src是无返回的，即不需要返回给服务器-要求跨域请求的服务器，所以不涉及CORS)，比如<script>、<img>、<iframe>）：<script src="http://example.com/abc.js"></script>
四HTML5支持新的跨域策略：CORS	$.get(url）和XMLHttpRequest()请求外域url都涉及SORS策略

jQuery是JavaScript世界中使用最广泛的一个库(操作DOM), <script src="//code.jquery.com/jquery-1.11.3.min.js"></script>
$是全局变量（函数）jQuery的别名
$(function () {...})是document对象的ready事件处理函数简写

#11跳到锚点11即name或id=11标签处，#0当前页面

underscore为JavaScript提供了一套完善的函数式编程的接口（函数库），underscore把自身绑定到唯一的全局变量_上

Node.js是JavaScript的后端开发，一般JavaScript在浏览器中运行，使用Node.js后就可以开发*.js的后端程序，优点是与JavaScript易接融，但是只能异步IO（也是由JavaScript决定的）Node.js的唯一全局对象global而不是window
koa是基于Node.js的web框架(模块)，koa中间件(Node.js模块)——koa-router、koa-bodyparser
ASP/JSP/PHP创建动态HTML：由于Web应用特点是修改频繁，用C/C++这样的低级语言非常不适合Web开发，而脚本语言由于开发效率高，与HTML结合紧密，因此，迅速取代了CGI模式。ASP是微软推出的用VBScript脚本编程的Web开发技术，而JSP用Java来编写脚本，PHP本身则是开源的脚本语言。JSP全称Java Server Pages，是一种动态网页开发技术。它使用JSP标签在HTML网页中插入Java代码。标签通常以<%开头以%>结束。
MVC：为了解决直接用脚本语言嵌入HTML导致的可维护性差的问题，Web应用也引入了Model-View-Controller的模式，来简化Web开发。ASP发展为ASP.Net，JSP和PHP也有一大堆MVC框架。
MVC：Model-View-Controller，中文名“模型-视图-控制器”。异步函数是C：Controller，Controller负责业务逻辑，比如检查用户名是否存在，取出用户信息等等；包含变量{{ name }}的模板就是V：View，View负责显示逻辑，通过简单地替换一些变量，View最终输出的就是用户看到的HTML。MVC中的Model在哪？Model是用来传给View的，这样View在替换变量的时候，就可以从Model中取出相应的数据。
WebSocket协议在浏览器和服务器之间建立一个不受限的双向通信的通道。TCP协议本身就实现了全双工通信，但是HTTP协议的请求－应答机制限制了全双工通信。WebSocket连接建立以后，其实只是简单规定了一下：接下来，咱们通信就不使用HTTP协议了（code101），直接互相发数据吧。
REST（Representational State Transfer）架构模式取代了复杂而笨重的SOAP，成为Web API(数据接口)的标准。REST  API只是一种请求类型和响应类型均为JSON的HTTP请求，(get/post/put/delete请求都可以)把前端页面看作是一种用于展示的客户端，是REST架构可扩展的一个关键。
Web API就是为前端页面提供数据、操作数据的接口。如果一个URL返回的不是HTML，而是机器能直接解析的数据，这个URL就可以看成是一个Web API。比如，读取http://localhost:3000/api/products/123
MVVM是Model-View-ViewModel的缩写MVVM的设计思想：关注Model的变化，让MVVM框架去自动更新DOM的状态，从而把开发者从操作DOM的繁琐步骤中解脱出来！比JQuery还要简单，把DOM整体当做对象处理。MVVM框架：Vue.js
但是MVVM不是万能的，它的目的是为了解决复杂的前端逻辑。对于以展示逻辑为主的页面，例如，新闻，博客、文档等，不能使用MVVM展示数据，因为这些页面需要被搜索引擎索引，而搜索引擎无法获取使用MVVM并通过API加载的数据。所以，需要SEO（Search Engine Optimization）的页面，不能使用MVVM展示数据。不需要SEO的页面，如果前端逻辑复杂，就适合使用MVVM展示数据，例如，工具类页面，复杂的表单页面，用户登录后才能操作的页面等等。