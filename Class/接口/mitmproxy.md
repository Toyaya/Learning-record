[原文链接](https://www.cnblogs.com/grandlulu/p/9525417.html)

![mitmproxy 是什么](https://img2018.cnblogs.com/blog/1420378/201809/1420378-20180926173817431-1438106427.png)

######顾名思义，mitmproxy 就是用于 MITM 的 proxy，MITM 即中间人攻击（Man-in-the-middle attack）。用于中间人攻击的代理首先会向正常的代理一样转发请求，保障服务端与客户端的通信，其次，会适时的查、记录其截获的数据，或篡改数据，引发服务端或客户端特定的行为。

#####事件
- 针对 HTTP 生命周期
```
def http_connect(self, flow: mitmproxy.http.HTTPFlow):
#(Called when) 收到了来自客户端的 HTTP CONNECT 请求。在 flow 上设置非 2xx 响应将返回该响应并断开连接。CONNECT 不是常用的 HTTP 请求方法，目的是与服务器建立代理连接，仅是 client 与 proxy 的之间的交流，所以 CONNECT 请求不会触发 request、response 等其他常规的 HTTP 事件。
```

```
def requestheaders(self, flow: mitmproxy.http.HTTPFlow):
#(Called when) 来自客户端的 HTTP 请求的头部被成功读取。此时 flow 中的 request 的 body 是空的。
```

```
def request(self, flow: mitmproxy.http.HTTPFlow):
#(Called when) 来自客户端的 HTTP 请求被成功完整读取。
```

```
def responseheaders(self, flow: mitmproxy.http.HTTPFlow):
#(Called when) 来自服务端的 HTTP 响应的头部被成功读取。此时 flow 中的 response 的 body 是空的。
```

```
def response(self, flow: mitmproxy.http.HTTPFlow):
#(Called when) 来自服务端端的 HTTP 响应被成功完整读取。
```

```
def error(self, flow: mitmproxy.http.HTTPFlow):
#(Called when) 发生了一个 HTTP 错误。比如无效的服务端响应、连接断开等。注意与“有效的 HTTP 错误返回”不是一回事，后者是一个正确的服务端响应，只是 HTTP code 表示错误而已。
```

- 获取地址：flow.request.host
- 请求地址的路径是以s开头：flow.request.path.startswith("/s")
- 获取请求参数：flow.request.query.keys()
- 替换请求参数：flow.request.query.set_all
- 返回一个非 404 响应断开连接：flow.response = http.HTTPResponse.make(404)

```
import mitmproxy.http
from mitmproxy import ctx, http


class Joker:
    def request(self, flow: mitmproxy.http.HTTPFlow):
        if flow.request.host != "www.baidu.com" or not flow.request.path.startswith("/s"):
            return

        if "wd" not in flow.request.query.keys():
            ctx.log.warn("can not get search word from %s" % flow.request.pretty_url)
            return

        ctx.log.info("catch search word: %s" % flow.request.query.get("wd"))
        flow.request.query.set_all("wd", ["360搜索"])

    def response(self, flow: mitmproxy.http.HTTPFlow):
        if flow.request.host != "www.so.com":
            return

        text = flow.response.get_text()
        text = text.replace("搜索", "请使用谷歌")
        flow.response.set_text(text)

    def http_connect(self, flow: mitmproxy.http.HTTPFlow):
        if flow.request.host == "www.google.com":
            flow.response = http.HTTPResponse.make(404)
```