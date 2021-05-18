[原文链接](https://mp.weixin.qq.com/s/jnD6SmORxnkVBromZEGzxg)

#####Activity是一个应用程序组件，提供一个屏幕，用户可以用来交互为了完成某项任务。在一个android应用中，一个Activity通常就是一个单独的屏幕，Activity上可显示控件，也可以监听并处理用户的事件并做出响应，下图是Android启动app时发生的事情：
![](https://mmbiz.qpic.cn/mmbiz_png/ervTCibwaujEicS5ibdrGfT8iaicGNPZ0UMSqvicH7kgmiaPW5riadbIzGv0rFwt3oby4xmtAfngZnMqZ1X4OsMEzt1pbg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
- 创建一个Linux进程，Linux进程创建Android虚拟机
- 进行application onCreate的加载
- 启动主线程：进行activity的初始化，activity onCreate用于加载自身逻辑及发送远程数据请求和渲染界面
- 加载动态页面

#####使用
######把各个环节拆分成冷启动，暖启动，热启动，首屏启动，含义如下：
- 冷启动：从进程创建开始到界面的展示
- 暖启动：相对于热启动要消耗更多资源。当用户退出应用程序时，进程还会存在。暖启动相较于冷启动只是少了进程的创建
- 热启动：应用之间的切换
- 首屏启动：第一次安装启动

```
adb logcat
```