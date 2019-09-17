#####对于少量数据或app运行参数，可以使用UserDefaults来保存至文件
#####UserDefaults是IOS系统自动为app分配的存储空间，存储于文件中，不会随app退出或崩溃而消失
```
//以guiderShow为关键字，存入
        let defaults = UserDefaults.standard
        defaults.set(true, forKey: "guiderShow")

        //判断：UserDefaults中是否有"guiderShow"对应value，如有，则退了
        let defaults = UserDefaults.standard
        if defaults.bool(forKey: "guiderShow") {
            return
        }

```