# 跨站请求伪造，利用网站对浏览器的信任（cookie），当用户浏览恶意代码（例如<img src=http://）就可能跳转到曾经登陆过的网站（浏览器保存有网站set-cookie）并进行用户操作，攻击方法不需要知道用户信息。越方便越危险……注意CSRF恶意链接容易出现在恶意网站上。
防御：用户不要在危险的页面打开重要的新页面，网站可以检查http的referer字段判断跨站请求，在请求地址中添加 token 并验证，在 HTTP 头中自定义属性并验证（比如token，关键在于在请求中放入私密信息，并且该信息不存在于 cookie 之中，这样的话CSRF请求就会缺少字段而不成功）。还有关键操作要加入验证码机制，以及Chrome浏览器端启用SameSite cookie
https://blog.csdn.net/xiaoxinshuaiga/article/details/80766369
CSRF一般使用form表单提交请求，而浏览器是不会对form表单进行同源拦截的，因为这是无响应的请求，浏览器认为无响应请求是安全的。
CSRF危害更多是针对可以进行业务动作（增删改）的页面，通过伪造请求欺骗站点进行业务办理。对于查询页面存在CSRF漏洞，由于浏览器跨域限制，即使请求返回数据，B.com的页面是无法对数据进行分析或处理，因此查询页面的CSRF危害会小很多，或者没有危害。否则涉及跨域策略
 <img src=http://www.bank.example/withdraw?account=daguanren1&amount=888&for=jinlian width='0' height='0'>


<iframe style="display:none" name="csrf-frame"></iframe>
<form method='POST' action='http://www.bank.example/withdraw' target="csrf-frame" id="csrf-form">
  <input type='hidden' name='account' value='daguanren1'>
  <input type='hidden' name='amount' value='888'>
  <input type='hidden' name='for' value='jinlian'>
  <input type='submit' value='submit'>
</form>
<script>document.getElementById("csrf-form").submit()</script>

双重Cookie验证，参考：https://juejin.im/post/5bc009996fb9a05d0a055192#heading-18 简单来说除了cookie中的CSRF-Token外，请求体(POST)或者请求参数(GET)中也要有一个CSRF-Token。后端比较Cookie和请求体(POST)或者请求参数(GET)中的CSRF-Token是否一致，一致才执行请求。 因为CSRF攻击实际上是获取不到Cookie(CSRF一般通过钓鱼网站进行，而第三方网站是获取不到Cookie)的，而请求体(POST)或者请求参数(GET)中的CSRF-TOKEN需要中cookie中提取,这样就保证只有自己网站的页面能够在请求体或请求参数中设置CSRF-TOKEN。这样就完成了CSRF的防御。 
以上方法就是通过url验证cookie内容，由于CSRF无法获取cookie所以url不能带上cookie参数。放在hideen标签里验证更安全？也可以放在头部