def sol(s):
    l=s.split('')
    for i in range(len(l)):
        l[i]=l[i].capitalize()
    s=' '.join(l)
    return s

if __name__=="__main__":
    s=input()
    print(sol(s))
