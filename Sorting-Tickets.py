tickets = [{'dep': 'C', 'arr': 'D'}, 
           {'dep': 'A', 'arr': 'B'},
           {'dep': 'D', 'arr': 'A'},
           {'dep': 'B', 'arr': 'C'}]
starting_city = "A"

ans = [starting_city]

while tickets != []:
    for item in tickets:
        if starting_city in item['dep']:
            ans.append(item['arr'])
            starting_city = item['arr']
            tickets.pop(tickets.index(item))
            
            
print(ans[:-1])