import os
#os.chdir('chapter3')
#print(os.getcwd())
'''
os.open 打开有问题，暂时不明白如何jie
直接open方法没有问题

'''
print(os.getcwd())
file = open(r'E:/work/python/testpython/chapter3/sketch.txt')
print(file.read(),end="")
file.close()
'''
文件关闭后无法在读取文件
'''
#print(file.read(),end="")
