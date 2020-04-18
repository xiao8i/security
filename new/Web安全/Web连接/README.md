# 一般通过url方式打开Web连接，基于HTTP/HTTPS，工具有urllib、request等.session存储在服务器端实现跨脚本共享文件(序列化的，可以修改)，cookie存储在客户端实现跨脚本共享临时数据（请求会带有cookie数据，数据很少）。
HTTP连接无状态，不知道以前干过什么，也不会知道是谁，所以可以用用户名/密码方式，但是如果每次发出请求都需要填入用户名/密码很麻烦，浏览器自动填写大大简化（cookie），但是这样的话cookie被盗=用户名/密码被盗，很危险，所以第一次登陆后，服务端给出生成的cookie用于认证用户，保护了用户名/密码：
cookie：服务器维护cookie信息对应的数据库，数据库记录用户各种信息，甚至操作，所以是很有用的。服务端通过set-cookie生成cookie信息响应给浏览器(注意服务器并不保存cookie，但是cookie会对应数据库信息)
session：保存在cookie中在关闭浏览器后删除，更安全，session保存关键信息，服务器生成并在内存维护session（注定了服务器不能长时间保存），并通过session生成sessionid响应给浏览器，浏览器关闭后（注意页面关闭不行并不会关闭会话）清除自身的sessionid(但是服务端的session不清除，看服务器的设定一般无交互20分钟清除)，一定程度保证了认证在客户端的安全（cookie可以在客户端长时间保存有风险）
token：解决了服务器内存维护session的开销，以及分布式存储session的问题，token其实就是session的升级版，服务端把userid进行签名形成token（令牌）响应给客户端，以后服务端只需要验证userid的签名即可认证userid即用户。注意token在客户端保存，所以服务器会对token设一个较短的时效。
当然无法保证cookie、session和token被窃取，无论是在客户端、服务端还是中间过程。
注意请求时浏览器会自动带上cookie，此时会自动带上sessionid；但是把sessionid像token那样另写入heder更加安全（防csrf），只使用cookie的好处就是以后登录不用输入用户名and密码
注意cookie是一定会有的，因为http是无状态的协议(直接建立在TCP层上，没有过会话层session)，为了实现记录用户(实现交互)，所以浏览器可以自动保存且提交cookie。（header头部的cookie字段）
但是我们用用户名区分用户，cookie会泄露用户真实信息，所以cookie往往需要hash处理，并且用cookie登录不安全(毕竟浏览器保存cookie信息)，所以服务端处理session并返回sessionid给客户端添加到cookie里，在不退出浏览器(会话有效期)内，用户凭sessionid使用账户(注意第一次打开网站是带有cookie登陆的，但是一定没有sessionid，用户登录后才会得到sessionid)
但是在浏览器使用期间还是可以用sessionid发起CSRF攻击(很难，服务端通过url方式完成用户的敏感请求是很蠢的，所以就算用sessionid发起CSRF通常无法造成很大危害，就相当于冒充客户发起了一次请求，但是聪明的服务器不会让请求就可以执行用户操作)，但是我们仍然可以避免这种攻击
办法是在header添加新的token字段，用户登录后服务端响应返回token值保存在body体中，以后用户请求则可以通过前端处理从body取出token放入header，这样的话不输入用户密码一次就无法获得token从而彻底封死CSRF；另一方面token可以附加服务器的签名，这样的话服务器就无须在内存中保存token信息而只需要验证签名即可，避免了session的额外内存开销问题。
Ajax添加Token到Header中的方法(需要前端处理，也需要后端处理CORS)
1.方法一：
$.ajax({
    type: "GET",
    url: "/access/logout/" + userCode,
    headers: {'Authorization': token}
});
2.方法二：
    $.ajax({
        type: "GET",
        url: "/access/logout/" + userCode,
        beforeSend: function(request) {
            request.setRequestHeader("Authorization", token);
        },
        success: function(result) {
        }
    });
