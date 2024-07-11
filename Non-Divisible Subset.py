def nonDivisibleSubset(k, s):
    reminderList = []
    for el in s:
        reminderList.append(el%k)
    result = 0
    freqDict = {}
    if reminderList.count(0) >0:
        result+=1
    if k%2 ==0:
        if reminderList.count(k/2) > 0:
            result+=1
    for i in range(1,k):
        if i == k/2:
            continue
        freqDict[i] = reminderList.count(i)
    for i in range(1, k//2 +1):
        if i == k/2:
            continue
        if freqDict[i] > freqDict[k-i]:
            result += freqDict[i]
        else:
            result += freqDict[k-i]
    return result