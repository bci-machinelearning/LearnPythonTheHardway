#coding=utf-8  //测试

'''
习题 17: 更多文件操作

现在让我们再学习几种文件操作。我们将编写一个 Python 脚本，将一个文件中的内容拷贝到另外一个文件中。
这个脚本很短，不过它会让你对于文件操作有更多的了解。

'''

from sys import argv
from os.path import exists

script,from_file,to_file = argv#读入脚本名称和文件名

print "Copying from %s to %s" %(from_file,to_file)

#we could do these two on one line too, how?

input = open(from_file)
indata = input.read()

print "The input file is %d bytes long" %len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready,hit return to contine, CTRL-C to abort."
raw_input()

output = open(to_file, 'w')
output.write(indata)

print "Alright,all done."

output.close()
'''如果不close()，那就要等到垃圾回收时，自动释放资源。垃圾回收的时机是不确定的，也无法控制的。

如果程序是一个命令，很快就执行完了，那么可能影响不大（注意：并不是说就保证没问题）。'''
input.close()


output = open(to_file,'w').write(open(from_file).read())
