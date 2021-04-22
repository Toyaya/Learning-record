
## Appium的简介

#### appium的引擎
- Android是uiautomator2
- ios是xcuitest

#### appium的设计理念
- webdriver是基于http协议的，第一连接会建立一个session会话，并通过post发送一个json告知服务端相关测试信息
- client/server设计模式
  - 客户端通过webdriver json wire协议与服务器通讯
  - 多语言支持
- server可以放在任何地方
- 服务器nodejs开发的http服务
- appium使用appium-xcuitest-driver来测试iphone设备，其中需要安装Facebook出的WDA(webdriver agent)来驱动ios测试

#### appium的生态工具
- adb：Android控制工具
- appium Destkop：内嵌appium server和inspector的综合工具
- appium server：appium的核心工具，命令行工具
- appium client：各种语言的客户端封装库，用户连接appium server，包含python、java、ruby等
- appcrawler自动遍历工具


#### 获取app的信息
- 获取当前元素界面：adb shell dumpsys activity top
- 获取任务列表：adb shell dumpsys activity activities
- 获取app的package和activity：adb shell；然后logcat | grep -i displayed
- 启动应用:adb shell am start -W -n "com.xueqiu.android/.view.WelcomeActivityAlias -S


#### Capability设置
- 文档地址：http://appium.io/docs/en/writing-running-appium/caps/index.html
-platformName:android 通常都是写android
- deviceName:127.0.0.1:7555 这个通常是adb devices的名称
- appPackage:com.xueqiu.android 这个是app的package包名
- appActivity:.view.WelcomeActivityAlias 这个是app的activity名
- noReset：true, false 是否重置测试的环境（例如首次打开弹框，或者登陆信息）
- unicodeKeyboard：true, false 是否需要输入非英文之外的语言并在测试完成后重置输入法，比如输入中文
- dontStopAppOnReset：true, false 首次启动的时候，不停止app
- skipDeviceInitialization：true, false 跳过安装，权限设置等操作


#### 测试用的apk
- https://github.com/appium/appium/tree/master/sample-code/apps

<br>

<br>

## Android的基础知识

#### Android的布局
- Android是通过容器的布局属性来管理子控件的位置关系，布局过程就是把界面上的所有的控件，根据他们的间距的大小，摆放在正确的位置
- 线性布局：LinearLayout
- 相对布局：RelativeLayout
- 帧布局：FrameLayout
- 绝对布局：AbsoluteLayout
- 表格布局：TableLayout
- 网格布局：GirdLayout
- 约束布局：ConstraintLayout


#### Android四大组件
- activity：与用户交互的可视化界面
- service：实现程序后台运行的解决方案，比如qq音乐的音乐在后台运行，没有界面
- content provide： 内容提供者，提供程序所需要的数据，比如？提供数据库？
- broadcast receiver：广播接收器，监听外部事件的到来（比如来电）

#### Android常用的控件：
- TextView：文本控件
- EditText：可编辑文本控件
- Button：按钮
- ImageButton：图标按钮
- ToggleButton:开关按钮
- ImageView：图片控件
- CheckBox：复选框控件
- RadioButton：单选框控件


#### 控件知识
- dom：Document Object Model 文档对象模型
- dom应用：最早应用于html和js的交互，用户表示界的控件层级，界面的结构化描述，常见的格式为html、xml。核心元素为节点和属性
- xpath：xml路径语言，用于xml中的节点定位
- Android的应用层级结构是定制的xml
- app source类似于dom，表示app的层级，表示界面里面所有的控件数的结构
- 每个控件都有它的属性（resourceid、xpath、aid），没有css属性