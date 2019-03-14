#coding=utf-8  //测试

'''
习题 18: 命名、变量、代码、函数

标题包含的内容够多的吧？接下来我要教你“函数(function)”了！咚咚锵！说到函数，不一样的人会对它有不一样的理解和使用方法，不过我只会教你现在能用到的最简单的使用方式。

函数可以做三样事情：

    它们给代码片段命名，就跟“变量”给字符串和数字命名一样。
    它们可以接受参数，就跟你的脚本接受 argv 一样。
    通过使用 #1 和 #2，它们可以让你创建“微型脚本”或者“小命令”。

你可以使用 def 新建函数。我将让你创建四个不同的函数，它们工作起来和你的脚本一样。然后我会演示给你各个函数之间的关系。

'''

#this is one like your scripts with argv
def print_two(*args):
    arg1,arg2=args
    print "arg1:%r, arg2: %r" %(arg1,arg2)

def print_two_again(arg1,arg2):
    print "arg1:%r, arg2: %r" %(arg1,arg2)

def print_one(arg1):
    print "arg1: %r" %arg1

def print_none():
    print "I got nothing'."

print_two("Zed","Shaw")  #传入时将变量打包
print_two_again("Zed","Shaw") #传入两个变量
print_one("First!")
print_none()
