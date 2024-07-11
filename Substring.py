def count_substring(string, sub_string):
    score=0
    for i in range(len(string)):
        c = 0
        if string[i]==sub_string[0]:
            k=i
            if k>=len(string)-1:
                    break
            for j in range(len(sub_string)):
                if string[k]==sub_string[j]:
                    c+=1
                else:
                    break
                k+=1
                if k>len(string)-1:
                    break
        if c==len(sub_string):
            score+=1
    return score

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
