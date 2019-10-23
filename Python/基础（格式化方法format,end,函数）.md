```
age = 20
name = 'Swaroop'

print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))

#输出
#Swaroop was 20 years old when he wrote this book
#Why is Swaroop playing with that python?


print('a', end='')
print('b', end=' ')
#通过 end 指定其应以空白/空格结尾
#输出
#ab
```
#### 默认参数
###### 只有那些位于参数列表末尾的参数才能被赋予默认参数值，意即在函数的参数列表中拥有默认参数值的参数不能位于没有默认参数值的参数之前。
###### 这是因为值是按参数所处的位置依次分配的。举例来说，def func(a, b=5) 是有效的，但 def func(a=5, b) 是无效的。

#### 关键字参数
###### 如果你有一些具有许多参数的函数，而你又希望只对其中的一些进行指定，那么你可以通过命名它们来给这些参数赋值——这就是关键字参数（Keyword Arguments）——我们使用命名（关键字）而非位置（一直以来我们所使用的方式）来指定函数中的参数。
###### 这样做有两大优点——其一，我们不再需要考虑参数的顺序，函数的使用将更加容易。其二，我们可以只对那些我们希望赋予的参数以赋值，只要其它的参数都具有默认参数值。

#### 可变参数
###### 有时你可能想定义的函数里面能够有任意数量的变量，也就是参数数量是可变的，这可以通过使用星号来实现
```
def total(a=5, *numbers, **phonebook):
    print('a', a)

    #遍历元组中的所有项目
    for single_item in numbers:
        print('single_item', single_item)

    #遍历字典中的所有项目
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)

print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))
#当我们声明一个诸如 *param 的星号参数时，从此处开始直到结束的所有位置参数（Positional Arguments）都将被收集并汇集成一个称为“param”的元组（Tuple）
#类似地，当我们声明一个诸如 **param 的双星号参数时，从此处开始直至结束的所有关键字参数都将被收集并汇集成一个名为 param 的字典（Dictionary）
```

#### DocStrings文档字符串
```
def print_max(x, y):
    '''打印两个数值中的最大数。

    这两个数都应该是整数'''
    # 如果可能，将其转换至整数类型
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print_max(3, 5)
print(print_max.__doc__)

#函数的第一行逻辑行中的字符串是该函数的 文档字符串（DocString）
#它所做的便是获取函数的 __doc__ 属性并以一种整洁的方式将其呈现给你
```