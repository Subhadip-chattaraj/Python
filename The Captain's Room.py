def freq(l,s):
    c=0
    for i in l:
        if i==s:
            c+=1
            l.remove(i)
    return c

def theCaptain(l):
    m=set(l)
    for i in m:
        if i in l:
            c=freq(l,i)
            if c==1:
                return i


if __name__=='__main__':
    k=int(input())
    l=list(map(int,input().split()))
    print(theCaptain(l))

