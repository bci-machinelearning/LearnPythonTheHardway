#coding=utf-8  //测试

'''
习题 32: 循环和列表
现在你应该有能力写更有趣的程序出来了。如果你能一直跟得上，你应该已经看出将“if 语句”和“布尔表达式”结合起来可以让程序作出一些智能化的事情。

然而，我们的程序还需要能很快地完成重复的事情。
这节习题中我们将使用 for-loop （for 循环）来创建和打印出各种各样的列表。
在做的过程中，你会逐渐明白它们是怎么回事。现在我不会告诉你，你需要自己找到答案。

在你开始使用 for 循环之前，你需要在某个位置存放循环的结果。
最好的方法是使用列表(list)，顾名思义，它就是一个按顺序存放东西的容器。
列表并不复杂，你只是要学习一点新的语法。首先我们看看如何创建列表：

hairs = ['brown', 'blond', 'red']
eyes = ['brown', 'blue', 'green']
weights = [1, 2, 3, 4]

你要做的是以 [ （左方括号）开头“打开”列表，然后写下你要放入列表的东西，用逗号隔开，就跟函数的参数一样，最后你需要用 ] （右方括号）结束右方括号的定义。
然后 Python 接收这个列表以及里边所有的内容，将其赋给一个变量。

'''

the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print("This is count %d" %number)

for fruit in fruits:
    print("A fruit of type: %s" %fruit)

for i in change:
    print("I got %r" %i)

# we can also build lists, first start with an empty one
elements = []

for i in range(2,7):
    elements.append(i)

elements.append(2)
elements.remove(2)  #移除索引值

for i in elements:
    print("Element was: %d" %i)
print("%r" %elements.reverse())

for i in elements:
    print("Element was: %d" %i)
