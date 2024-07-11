def cat_hat(str):
  ##your code here##
  ##You need to write complete code this time 
  m='cat'
  n='hat'
  cat=0
  hat=0
  for i in range(0,len(str)):
    p=i
    if str[i]==m[0] and i!=len(str)-1:
        c=0
        for j in m:
            if p==len(str) or j!=str[p]:
                break
            else:
                c+=1
                p+=1
        if c==3:
            cat+=1
    elif str[i]==n[0] and i!=len(str)-1:
        c=0
        for j in n:
            if p==len(str) or j!=str[p]:
                break
            else:
                c+=1
                p+=1
        if c==3:
            hat+=1
  if cat==hat:
      return True
  else:
      return False


