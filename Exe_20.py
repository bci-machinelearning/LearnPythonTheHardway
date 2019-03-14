#coding=utf-8  //测试

'''
习题 20: 函数和文件

回忆一下函数的要点，然后一边做这节练习，一边注意一下函数和文件是如何在一起协作发挥作用的。

'''

from sys import argv

script,input_file = argv#载入属性

def print_all(f):
    print f.read()  #全部打印

def rewind(f):
    f.seek(1)       #偏移量+1

def print_a_line(line_count,f):
    print line_count,f.readline()

current_file = open(input_file) #读入文件变量

print "First let's print the whole file:\n"

print_all(current_file)

print"Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print 3 lines"

line_number = 0
print_a_line(line_number,current_file)    #按顺序向下进行行读取
line_number+=1
print_a_line(line_number,current_file)    #按顺序向下进行行读取
line_number+=1
print_a_line(line_number,current_file)    #按顺序向下进行行读取
line_number+=1

print current_file.readline()
