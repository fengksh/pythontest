movies = ["The Holy Grail","The Life of Brian","The Meaning of life"]
movies.insert(1,1976)
movies.insert(3,1996)
movies.append(2020)
#print(movies);
movies_test = ["The Holy Grail",1111,"The Life of Brian",2222,"The Meaning of life",3333]
#print(movies_test)
cast =["Cleese","Palin","Jones","Idle"]
#print(len(cast))
#cast.append("Aaaaa")
#print(cast)

#print(cast.pop())
#print(cast)
'''
len（）计算数据项长度
append是在列表末尾添加一个数据项
pop是从列表末尾删除数据
extend是在列表末尾增加一个数据项集合
'''
cast_test = ["1111","2222"]
cast.extend(cast_test)
#print(cast)

'''
remove()删除特定数据项
insert()在特定位置添加一个数据项
'''
cast.remove("1111")
#print(cast)
cast.insert(3,cast_test)
#print(cast)
for each_test in movies:
    #print(each_test)
    for each_list in movies:
        #print(each_list)
        pass

count = 0
while count < len(movies):
        #print(str(movies[count])+str(1))
        count = count + 1

'''
isinstance(数据，类型)判断数据是否为后面定义的类型
在字符串中"\"代表转义  想不转义有两种办法 
    第一\\ 
    第二在字符串开头写个小r就不转义 例如：r"\asdasda"
'''
#print(isinstance(movies,list))
#print(isinstance("\"1",str))
#print("\asdasda")
#print(r"\asdasda")
#print(isinstance(1,str))

movies_test_test = ["11111","22222",["33333","44444",["55555","66666"]]]

''' test
for each_list in movies_test_test:
    print(each_list)
    if isinstance(each_list,list):
        for each_list_test in each_list:
            print(each_list_test)
            if isinstance(each_list_test,list):
                for each_list_test_test in each_list_test:
                    print(each_list_test_test)

'''
'''
for each_list in movies_test_test:
    if isinstance(each_list,list):
        for each_list_test in each_list:
            if isinstance(each_list_test,list):
                for each_list_test_test in each_list_test:
                    if isinstance(each_list_test_test,list):
                        pass
                    else:
                        print(each_list_test_test)
            else:
                print(each_list_test)
    else:
        print(each_list)
'''

'''
hahahahaha fengksh NB
'''
'''定义第一个python函数'''
def for_test (thelist):
    """for循环嵌套遍历"""
    for thelist_test in thelist:
        if isinstance(thelist_test,list):
            for_test(thelist_test)
        else:
            print(thelist_test)

for_test(movies_test_test)

