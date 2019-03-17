#coding=utf-8  //测试

'''
习题 29: 如果(if)
下面是你要写的作业，这段向你介绍了“if语句”。把这段输入进去，让它能正确执行。然后我们看看你是否有所收获。
'''

people
cats
dogs

if people<cats:   #python中用缩进符替代了C语言中 {} 的作用
    print("Too many cats! The world is doomed!")

if people<dogs:
    print("The world is drooled on!")

if people>dogs:
    print("The world is dry!")

dogs+=5

if people>=dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
     print("People are dogs.")
