```
import logging  # 引入logging模块
# 将信息打印到控制台上
logging.debug(u"弥弥")
logging.info(u"砂糖")
logging.warning(u"亚瑟")
logging.error(u"岁岁")
logging.critical(u"泡芙")
#默认打印出warning，error和critical

```
#####级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG

```
logging.basicConfig(level=logging.NOTSET)  # 设置日志级别
logging.debug(u"如果设置了日志级别为NOTSET,那么这里可以采取debug、info的级别的内容也可以显示在控制台上了")
```
[python中logging日志模块详解](https://www.cnblogs.com/xianyulouie/p/11041777.html)