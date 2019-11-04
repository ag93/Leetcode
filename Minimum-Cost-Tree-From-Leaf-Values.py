'''     
        Given an array A, choose two neighbors in the array a and b,
        we can remove the smaller one min(a,b) and the cost is a * b.
        What is the minimum cost to remove the whole array until only one left?
        
        To remove a number a, it needs a cost a * b, where b >= a.
        So a has to be removed by a bigger number.
        We want minimize this cost, so we need to minimize b.

        b has two candidates, the first bigger number on the left,
        the first bigger number on the right.

        The cost to remove a is a * min(left, right).
        
'''
def mctFromLeafValues(arr):
        def findMinProd(arr):
            n = len(arr)
            if n == 1:
                return -1
            minprod = float('inf')
            minidx = 0
            for i in range(n-1):
                tmp = arr[i]*arr[i+1]
#                print("temp = ",tmp)
                if tmp<minprod:
                    minprod = tmp
                    minidx = i
#            print("Before ", arr)
            arr[minidx] = max(arr[minidx], arr[minidx+1])
#            print("After ", arr)
            del arr[minidx+1]
#            print("Del ", arr)
#            print(minprod)
            return minprod
        
        
        res = 0
        p = findMinProd(arr)
        while p!=-1:
            print(p)
            res += p
            p = findMinProd(arr)
        return res
    
    
arr = [6,2,4]
print(mctFromLeafValues(arr))