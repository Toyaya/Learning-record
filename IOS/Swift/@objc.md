## @objc:
###### 一般的方法前面是不需要写@objc的，但selector对应的方法前面必须加，因为selector其实是 Objective-C runtime 的概念。在 Swift4 中，默认情况下所有的 Swift 方法在Objective-C 中都是不可见的，所以你需要在这类方法前面加上@objc关键字，将这个方法暴露给 Objective-C，才能进行使用。