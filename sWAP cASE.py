def swap_case(s):
    r=list()
    for i in s:
        if i>='A' and i<='Z':
           r.append(i.lower())
        elif i>='a' and i<='z':
            r.append(i.upper())
        else:
            r.append(i)
    result=""
    return (result.join(r))

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
