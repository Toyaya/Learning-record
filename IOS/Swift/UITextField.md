```
//设置输入框的样式
/**
 bezel : 是矩形的浅黑线框样式
 line  : 是矩形的黑线框样式
 roundedRect ： 四个圆角的浅灰色矩形框
 none:   系统默认（全白色）
 */
 NetWorkTextField.borderStyle = .roundedRect
NetWorkTextField.borderStyle = UITextBorderStyle.roundedRect


//显示提示文字
NetWorkTextField.placeholder = "文本提示框"


//文本框的键盘为暗色主题
NetWorkTextField.keyboardAppearance = UIKeyboardAppearance.dark


//设置清除按钮
/**
 设置全部清除按钮
 always :输入框内有输入的情况下，还会一直显示
 whileEditing : 当输入框处于编辑的情况下会显示清除按钮，当输入框不在编辑的情况下，清除按钮就会消失。
 never : 就是一直都不显示全部清除按钮
 unlessEditing : 输入框在编辑的时候不出现清除按钮，当输入框结束编辑的时候，清除按钮就会出现
 */
NetWorkTextField.clearButtonMode = UITextFieldViewMode.unlessEditing


//输入框文字显示明文还是暗文
/**
 控制输入的内容是以明文显示还是暗纹显示
 isSecureTextEntry 
 true : 是暗纹显示
 false : 明文显示（默认）
 */
NetWorkTextField.isSecureTextEntry = true



 //设置输入文字的大小
NetWorkTextField.font = UIFont.systemFont(ofSize: 16)



 //设置输入文字在输入框显示位置
 /**NSTextAlignment
 left : 显示的文字靠近输入框的左边显示（系统默认）
 right: 显示的文字靠近输入框的右边显示
 center :显示文字在输入框的中间
 */
NetWorkTextField.textAlignment = NSTextAlignment.center
```