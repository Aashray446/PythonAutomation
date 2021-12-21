def convertTostring (lst):
    req_string = ''
    

    try:
        if(len(lst) == 1):
            print(lst[0])
        #For more than one
        else:
            for i in range(0,len(lst)-1):
                req_string += lst[i]
                req_string += ", "
            req_string += "and "
            req_string += lst[-1]
            print(req_string)
    except:
        print("I guess you entered wrong input or null")
abc = ["asd", "asd", "asd"]
convertTostring(['ads'])