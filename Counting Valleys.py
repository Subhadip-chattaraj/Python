def countingValleys(steps, path):
    # Write your code here
    level=0
    last=0
    vally=0
    for i in path:
        last=level
        if i=='U':
            level+=1
        if i=='D':
            level-=1
        if level==0 and last<0:
            vally+=1
    return vally

if __name__ == '__main__':
    steps = int(input())
    path = input()
    result = countingValleys(steps, path)
    print(result)
