```
/**
 按钮添加点击事件
 UIControlEvents
 常用的触摸事件类型：
 touchDown：单点触摸按下事件，点触屏幕
 touchDownRepeat：多点触摸按下事件，点触计数大于1，按下第2、3或第4根手指的时候
 touchDragInside：触摸在控件内拖动时
 touchDragOutside：触摸在控件外拖动时
 touchDragEnter：触摸从控件之外拖动到内部时
 touchDragExit：触摸从控件内部拖动到外部时
 touchUpInside：在控件之内触摸并抬起事件
 touchUpOutside：在控件之外触摸抬起事件
 touchCancel：触摸取消事件，即一次触摸因为放上太多手指而被取消，或者电话打断
 */

 /**
 按钮文字显示的类型
 NSLineBreakMode
 byTruncatingHead：省略头部文字，省略部分用...代替
 byTruncatingMiddle：省略中间部分文字，省略部分用...代替（默认）
 byTruncatingTail：省略尾部文字，省略部分用...代替
 byClipping：直接将多余的部分截断
 byWordWrapping：自动换行（按词拆分）
 注意：当设置自动换行后（byWordWrapping 或 byCharWrapping），我们可以在设置 title 时通过 \n 进行手动换行。
 */
 NetWorkBtn.titleLabel?.lineBreakMode = NSLineBreakMode.byClipping
```