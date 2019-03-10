#coding=utf-8  //测试

'''
习题16：读写文件

如果你做了上一个练习的加分习题，你应该已经了解了各种文件相关的命令（方法/函数）。你应该记住的命令如下：

    close – 关闭文件。跟你编辑器的 文件->保存.. 一个意思。
    read – 读取文件内容。你可以把结果赋给一个变量。
    readline – 读取文本文件中的一行。
    truncate – 清空文件，请小心使用该命令。
    write(stuff) – 将stuff写入文件。

这是你现在该知道的重要命令。有些命令需要接受参数，这对我们并不重要。你只要记住 write 的用法就可以了。
write 需要接收一个字符串作为参数，从而将该字符串写入文件。

让我们来使用这些命令做一个简单的文本编辑器吧:


'''

from sys import argv

script,filename = argv#读入脚本名称和文件名

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C(^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print"Opening the file..."
target = open(filename,'w')

print "Now I'm going to ask you for thress lines."

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."

target.close()
