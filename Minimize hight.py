def getMinDiff(arr, n, k):
        # code here
    new=[]

    if arr[0]<=k:
        new.append((arr[0]+k))
    else:
        new.append((arr[0]-k))

    high=new[0]
    low=new[0]

    for i in range(1,n):

        if arr[i]<=k:
            new.append((arr[i]+k))
        else:
            new.append((arr[i]-k))

        if high<new[i]:
            high=new[i]

        if low>new[i]:
            low=new[i]

    return (high-low)


arr=[7,7,3,5]
n=4
k=1
print(getMinDiff(arr,n,k))
