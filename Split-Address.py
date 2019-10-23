def splitAddress(address):
    ptr = 0
    result = []
    for i in range(2):
        temp = ""
        while(address[ptr].isalnum() and ptr < len(address)-1):
            temp+=address[ptr]
            ptr+=1
            
        result.append(temp)
        
        while(not address[ptr].isalnum() and ptr <= len(address)-1):
            ptr+=1
            
    
    temp1 = address.split('.com')
    temp2 = ""
    
    for letter in temp1[1]:
        if letter.isalnum():
            temp2 += letter

    if temp2 != "":      
        result.append(temp2)
    return(result)