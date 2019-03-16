#coding=utf-8  //测试

'''
习题 25: 更多更多的练习
我们将做一些关于函数和变量的练习，以确认你真正掌握了这些知识。这节练习对你
来说可以说是一本道：写程序，逐行研究，弄懂它。
不过这节练习还是有些不同，你不需要运行它，取而代之，你需要将它导入到 python
里通过自己执行函数的方式运行

'''

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print("%r" %word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print("%r" %word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

say_hello = "Hello world, here I am"
print("function: break_word %s" %break_words(say_hello))
print_first_and_last(say_hello)
print_first_and_last_sorted(say_hello)


'''
import Exe_25
>>> sentence = "All good things come to those who wait."
>>> words = Exe_25.break_words(sentence)
>>> words
['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
>>> sorted_words = Exe_25.sort_words(words)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> Exe_25.print_last_word(words)
'wait.'
>>> Exe_25.print_first_and_last_sorted(sentencs)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    Exe_25.print_first_and_last_sorted(sentencs)
NameError: name 'sentencs' is not defined
>>> Exe_25.print_first_and_last_sorted(sentence)
'All'
'who'
>>> help(Exe_25)

'''
