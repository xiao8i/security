# 为了保存类或实例中的数据以下次使用，并节约系统资源，可以把对象序列化保存serialize()成字符串，再进行反序列化恢复并使用unserialize().https://chybeta.github.io/2017/06/17/%E6%B5%85%E8%B0%88php%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96%E6%BC%8F%E6%B4%9E/
虽然序列化后的对象不包含方法，更无法调用对象的方法，但是当对象涉及到魔法方法时，就有可能自动调用，例如
__construct()当一个对象创建时被调用

__destruct()当一个对象销毁时被调用

__toString()当一个对象被当作一个字符串使用

__sleep() 在对象在被序列化之前运行

__wakeup将在序列化之后立即被调用
此时修改对象的数据，就有可能执行对应的功能。
审计http://www.freebuf.com/column/161798.html

http://p0sec.net/index.php/archives/114/

https://www.anquanke.com/post/id/84922
防御：唯一安全的架构模式是不接受来自不受信源的序列化对象，或使用只允许原始数据类型的序列化媒体。