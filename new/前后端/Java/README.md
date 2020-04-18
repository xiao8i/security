# Java是基于JVM虚拟机的跨平台语言，一次编写，到处运行。面向对象
Java介于编译型语言和解释型语言之间。编译型语言如C、C++，代码是直接编译成机器码执行，但是不同的平台（x86、ARM等）CPU的指令集不同，因此，需要编译出每一种平台的对应机器码。解释型语言如Python、Ruby没有这个问题，可以由解释器直接加载源码然后运行，代价是运行效率太低。而Java是将代码编译成一种“字节码”，它类似于抽象的CPU指令，然后，针对不同平台编写虚拟机，不同平台的虚拟机负责加载字节码并执行，这样就实现了“一次编写，到处运行”的效果。
Java规定，某个类定义的public static void main(String[] args)是Java程序的固定入口方法，因此，Java程序总是从main方法开始执行。
一个Java源码只能定义一个public类型的class，并且class名称和文件名要完全一致；
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello, world!");
    }
}
使用javac可以将.java源码编译成.class字节码；
使用java可以运行一个已编译的Java程序，参数是类名。
使用Eclipse作为IDE，Eclipse IDE提供了快捷键Ctrl+Shift+F帮助我们快速格式化代码的功能，
注意char类型使用单引号'，且仅有一个字符，要和双引号"的String类型区分开。
使用var定义变量，仅仅是少写了变量类型而已
字符串的不可变是指字符串内容不可变，赋新值会重新引用。
new操作符可以创建一个实例Person ming = new Person();
可变参数 public void setNames(String... names) 可以不用定义数组直接传入，还可以保证无法传入null，因为传入0个参数时，接收到的实际值是一个空数组而不是null
Java使用extends关键字来实现继承：
class Student extends Person {
    protected int score;

    public Student(String name, int age, int score) {
        super(); // 自动调用父类的构造方法
        this.score = score;
    }
}中间是类的构造方法
把一个方法声明为abstract，表示它是一个抽象方法，本身没有实现任何方法语句。因为这个抽象方法本身是无法执行的，所以，抽象类也无法被实例化，类本身也声明为abstract，才能正确编译它。因为抽象类本身被设计成只能用于被继承，因此，抽象类可以强迫子类实现其定义的抽象方法，否则编译会报错。
当我们定义了抽象类Person，以及具体的Student、Teacher子类的时候，我们可以通过抽象类Person类型去引用具体的子类的实例：
Person s = new Student();
Person t = new Teacher();具体的业务逻辑由不同的子类实现，调用者并不关心。
在抽象类中，抽象方法本质上是定义接口规范：即规定高层类的接口，从而保证所有子类都有相同的接口实现，这样，多态就能发挥出威力。
如果一个抽象类没有字段，所有方法全部都是抽象方法：就可以把该抽象类改写为接口：interface在Java中，一个类只能继承自另一个类，不能从多个类继承。但是，一个类可以实现多个interface，例如：class Student implements Person, Hello{}
abstract class Person {
    public abstract void run();
    public abstract String getName();
}可以改为接口interface
static静态字段和静态方法类比于类属性和类方法。
包：
package mr.jun; // 申明包名mr.jun

