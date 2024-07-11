def zigZag(l):
    arr=l.copy()
    arr.sort()
    n=(len(arr)+1)//2
    arr[n:len(arr)-1].sort(reverse=True)
    return arr
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        l=zigZag(arr)
        print(l)
        for i in arr:
            print(i,end=' ')
