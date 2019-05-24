def gRange(a, b=None): #need to add step and begin
    """
    @param a: either a list or an int.
    @param b: either a list or an int or None
    @return: if A and B are lists: for elements of A without elements of B
             if A list and B an int: for element of A without A[b]
             if a an int and B a list: for elements from 0 to a, without elements of b
             if a and b are int : for elements from 0 to a, exept b
    """
    if type(a) == 'list' and type (b) == 'list' :
        c=[]
        for k in a :
            tmp=0
            for l in b :
                if l == k :
                    tmp += 1
            if tmp == 0 :
                c.append(k)
        return c
    elif type(a) == 'list' and type(b) == 'int':
        del a[b]
        return a
    elif type(a) == 'list' and b == None : 
        return a
    elif type(a) == 'int' and type (b) == 'list' :
        c=[]
        for k in range(0,a) :
            tmp=0
            for l in b :
                if l == k :
                    tmp += 1
            if tmp == 0 :
                c.append(k)
        return c
    elif type(a) == 'int' and type(b) == 'int':
        c=[]
        for k in range(0,a) :
            if k != b:
                c.append(k)
        return c
    
    elif type(a) == 'int' and b == None : 
        c=[]
        for k in range(0,a):
            c.append(k)
        return c
    else :
        print("Type error")
        return 1