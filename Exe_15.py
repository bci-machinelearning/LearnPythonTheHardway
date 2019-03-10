#coding=utf-8  //测试

'''
习题 15: 读取文件

你已经学过了 raw_input 和 argv，这些是你开始学习读取文件的必备基础。你可能需要多多实验才能明白它的工作原理，所以你要细心做练习，并且仔细检查结果。
处理文件需要非常仔细，如果不仔细的话，你可能会吧有用的文件弄坏或者清空。导致前功尽弃。
这和一些游戏中的方式类似，例如 Zork 或者 Adventure 这两款游戏。

这节练习涉及到写两个文件。一个正常的 ex15.py 文件，另外一个是 ex15_sample.txt，第二个文件并不是脚本，而是供你的脚本读取的文本文件。以下是后者的内容：

This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.


'''

from sys import argv

script,filename = argv#读入脚本名称和文件名

txt = open(filename) #打开文件对象

print "Here's your file %r"%filename
print txt.read()#读入文件内容

print "Type the filename again:"
file_again=raw_input(">")

txt_again = open(file_again)
print txt_again.read()
