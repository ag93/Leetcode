def meanGroups(a):
    dict = {}
    for i in range(0, len(a)):
        mean = sum(a[i])/len(a[i])
        if mean not in dict:
            dict[mean] = [i]
        else:
            dict[mean].append(i)

    return(list(dict.values()))