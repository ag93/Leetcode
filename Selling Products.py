#
# Complete the 'deleteProducts' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ids
#  2. INTEGER m
#
import collections
def deleteProducts(ids, m):
    # Write your code here
    cnt = collections.Counter(ids)
    cnts = list(cnt.values())
    print(cnt, cnts)
    
    while m > 0:
        min_ = min(cnts)
        ind = cnts.index(min_)
        if m >= min_:
            cnts.pop(ind)
            m -= min_
        else:
            break
    return len(cnts)