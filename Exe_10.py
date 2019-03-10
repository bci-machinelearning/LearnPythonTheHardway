#coding=utf-8  //测试

'''
习题 10: 那是什么？
在习题 9 中我你接触了一些新东西。我让你看到两种让字符串扩展到多行的方法。第一种方法是在月份之间用 \n (back-slash n )隔开。这两个字符的作用是在该位置上放入一个“新行(new line)”字符。

使用反斜杠 \ (back-slash) 可以将难打印出来的字符放到字符串。针对不同的符号有很多这样的所谓“转义序列(escape sequences)”，但有一个特殊的转义序列，就是 双反斜杠(double back-slash) \\ 。这两个字符组合会打印出一个反斜杠来。接下来我们做几个练习，然后你就知道这些转义序列的意义了。

另外一种重要的转义序列是用来将单引号 ' 和双引号 " 转义。想象你有一个用双引号引用起来的字符串，你想要在字符串的内容里再添加一组双引号进去，比如你想说"I "understand" joe."，Python 就会认为 "understand" 前后的两个引号是字符串的边界，从而把字符串弄错。你需要一种方法告诉 python 字符串里边的双引号不是真正的双引号。

要解决这个问题，你需要将双引号和单引号转义，让 Python 将引号也包含到字符串里边去。这里有一个例子：
"I am 6'2\" tall."  # 将字符串中的双引号转义
'I am 6\'2" tall.'  # 将字符串种的单引号转义
第二种方法是使用“三引号(triple-quotes)”，也就是 """

'''
tabby_cat = "\tI'm tabbled in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

tabby_cat_str = "%rI'm tabbled in." %'\t'
print tabby_cat_str
