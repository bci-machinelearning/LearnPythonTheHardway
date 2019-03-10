#coding=utf-8  //测试

'''
习题 8: 打印，打印
'''


formatter = "%r %r %r %r"
print formatter %(1,2,3,4)
print formatter %("One","Two","Three","Four")
print formatter %(True,False,False,True)
print formatter %(formatter,formatter,formatter,formatter)

print formatter %(
"I had this thing.",
"That you could type up right.",
"But it didn't sing.", #" 优先级高于' ，如果字符串中要包含 ‘，必须用“囊括它
"So I said goodnight."
)
