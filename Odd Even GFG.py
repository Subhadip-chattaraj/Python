s=input()
s=list(s)
x=0#Even
y=0#Odd
for i in s:
    pos=ord(i) - ord('a')+1
    freq=s.count(i)
    print(pos,freq)
    if pos%2==0 and freq%2==0:
        x+=1
    elif pos%2!=0 and freq%2!=0:
        y+=1
if (x+y)%2==0:
    print("Even")
else:
    print("Odd")

