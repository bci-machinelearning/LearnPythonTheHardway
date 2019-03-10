#coding=utf-8  //测试

'''
习题 14: 提示和传递

让我们使用 argv 和 raw_input 一起来向用户提一些特别的问题。
下一节习题你会学习如何读写文件，这节练习是下节的基础。在这道习题里我们将用略微不同的方法使用 raw_input，让它打出一个简单的 > 作为提示符。
这和一些游戏中的方式类似，例如 Zork 或者 Adventure 这两款游戏。
'''

from sys import argv

script,user_name,last_name = argv
prompt ='>'

print "Hi %s, I'm the %s script."%(user_name,script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" %user_name

likes = raw_input(prompt)

print "Where do you like to live %s?"% user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so %s said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (last_name,likes, lives, computer)
