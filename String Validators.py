if __name__ == '__main__':
    s = input()
    num=0
    upch=0
    loch=0
    for i in s:
        if i>='0' and i<='9' and num==0:
            num+=1
        if i>='A' and i<='Z' and upch==0:
            upch+=1
        if i>='a' and i<='z' and loch==0:
            loch+=1
        if num>0 and upch>0 and loch>0:
            break
    if num>0 or upch>0 or loch>0:
        print('True')
    else:
        print('False')
    if upch>0 or loch>0:
        print('True')
    else:
        print('False')
    if num>0:
        print('True')
    else:
        print('False')
    if loch>0:
        print('True')
    else:
        print('False')
    if upch>0:
        print('True')
    else:
        print('False')
        
