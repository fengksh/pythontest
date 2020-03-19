import pickle
from test2020031901 import Fengksh

def get_coach_data(filenames):
    try:
        with open(filenames) as  file:
            data = file.readline().strip().split(',')
        return Fengksh(data.pop(0), data.pop(0), data)
    except IOError as err:
        print('file is missing' + str(err))
        return None
def put_to_store(files_list):
    all_athletes = {}
    for file in files_list:

        auh = get_coach_data(file)
        all_athletes[auh.name] = auh
    try:
        with open('../athletes,pickle', 'wb') as athf:
            pickle.dump(all_athletes,athf)
    except IOError as err:
        print(str(err))
    return all_athletes
def get_for_store():
    all_athletes = {}
    try:
        with open('../athletes,pickle', 'rb') as athf:
            pickle.load(all_athletes,athf)
    except IOError as err:
        print(str(err))
    return all_athletes



files_list = [r'E:/work/python/testpython/chapter3/20200917/james.txt',r'E:/work/python/testpython/chapter3/20200917/julie.txt',r'E:/work/python/testpython/chapter3/20200917/mikey.txt',r'E:/work/python/testpython/chapter3/20200917/sarah.txt']
data = put_to_store(files_list)
for each_list in data:
    print(data[each_list].name+' '+data[each_list].dob+'fast time is  '+str(data[each_list][0:3]) )