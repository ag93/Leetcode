def pizzaTreats(cnt ,days):  
    i = 0
    
    if not days:
        return("YES")
    
    while i < cnt-1:
        if days[i] == -1:
            return("NO")
            break
        if days[i]%2 == 1:
            days[i] = 0
            days[i+1]-=1
            i+=1
        elif days[i] %2 == 0:
            days[i] = 0
            i+=1
            
    if days[-1] % 2 == 0:
        days[-1] = 0
        
    if days.count(0) == len(days):
        return("YES")
    else:
        return("NO")
        
days = [10,201,101,111,10] 
cnt = len(days)       
print(pizzaTreats(cnt, days))