
def secondLargest(list):
    first = list[0]
    second = -1
    for i in range(1, len(list)):
        if list[i] > first:
            second = first
            first = list[i]
        if second < list[i] < first:
            second = list[i]
    return second

print("Enter Element on th Array",end=':')
arr = list(map(int, input().split()))
print(secondLargest(arr))
