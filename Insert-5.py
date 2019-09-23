def solution(N):
    if N == 0:
        return int('5' + str(N))
    
    elif N > 0:
       number = str(N)
       i = 0
       while(number[i] > '4'):
           i += 1
           if(i > len(number)-1):
               number = number + '5'
               return(number)
       number = number[:i] + '5' + number[i:]
       return(int(number))

    else:
        number = str(N)
        i = 0
        while(number[i] < '5'):
            i += 1
            if(i > len(number)-1):
                number = number + '5'
                return(number)
        number = number[:i] + '5' + number[i:]
        return(int(number))

N = -470
print(solution(N))