public class Arrays {
}//完整类名是mr.jun.Arrays；
默认自动import java.lang.*
最佳实践如果不确定是否需要public，就不声明为public，即尽可能少地暴露对外的字段和方法。
把方法定义为package权限有助于测试，因为测试类和被测试类只要位于同一个package，测试代码就可以访问被测试类的package权限方法。
一个.java文件只能包含一个public类，但可以包含多个非public类。如果有public类，文件名必须和public类的名字相同。
小结
Java内建的访问权限包括public、protected、private和package权限；
Java在方法内部定义的变量是局部变量，局部变量的作用域从变量声明开始，到一个块结束；
final修饰符不是访问权限，它可以修饰class、field和method；
一个.java文件只能包含一个public类，但可以包含多个非public类。
JVM通过环境变量classpath决定搜索class的路径和顺序.建议始终通过-cp命令传入
String.valueOf(123);静态方法转换为字符串
String和char[]类型可以互相转换，方法是：
char[] cs = "Hello".toCharArray(); // String -> char[]
String s = new String(new char[] {'H', 'e', 'l', 'l', 'o', '!'}); // char[] -> String
我们把能创建“新”对象的静态方法称为静态工厂方法。
SecureRandom：生成安全的随机数
通过Class实例获取class信息的方法称为反射（Reflection）。Class cls = String.class; 通过一个class的静态变量class获取/String s = "Hello"; Class cls = s.getClass();通过该实例变量提供的getClass()方法获取： /Class cls = Class.forName("java.lang.String");通过一个class的完整类名
@注解；注释会被编译器直接忽略，注解则可以被编译器打包进入class文件，因此，注解是一种用作标注的“元数据”。
Java的泛型是采用擦拭法实现的；擦拭法决定了泛型<T>：在编译过程中实际为object
java.util包主要提供了以下三种类型的集合：区别于array数组初始化后大小不可变；数组只能按索引顺序存取。
List：一种有序列表的集合，ArrayList和LinkedList两种实现；
Set：一种保证没有重复元素的集合，例如，所有无重复名称的Student的Set；
Map：一种通过键值（key-value）查找的映射表集合，最常用的实现类是HashMap。
通过一个“基础”组件再叠加各种“附加”功能组件的模式，称之为Filter模式（或者装饰器模式：Decorator）。它可以让我们通过少量的类来实现各种功能的组合：
在classpath中的资源文件，路径总是以／开头
序列化是指把一个Java对象变成二进制内容，本质上就是一个byte[]数组。Java的序列化机制仅适用于Java，如果需要与其它语言交换数据，必须使用通用的序列化方法，例如JSON
Java平台最常用的测试框架JUnit单元测试，断言方法测试。
URL编码如果字符是A~Z，a~z，0~9以及-、_、.、*，则保持不变；如果是其他字符，先转换为UTF-8编码，然后对每个字节以%XX表示。URLEncoder把空格字符编码成+，而现在的URL编码标准要求空格被编码为%20
Base64编码的目的是把二进制数据变成文本格式，这样在很多文本中就可以处理二进制数据。Base64编码的缺点是传输效率会降低，因为它把原始数据的长度增加了1/3。
URL编码和Base64编码都是编码算法，它们不是加密算法；URL编码的目的是把任意文本数据编码为%前缀表示的文本，便于浏览器和服务器处理；Base64编码的目的是把任意二进制数据编码为文本，但编码后数据量会增加1/3。
DH(Diffie-Hellman)算法是一种密钥交换协议，通信双方通过不安全的信道协商密钥，然后进行对称加密传输。DH算法没有解决中间人攻击。
非对称加密的缺点就是运算速度非常慢，比对称加密要慢很多。此外，只使用非对称加密算法不能防止中间人攻击。
Java线程的状态有以下几种：
New：新创建的线程，尚未执行；
Runnable：运行中的线程，正在执行run()方法的Java代码；
Blocked：运行中的线程，因为某些操作被阻塞而挂起；
Waiting：运行中的线程，因为某些操作在等待中；
Timed Waiting：运行中的线程，因为执行sleep()方法正在计时等待；
Terminated：线程已终止，因为run()方法执行完毕。
当main线程对线程对象t调用join()方法时，主线程将等待变量t表示的线程运行结束，即join就是指等待该线程结束，然后才继续往下执行自身线程。
volatile关键字的目的是告诉虚拟机：每次访问线程间共享变量时，总是获取主内存的最新值；每次修改线程间共享变量后，立刻回写到主内存。volatile保证时效性不是原子性
在JVM中，所有非守护线程都执行完毕后，无论有没有守护线程（Daemon Thread），虚拟机都会自动退出。
使用synchronized加锁解决了多线程同步访问共享变量的正确性问题。
这种在一个线程中，横跨若干方法调用，需要传递的对象，我们通常称之为上下文（Context），它是一种状态，可以是用户身份、任务信息等。ThreadLocal，它可以在一个线程中传递同一个对象
计算机网络：由两台或更多计算机组成的网络；
互联网：连接网络的网络；
IP地址：计算机的网络接口（通常是网卡）在网络中的唯一标识；
网关：负责连接多个网络，并在多个网络之间转发数据的计算机，通常是路由器或交换机；
网络协议：互联网使用TCP/IP协议，它泛指互联网协议簇；
IP协议：一种分组交换传输协议；
TCP协议：一种面向连接，可靠传输的协议；
UDP协议：一种无连接，不可靠传输的协议。
Socket、TCP和部分IP的功能都是由操作系统提供的，不同的编程语言只是提供了对操作系统调用的简单的封装。例如，Java提供的几个Socket相关的类就封装了操作系统提供的接口。
发送邮件协议SMTP，接收邮件使用最广泛的协议是POP3(Post Office Protocol version 3)，另一种接收邮件的协议是IMAP：Internet Mail Access Protocol
1xx：表示一个提示性响应，例如101表示将切换协议，常见于WebSocket连接；
2xx：表示一个成功的响应，例如200表示成功，206表示只发送了部分内容；
3xx：表示一个重定向的响应，例如301表示永久重定向，303表示客户端应该按指定路径重新发送请求；
4xx：表示一个因为客户端问题导致的错误响应，例如400表示因为Content-Type等各种原因导致的无效请求，404表示指定的路径不存在；
5xx：表示一个因为服务器问题导致的错误响应，例如500表示服务器内部故障，503表示服务器暂时无法响应。
最早期的HTTP/1.0协议，每次发送一个HTTP请求，客户端都需要先创建一个新的TCP连接，然后，收到服务器响应后，关闭这个TCP连接。由于建立TCP连接就比较耗时，因此，为了提高效率，HTTP/1.1协议允许在一个TCP连接中反复发送-响应，这样就能大大提高效率：HTTP/2.0允许客户端在没有收到响应的时候，发送多个HTTP请求，服务器返回响应的时候，不一定按顺序返回，只要双方能识别出哪个响应对应哪个请求，就可以做到并行发送和接收：
Java的RMI远程调用是指，一个JVM中的代码可以通过网络实现远程调用另一个JVM的某个方法。RMI是Remote Method Invocation的缩写。
Java的RMI严重依赖序列化和反序列化，而这种情况下可能会造成严重的安全漏洞，因为Java的序列化和反序列化不但涉及到数据，还涉及到二进制的字节码，即使使用白名单机制也很难保证100%排除恶意构造的字节码。因此，使用RMI时，双方必须是内网互相信任的机器，不要把1099端口暴露在公网上作为对外服务。
XML是可扩展标记语言（eXtensible Markup Language）的缩写，它是是一种数据表示格式，可以描述非常复杂的数据结构，常用于传输和存储数据。
JSON是JavaScript Object Notation的缩写，它去除了所有JavaScript执行代码，只保留JavaScript的对象格式。XML的特点是功能全面，但标签繁琐，格式复杂。在Web上使用XML现在越来越少，取而代之的是JSON这种数据结构。