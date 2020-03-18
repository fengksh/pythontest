cleese ={}
palin = dict()
#print(type(cleese))
#print(type(palin))
cleese['Name'] = 'John Cleese'
cleese['Occupations'] = ['actor','comedian','writer','film producer']
palin = {'Name':'Michael Palin','Occupations':['comedian','actor','writer','tv']}

palin['Birthplace'] = 'Broomhill,Sheffield,England'
cleese['Birthplace'] = 'China,China,China'

#print(palin)
#print(cleese)


def sanitize(time_string):
    if '-' in time_string:
        spliter = '-'
    elif ':' in time_string:
        spliter = ':'
    else:
        return (time_string)
    (mins,secords) = time_string.split(spliter)
    return (mins+'.'+secords)
def getfilename(filenames):
    try:
        with open(filenames) as  file:
            data = file.readline().strip().split(',')
        newname = {}
        (newname['name'], newname['birthday']) = data.pop(0), data.pop(0)
        newname['time'] = sorted(set(sanitize(t) for t in data))
        return newname
    except IOError as err:
        print('file is missing' + str(err))
        return None

newname = getfilename(r'E:/work/python/testpython/chapter3/20200917/sarah.txt')

#print(sorted(set([sanitize(t) for t in newname['time']]))[0:3])
#newname['time'] = sorted(set(sanitize(t) for t in sarah))[0,3]

print(newname['name']+"'s fastest times are: "+str(newname['time'][0:3]))


