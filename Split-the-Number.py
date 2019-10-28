
N = 1232
pattern = "ab+cd"

n = str(N)

if pattern.count("-") == 1:
    pattern = pattern.split("-")
    number1 = int(n[:len(pattern[0])])
    number2 = int(n[len(pattern[0]):])
    
    print(number1 - number2)
    
elif pattern.count("+") == 1:
    pattern = pattern.split("+")
    number1 = int(n[:len(pattern[0])])
    number2 = int(n[len(pattern[0]):])
    print(number1 + number2)
    