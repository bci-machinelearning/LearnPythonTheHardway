#coding=utf-8  //测试

'''
习题 13: 参数、解包、变量

在这节练习中，我们将降到另外一种将变量传递给脚本的方法(所谓脚本，就是你写的 .py 程序)。
你已经知道，如果要运行 ex13.py，只要在命令行运行 python ex13.py 就可以了。这句命令中的 ex13.py 部分就是所谓的“参数(argument)”，我们现在要做的就是写一个可以接受参数的脚本。

将下面的程序写下来，后面你将看到详细解释。
'''

from sys import argv

script,first,second,third = argv

user_input = raw_input("What you want to say?")

print "The script name is",script
print "Your first argument is",first
print "Your first argument is",second
print "Your first argument is",third
print "Customer argument is",user_input
