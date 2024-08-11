def minimumPlatform(n,arr,dep):
    arr.sort()
    dep.sort()
    i=j=0
    maxi=platform=0
    while i<n and j<n:
        if arr[i]<=dep[j]:
            i+=1
            platform+=1
            maxi=max(platform,maxi)
        else:
            platform-=1
            j+=1
    return maxi

arr=[900, 940, 950, 1100, 1500, 1800]
dep=[910, 1200, 1120, 1130, 1900, 2000]
n=6
print(minimumPlatform(n,arr,dep))


