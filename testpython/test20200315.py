import os
file = open(r'E:/work/python/testpython/chapter3/sketch.txt')
ss = os.path.exists(r'E:/work/python/testpython/chapter3/sketch.txt')
osfile = os.access(r'E:/work/python/testpython/chapter3/sketch1.txt',os.F_OK)
osreadfile = os.walk(r'E:/work/python/testpython/chapter3/sketch1.txt')
print(osfile)


File = open('E:/work/python/testpython/chapter3/sketch.txt')
lines = File.readlines()
#print(lines)
newList = []
for index in range(len(lines)):
    newList.append(lines[index])
#print(newList)



 