#coding=utf-8  //测试

'''
习题 24: 更多联系

    你离这本书第一部分的结尾已经不远了，你应该已经具备了足够的 Python 基础知识，
可以继续学习一些编程的原理了，但你应该做更多的练习。这个练习的内容比较长，它的
目的是锻炼你的毅力，下一个习题也差不多是这样的，好好完成它们，做到完全正确，记
得仔细检查。

'''

print("Let's pratice everything.")
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem ='''
\tThe lovely world
 with logic so firmly planted
 cannot discern \n the needs of love
 nor comprehend passion from intuition
 and requires an explanation
\n\t\twhere there is none'''   #多行打印和转义字符

print("--------------------------")
print(poem)
print("--------------------------")

five = 10 -12 + 3 - 6
def secret_formula(started):    #定义方法
        jelly_beans = started * 500
        jars = jelly_beans/1000
        crates = jars / 100
        return jelly_beans,jars,crates

start_point = 10000
beans,jars,crates = secret_formula(start_point)

print("With a starting point of : %d" %start_point)
print("We'd  have %d beans,%d jars,%d crates" %(beans,jars,crates))

start_point /= 10

print("We can also do that this way.")
print("We'd  have %d beans,%d jars,%d crates" %secret_formula(start_point))
