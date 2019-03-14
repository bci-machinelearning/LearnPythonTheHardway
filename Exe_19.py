#coding=utf-8  //测试

'''
习题 18:  19: 函数和变量

函数这个概念也许承载了太多的信息量，不过别担心。只要坚持做这些练习，对照上个练习中的检查点检查一遍这次的联系，你最终会明白这些内容的。

有一个你可能没有注意到的细节，我们现在强调一下：函数里边的变量和脚本里边的变量之间是没有连接的。下面的这个练习可以让你对这一点有更多的思考：

'''

def cheese_and_crackers(cheese_count, boxes_of_crackers):#定义了一个函数
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

def self_designFun(var_01):
    print"%d" %(var_01+ 1);
    return var_01 + 1

print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

print "Or we can use variables from our scripts:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10+15,5+6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 1000,amount_of_crackers + 100)

self_designFun(1)
self_designFun(amount_of_cheese)
self_designFun(self_designFun(1))
self_designFun(self_designFun(1) + 1)
self_designFun(self_designFun(self_designFun(1)))
