#coding=utf-8  //测试

'''虽然你已经在程序中写过字符串了，你还没学过它们的用处。在这章习题中我们将使用复杂的字符串来建立一系列的变量，从中你将学到它们的用途。
首先我们解释一下字符串是什么 东西。
字符串通常是指你想要展示给别人的、或者是你想要从程序里“导出”的一小段字符。Python 可以通过文本里的双引号 " 或者单引号 ' 识别出字符串来。
这在你以前的 print 练习中你已经见过很多次了。如果你把单引号或者双引号括起来的文本放到 print 后面，它们就会被 python 打印出来。

字符串可以包含格式化字符 %s，这个你之前也见过的。你只要将格式化的变量放到字符串中，再紧跟着一个百分号 % (percent)，再紧跟着变量名即可。
唯一要注意的地方，是如果你想要在字符串中通过格式化字符放入多个变量的时候，你需要将变量放到 ( ) 圆括号(parenthesis)中，而且变量之间用 , 逗号(comma)隔开。就像你逛商店说“我要买牛奶、面包、鸡蛋、八宝粥”一样，只不过程序员说的是”(milk, eggs, bread, soup)”。

我们将键入大量的字符串、变量、和格式化字符，并且将它们打印出来。我们还将练习使用简写的变量名。程序员喜欢使用恼人的难度的简写来节约打字时间，所以我们现在就提早学会这个，这样你就能读懂并且写出这些东西了。'''


x = 'There are %d types of people.'%10 #使用%占位符，将常量10传入
binary = "binary"
do_not = "don't"

y = "Those who know %s and those who %s." %(binary,do_not)
#使用占位符，以变量传入，多变量传入写作%(a,b)
print x
print y

hilarious = False
joke_evalution = "Isn't that joke so funny?! %r"

print joke_evalution % hilarious
#字符串以变量存在
print joke_evalution+str(hilarious)

w="This is the left side of..."
e="a string with a right side."
print w+e
#字符串用 + 连接
