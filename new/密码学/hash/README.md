# hash映射为定长的数据，可以做为摘要也可以作为索引https://www.liaoxuefeng.com/wiki/1022910821149312/1023025778520640
摘要hash：
base64，MD5可以被破解(MD5因为输出长度较短，短时间内破解是可能的，目前已经不推荐使用)，较安全的为SHA256
MAC(HMAC)：带秘密密钥的Hash函数。由于密钥参与散列值的运算，所以更安全。注意MAC可以认证，也可以校验，但是无法防抵赖（防抵赖还是需要私钥进行签名）
RSA（非对称加密一种）加密的原始信息必须小于Key的长度，非对称加密算法还有ECC椭圆曲线密码学（Elliptic curve cryptography)和DSA(Digital Signature Algorithm基于离散对数)
对称加密算法有：
高级加密标准（Advanced Encryption Standard，AES） DES全称为Data Encryption Standard，即数据加密标准   国际数据加密算法（IDEA，International Data Encryption Algorithm）
算法	密钥长度	工作模式	填充模式
DES	56/64	ECB/CBC/PCBC/CTR/...	NoPadding/PKCS5Padding/...
AES	128/192/256	ECB/CBC/PCBC/CTR/...	NoPadding/PKCS5Padding/PKCS7Padding/...
IDEA	128	ECB	PKCS5Padding/PKCS7Padding/...
DES算法由于密钥过短，可以在短时间内被暴力破解，所以现在已经不安全了。CBC模式的全称是Cipher Block Chaining模式（密文分组链接模式），ECB（Electronic Codebook，电码本）模式
AES算法是目前应用最广泛的加密算法，ECB模式是最简单的AES加密模式，它只需要一个固定长度的密钥，固定的明文会生成固定的密文，这种一对一的加密方式会导致安全性降低，更好的方式是通过CBC模式，它需要一个随机数作为IV参数，这样对于同一份明文，每次生成的密文都不同：
RC4（来自Rivest Cipher 4的缩写）是一种流加密算法，密钥长度可变。它加解密使用相同的密钥，因此也属于对称加密算法。
RC5分组密码算法，也属于对称加密算法。

PBE就是Password Based Encryption口令加密算法
密钥交换算法即DH算法：Diffie-Hellman算法
RSA：基于大数分解（1024位目前是安全的），大数为两个大质数(素数)P、Q之积。
即公共模数N=p*Q
欧拉函数(在1到N之中，有多少个数与N构成互质关系[互质关系：只有公因数1])φ(N) =φ(P)*φ(Q)= (P-1)(Q-1) --前面由欧拉函数给出，后面质数PQ的欧拉函数自然是-1
