#####mock使用场景
- 匹配规则
- 模拟数据

### mock 原理过程

![image|800x342, 50%](https://ceshiren.com/uploads/default/optimized/2X/2/2548609f7c223d81bb16005a21b10272cab39e8a_2_800x342.png)

### map local 原理

![image|800x414, 50%](https://ceshiren.com/uploads/default/optimized/2X/2/29020fbd205a44e3fda23a8737f31fa10e7cb438_2_800x414.png)


### map remote

![image|800x292](https://ceshiren.com/uploads/default/optimized/2X/1/10e5005e54a1a53afdec3e890b2cb2e714452a37_2_1600x584.png)


###  mitmproxy

`q`: 返回上一级
键盘↑⬇️:代表切换数据，回车可以查看 

flow 代表一条请求以及对应响应的接口信息

### mitmdump

`-s`:执行python脚本

```python
"""
Basic skeleton of a mitmproxy addon.

Run as follows: mitmproxy -s anatomy.py
"""
from mitmproxy import ctx


class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow):
        self.num = self.num + 1
        ctx.log.info("We've seen %d flows" % self.num)


addons = [
    Counter()
]
```

# --proxy 代表使用的代理
```
curl -X GET "https://httpbin.testing-studio.com/get" -H "accept: application/json" --proxy http://127.0.0.1:8080
```

#####事件
- 有严格的方法命名规定
- 每一个不同的事件，代表网络请求过程中的不同的阶段
- 每个时间方法，都必须有flow 参数。可以通过控制flow 参数，去做mock

#####MITMDUMP DEBUG
```
if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump
    #使用debug模式启动mitmdump
    mitmdump(['-p', '8080', '-s', __file__])
```