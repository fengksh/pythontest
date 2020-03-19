def for_test (thelist,iss = False,level=0):
    """for循环嵌套遍历"""
    for thelist_test in thelist:
        if isinstance(thelist_test,list):
            for_test(thelist_test,iss,level+1)
        else:
            if iss:
                for asd in range(level):
                    print("\t",end="")
            print(thelist_test)