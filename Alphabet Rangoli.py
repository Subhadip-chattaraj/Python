def par(n):
    m=2*((2*n)-2)+1
    for i in range(n):
        ch=97+n-1
        f=0
        c=0
        for j in range(m):
            if j<((2*n)-(i*2+2)) or f==(4*i)+1:
                print("-",end='')
            elif j%2==0:
                print(chr(ch),end='')
                f+=1
                c+=1
                if c<(i+1):
                    ch-=1
                elif c>=(i+1):
                    ch+=1
            else:
                print("-",end='')
                f+=1
        print()
    for i in range(n-2,-1,-1):
        f=0
        c=0
        ch=97+n-1
        for j in range(m):
            if j<((2*n)-(i*2+2)) or f==(4*i)+1:
                print("-",end='')
            elif j%2==0:
                print(chr(ch),end='')
                f+=1
                c+=1
                if c<(i+1):
                    ch-=1
                elif c>=(i+1):
                    ch+=1
            else:
                print("-",end='')
                f+=1
        print()

if __name__=='__main__':
    n=int(input())
    par(n)
