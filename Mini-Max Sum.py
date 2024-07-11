def sum(l):
    max=0
    min=0
    l.sort()
    for i in range(4):
        max=max+l[i+1]
        min=min+l[i]
        print(min,max)
    return min,max
    
