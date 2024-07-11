def score_words(s):
    w=s.split()
    v="aeiouy"
    result=0
    for i in w:
        c=0
        for j in i:
            if j in v:
                c+=1
        print(c)
        if c%2==0:
            score=2
        else:
            score=1
        print(score)
        result=result+score
    return result
                
            
if __name__=="__main__":
    n=int(input())
    s=input()
    v= score_words(s)
    print(v)
