import random
def rando(n):   
    inside = 0
    total = 0
    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        
        distance = x**2 + y**2
        
        if distance <= 1:
            inside += 1
        total += 1
    
    return 4*(inside/total)


print(rando(100000000))        