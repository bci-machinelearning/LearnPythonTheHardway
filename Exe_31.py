#coding=utf-8  //测试

'''
习题 31: 作出决定
这本书的上半部分你打印了一些东西，而且调用了函数，不过一切都是直线式进行的。
你的脚本从最上面一行开始，一路运行到结束，但其中并没有决定程序流向的分支点。
现在你已经学了 if, else, 和 elif ，你就可以开始创建包含条件判断的脚本了。

上一个脚本中你写了一系列的简单提问测试。这节的脚本中，你将需要向用户提问，依据用户的答案来做出决定。
把脚本写下来，多多鼓捣一阵子，看看它的工作原理是什么。

'''


print("You enter a dark room with two doors.  Do you go through door #1 or door #2?")

door = input(">>")

if door == "1":
    print( "There's a giant bear here eating a cheese cake.  What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input(">>")
    if bear == "1":
        print("The bear eats your face off.  Good job!")
    elif bear == "2":
        print("The bear eats your legs off.  Good job!")
    else:
        print("Well, doing %s is probably better.  Bear runs away." %bear)

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = raw_input(">>")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.  Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.  Good job!")

else:
    print("You stumble around and fall on a knife and die.  Good job!")
