class Fengksh(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)
    def top3(self):
        return sorted(set([sanitize(t) for t in self]))[0:3]
    def add_time(self,time):
        self.append(time)
    def add_times(self,times=[]):
        self.extend(times)

''''''


def getfilename(filenames):
    try:
        with open(filenames) as  file:
            data = file.readline().strip().split(',')

        return Fengksh(data.pop(0), data.pop(0), data)
    except IOError as err:
        print('file is missing' + str(err))
        return None


''''''


def sanitize(time_string):
    if '-' in time_string:
        spliter = '-'
    elif ':' in time_string:
        spliter = ':'
    else:
        return (time_string)
    (mins, secords) = time_string.split(spliter)
    return mins + '.' + secords


sarah = getfilename(r'E:/work/python/testpython/chapter3/20200917/sarah.txt')
sarah.add_time('1.11')
sarah.add_times(['1.5','2.7','3.3'])
print(sarah)
print(sarah.name + "'s fastest times are: " + str(sarah.top3()))

print(str(sarah.top3()))




