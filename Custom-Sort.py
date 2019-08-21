class Solution(object):
    def CustomSort(a):
#a = [6, 3, 4, 5, 11, 17, 18, 22]

left_ptr = 0
right_ptr = len(a) - 1
count = 0

while (right_ptr > left_ptr):    
    while(a[left_ptr] % 2 == 0):
        left_ptr = left_ptr + 1
        
    while(a[right_ptr] % 2 != 0):
        right_ptr = right_ptr - 1
        
    if (right_ptr > left_ptr):
        a[left_ptr], a[right_ptr] = a[right_ptr], a[left_ptr]
        count = count + 1

print(a, "Number of Swaps ->" ,count)
return(count)