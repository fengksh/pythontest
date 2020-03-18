import sys
import pickle
def print_lol(the_list,ident = False,num = 1, out = sys.stdout):
    for each_list in the_list:
        if isinstance(each_list,list):
            print_lol(each_list,ident,num+1,out)
        else:
            if ident:
                for each in range(num):
                    print('\t',end="",file=out)
            print(each_list,file=out)


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
    with open(r'E:/work/python/testpython/chapter3/man_data.txt','wb') as man_file,open(r'E:/work/python/testpython/chapter3/other_data.txt','wb') as other_file:
        pickle.dump(man,man_file)
        pickle.dump(other,other_file)
except pickle.PickleError as err:
    print(str(err))

new_man =[]
try:
    with open(r'E:/work/python/testpython/chapter3/man_data.txt','rb') as man_file:
        new_man = pickle.load(man_file)
except IOError as err:
    print(str(err))
except pickle.PickleError as err:
    print(str(err))
print(new_man[0])
#print(new_man[-19])
'''
sorted(值)是复制排序
值.sort()是原地排序
'''
def sanitize(time):
    if '-' in time:
        spliter = '-'
    elif ':' in time:
        spliter = ':'
    else:
        return(time)
    (mins,secord) = time.split(spliter)
    return(mins+'.'+secord)

def openfile(fn = sys.stdout):
    try:
        with open(fn) as out:
            newname = dict()
            names = out.readline().strip().split(',')
            (newname['name'],newname['birthday']) = names.pop(0),names.pop(0)
            newname['time'] = sorted(set([sanitize(namses_test) for namses_test in names]))
            return newname
    except IOError as ioerr:
        print("FIle Eror: "+str(ioerr))
        return (None)


#print(openfile(r'E:/work/python/testpython/chapter3/20200917/james.txt')[0:3])
#print(openfile(r'E:/work/python/testpython/chapter3/20200917/julie.txt')[0:3])
#print(openfile(r'E:/work/python/testpython/chapter3/20200917/mikey.txt')[0:3])
newnames = dict()
newnames = openfile(r'E:/work/python/testpython/chapter3/20200917/sarah.txt')
print(newnames['name']+' birthday is '+newnames['birthday']+" and fastest times are"+str(newnames['time'][0:3]))
'''
try:
    with open('mydata.pickle','rb') as mydatapickle:
        print(pickle.load(mydatapickle))
except IOError as err:
    print(str(err))
except pickle.PickleError as err:
    print(str(err))
'''