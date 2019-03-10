#coding=utf-8  //测试

'''
习题 12: 提示别人

当你键入 raw_input() 的时候，你需要键入 ( 和 ) 也就是“括号(parenthesis)”。这和你格式化输出两个以上变量时的情况有点类似，比如说 "%s %s" % (x, y) 里边就有括号。对于 raw_input 而言，你还可以让它显示出一个提示，从而告诉别人应该输入什么东西。你可以在 () 之间放入一个你想要作为提示的字符串，如下所示：

y = raw_input("Name? ")

这句话会用 “Name?” 提示用户，然后将用户输入的结果赋值给变量 y。这就是我们提问用户并且得到答案的方式。

也就是说，我们的上一个练习可以使用 raw_input 重写一次。所有的提示都可以通过
raw_input 实现。
'''
age = raw_input("How old are you?");
height = raw_input("How tall are you?");
weight = raw_input("How much do you weigh?")
#由于不确定输入变量的类型，输出用%r
print"So, you're %r old,%r tall and %r heavy."%(age,height,weight)
