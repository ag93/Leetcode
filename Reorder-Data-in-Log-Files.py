class Solution:
    def reorderLogFiles(logs):
        def getKey(log):
            all_parts = log.split()
            key, rest = all_parts[0], all_parts[1:]
            return  [' '.join(rest), ' ' + key]
        
        letterLogs = []``
        digitLogs = []
        
        for log in logs:
            if log.split()[1].isalpha():
                letterLogs.append(log)
            else:
                digitLogs.append(log)
                
        letterLogs.sort(key=getKey)
        return(letterLogs+digitLogs)

    logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]
    result = reorderLogFiles(logs)
    print(result)