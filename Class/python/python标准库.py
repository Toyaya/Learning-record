import os
import time

print(os.getcwd())   #目前所在文件夹
print(os.listdir("./")) #ls方法

if not os.path.exists("b"):
    os.mkdir("b")
if not os.path.exists("b/test.txt"):
    f = open("b/test.txt","w") #w:可写
    f.write("hello")
    f.close()


# time.asctime()国外的时间格式
# time.time()时间戳
# time.sleep()等待
# time.localtime()时间戳转为时间元组
# time.strftime() 当前的时间戳转成带格式的时间