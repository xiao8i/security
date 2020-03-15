# 跨站请求伪造，利用网站对浏览器的信任（cookie），当用户浏览恶意代码（例如<img src=http://）就可能跳转到曾经登陆过的网站（浏览器保存有网站set-cookie）并进行用户操作，攻击方法不需要知道用户信息。
防御：用户不要在危险的页面打开重要的新页面，网站可以检查http的referer字段判断跨站请求，也可以添加校验token确保是用户操作。
https://blog.csdn.net/xiaoxinshuaiga/article/details/80766369