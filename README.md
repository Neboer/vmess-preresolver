# vmess dns pre-resolver

通过pythondns模块和指定的dns server，批量解析订阅链接里的域名并解析为本地的ip。

# 作用
如果您的机场无法连接，不妨检查一下它的域名是否被污染。如果它的域名遭到了污染，你的v2ray core就无法连接它了。

这个时候，不妨试一下修改链接的地址域名为他们的真实ip，这个时候你可能就发现可以正常连接了。

# 说明
不是很清楚V2ray对域名是怎么处理的，如果走系统解析的话，这可能会导致你的每个代理过去的proxy都会
有一个解析代理服务器域名的过程，如果域名解析速度有些缓慢，或本地使用了相对缓慢的dns（比如doh和dot等等）时可能会极大地降低网络速度和延迟，此时，优先解析域名为ip的作用就体现了出来。

正常的tls连接是需要域名这一关键信息的。因为没有ca会给一个没有域名的服务器颁发证书。但v2ray的tls handshake过程
应该是带有混淆的，因此正常情况下把域名改成ip地址理论上不会产生问题。

# 使用
下载你的订阅连接的全部响应到本地磁盘，保存为一个文件。然后调用python main.py xxx，订阅信息会自动被decode，
程序会取出里面所有的add为域名的记录，然后多线程解析域名，并覆盖原来的add字段。程序不会修改任何其他的参数。

# 有效性
当你的节点被dns污染的时候，直接写hosts会来的更加迅速一些，所以这个程序并没有什么卵用。但是对于安卓手机等不方便修改hosts的设备，我认为它是一个不错的选择

# 协议
本项目遵守MIT开源协议，希望大家能协助开发。
