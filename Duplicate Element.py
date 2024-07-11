arr=[1,2,3,4,5,1,4,5]
new=[]
for a in arr:
    n=arr.count(a)
    if n>1:
        if new.count(a)==0:
            new.append(a)
if len(new)!=0:
    print(new)
else:
    print(-1)
