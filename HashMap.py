
def hashMap(queryType, query):
    keys = []
    values = []
    res = 0
    
    for typ, val in zip(queryType, query):
        if typ == "insert":
            keys.append(val[0])
            values.append(val[1])
                        
        elif typ == "addToValue":
            #res2 = [x + val[0] for x in values] 
            #values = res2
            
            for i in range(len(values)):
                values[i] += val[0]
                
            
        elif typ == "addToKey":
            #res1 = [x + val[0] for x in keys] 
            #keys = res1
            
            for i in range(len(keys)):
                keys[i] += val[0]
            
        elif typ == "get":
            '''if (len(keys) != 0 and len(values) != 0):
                for i in range(0, len(keys)):
                    if keys[i] == val[0]:
                        res+=values[i]'''
            
            res += values[keys.index(val[0])]

    return(res)
