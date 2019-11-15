cnt = {}
m = [[1,4,-2],
     [-2,3,4],
     [3,1,3]]

"""
Answer:
3 3 4
3 4 1
1 -2 -2
"""

ROW = len(m)
COL = len(m[0])

result = [[0]* len(m[0]) for k in range(len(m))]

for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] not in cnt:
            cnt[m[i][j]] = 1
        else:
            cnt[m[i][j]] += 1

cnt = sorted(cnt.items(), key=lambda item: item[1], reverse = True)

final = {}

for item in cnt:
    if item[1] not in final:
        final[item[1]] = [item[0]]
    else:
        final[item[1]].append(item[0])
        final[item[1]].sort(reverse = True)


final_list = []

for item in final:
    for i in range(len(final[item])):
        for _ in range(item):
            final_list.append(final[item][i])
            
c = 0
for line in range(1, (ROW + COL)) :  
        start_col = max(0, line - ROW)   
        count = min(line, (COL - start_col), ROW) 
        for j in range(0, count) : 
            result[start_col + j][min(ROW, line) - j - 1] = final_list[c]
            c+=1
            
print(result)