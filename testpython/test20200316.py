
try:
    file = open(r'E:/work/python/testpython/chapter3/sketch1.txt')
    for eacH_list in file:
        try:
            (roles,tttt) = eacH_list.split(':',1)
            print(roles,end="")
            print(" : ",end="")
            print(tttt,end='')
        except ValueError:
            pass

    file.close()
except IOError:
    print("data is missing")

'''
man = []
other= []
try:
    data = open(r'E:/work/python/testpython/chapter3/sketch.txt')
    for eacHa_list in data:
        try:
            (role,line_spoken) = eacHa_list.split(":",1)
            line_spoken = line_spoken.strip()
            if role =='Man':
                man.append(line_spoken)
            elif role == "Other Man":
                other.append(line_spoken)
        except ValueError:
            pass
except IOError:
    print("data is missing")

print(man)
print(other)
'''
out = open(r'E:/work/python/testpython/chapter3/sketch1.txt',"w")
print("HHHHHHHHHHHHHHHHHHHHHHHHHHsssssss",file = out)
out.close()
out1 = open(r'E:/work/python/testpython/chapter3/sketch1.txt')
#print('11111111111111')
#print(out1.readlines())
#print('2222222222222222')
out1.close()

man = []
other = []
try:
    spoke = open(r'E:/work/python/testpython/chapter3/sketch.txt')
    for sopken_list in spoke:
        try:
            (role,spoken) = sopken_list.split(":",1)
            if role == 'Man':
                man.append(spoken)
            elif role =='Other Man':
                other.append(spoken)
        except ValueError:
            pass
    spoke.close()
except IOError:
    print('data is missng')


try:
    with open('E:/work/python/testpython/chapter3/missing.txt','w') as man_file,open('E:/work/python/testpython/chapter3/other_data.txt','w') as other_file:
        print(man,file = man_file)
        print(other,file=other_file)
except IOError as err:
    print("File Error:" + str(err))

print("1111111111111")
'''
try:
    data = open('E:/work/python/testpython/chapter3/missing.txt')
    print(data.readlines())
except IOError as err:
    print('File Error: '+ str(err))
finally:
    if 'data' in locals():
        data.close()
'''

try:
    with open('E:/work/python/testpython/chapter3/missing.txt','w') as data:
        print('it is a file',file = data)
except IOError as err:
    print("File Error: "+str(err))


