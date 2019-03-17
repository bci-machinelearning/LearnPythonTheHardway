#coding=utf-8  //测试

'''
习题 28: 布尔表达式练习
上一节你学到的逻辑组合的正式名称是“布尔逻辑表达式(boolean logic expression)”。在编程中，布尔逻辑可以说是无处不在。它们是计算机运算的基础和重要组成部分，掌握它们就跟学音乐掌握音阶一样重要。

在这节练习中，你将在 python 里使用到上节学到的逻辑表达式。先为下面的每一个逻辑问题写出你认为的答案，每一题的答案要么为 True 要么为 False。写完以后，你需要将python 运行起来，把这些逻辑语句输入进去，确认你写的答案是否正确。


'''

True and True       T
False and True      T
1 == 1 and 2 == 1   F
"test" == "test"    T
1 == 1 or 2 != 1    T
True and 1 == 1     T
False and 0 != 0    F
True or 1 == 1  T
"test" == "testing" F
1 != 0 and 2 == 1   F
"test" != "testing" T
"test" == 1         F
not (True and False)T
not (1 == 1 and 0 != 1)F
not (10 == 1 or 1000 == 1000)F
not (1 != 10 or 3 == 4)F
not ("testing" == "testing" and "Zed" == "Cool Guy")T
1 == 1 and not ("testing" == 1 or 1 == 0)   T
"chunky" == "bacon" and not (3 == 4 or 3 == 3)  F
3 == 3 and not ("testing" == "testing" or "Python" == "Fun")    F
