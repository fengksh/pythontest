import os
#os.chdir('chapter3')
#print(os.getcwd())
'''
os.open 打开有问题，暂时不明白如何jie
直接open方法没有问题

'''
print(os.getcwd())
file = open(r'E:/work/python/testpython/chapter3/sketch.txt')
#print(file.read(),end="")
file.close()
'''
文件关闭后无法在读取文件
'''
#print(file.read(),end="")
try:
    file = open(r'E:/work/python/testpython/chapter3/sketch.txt')
except:
    pass

'''
打印两行会一词打印
'''
#print(file.readline(),end="")
#print(file.readline(),end="")
#file.close()
for each_list in file:
    try:
        (role,line_spoken) = each_list.split(":",1)
        print(role,end="")
        print(" said: ",end="")
        print(line_spoken,end="")
    except:
        pass

for each_list in file:
        if not each_list.find(':') == -1:
            (role,line_spoken) = each_list.split(":",1)
            print(role,end="")
            print(" said: ",end="")
            print(line_spoken,end="")
        else:
            pass