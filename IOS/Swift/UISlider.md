```
//滑块的创建
let slider=UISlider(frame:CGRectMake(0,0,300,50))
slider.center=self.view.center
slider.minimumValue=0  //最小值
slider.maximumValue=1  //最大值
slider.value=0.5  //当前默认值
self.view.addSubview(slider)

//设置滑块的值，同时有动画
slider.setValue(0.8,animated:true)

//滑块值改变响应
slider.continuous=false  //滑块滑动停止后才触发ValueChanged事件
slider.addTarget(self,action:"sliderDidchange:", forControlEvents:UIControlEvents.ValueChanged)
 
func sliderDidchange(slider:UISlider){
    print(slider.value)
}

//滑块左右两边槽的颜色
slider.minimumTrackTintColor=UIColor.redColor()  //左边槽的颜色
slider.maximumTrackTintColor=UIColor.greenColor() //右边槽的颜色

//滑块后面槽线两侧添加图标
slider.minimumValueImage=UIImage(named:"voice+")  //左边图标
slider.maximumValueImage=UIImage(named:"voice-")  //右边图标
```