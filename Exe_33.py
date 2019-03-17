#coding=utf-8  //测试

'''
习题 33: While 循环
接下来是一个更在你意料之外的概念： while-loop``（while 循环）。``while-loop 会一直执行它下面的代码片段，直到它对应的布尔表达式为 False 时才会停下来。

等等，你还能跟得上这些术语吧？如果你的某一行是以 : （冒号, colon）结尾，那就意味着接下来的内容是一个新的代码片段，新的代码片段是需要被缩进的。只有将代码用这样的方式格式化，Python 才能知道你的目的。如果你不太明白这一点，就回去看看“if 语句”和“函数”的章节，直到你明白为止。

接下来的练习将训练你的大脑去阅读这些结构化的代码。这和我们将布尔表达式烧录到你的大脑中的过程有点类似。

回到 while 循环，它所作的和 if 语句类似，也是去检查一个布尔表达式的真假，不一样的是它下面的代码片段不是只被执行一次，而是执行完后再调回到 while 所在的位置，如此重复进行，直到 while 表达式为 False 为止。

While 循环有一个问题，那就是有时它会永不结束。如果你的目的是循环到宇宙毁灭为止，那这样也挺好的，不过其他的情况下你的循环总需要有一个结束点。

为了避免这样的问题，你需要遵循下面的规定：

尽量少用 while-loop，大部分时候 for-loop 是更好的选择。
重复检查你的 while 语句，确定你测试的布尔表达式最终会变成 False 。
如果不确定，就在 while-loop 的结尾打印出你要测试的值。看看它的变化。
在这节练习中，你将通过上面的三样事情学会 while-loop ：

'''

def print_array(index, step):
    numbers= []
    for i in range(0,index,step):
        print("At the top i is %d" %i)
        numbers.append(i)
        print("Number now:%r" % numbers)
        print("At the bottom is %d" %i)

    print("The numbres:")
    for num in numbers:
        print(num)

    print("Index %d, %d" %(2,numbers[1]))

print_array(6,2)
