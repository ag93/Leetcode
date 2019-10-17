
def mergeStrings(s1, s2):
    ptr1 = 0
    ptr2 = 0
    result = ""

    while ptr1 < len(s1) and ptr2 < len(s2):
        if s1.count(s1[ptr1]) < s2.count(s2[ptr2]):
            result+=s1[ptr1]
            ptr1+=1
        elif s1.count(s1[ptr1]) > s2.count(s2[ptr2]):
            result+=s2[ptr2]
            ptr2+=1
        else:
            if s1[ptr1] < s2[ptr2]:
                result+=s1[ptr1]
                ptr1+=1
            elif s1[ptr1] > s2[ptr2]:
                result+=s2[ptr2]
                ptr2+=1  
            else:
                result+=s1[ptr1]
                ptr1+=1

    if (ptr1 != len(s1)):
        result+=s1[ptr1:]

    if (ptr2 != len(s2)):
        result+=s2[ptr2:]

    return(result)