
####异常捕捉与异常处理：
try:执行代码
except:发生异常时执行的代码
else:没有异常时执行的代码
finally:不管有没有异常都会执行

####使用raise抛出异常：
```
def set_age(num):
   if num <= 0 or num > 200 :
       raise ValueError(f"值错误:{num}")

```