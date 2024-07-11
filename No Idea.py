def happy(arr,A,B):
    like=set(A)
    dislike=set(B)
    mood=0
    for i in arr:
        if i in like:
            mood+=1
        elif i in dislike:
            mood-=1
    return mood

if __name__=="__main__":
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    res=happy(arr,A,B)
    print(res)
