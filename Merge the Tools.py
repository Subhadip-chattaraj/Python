def merge_the_tools(string, k):
    # your code goes here
    substrings = [string[i: i+k] for i in range(0, len(string), k)]
    for i in substrings:
        for j in i:
            m=i.count(j)
            while m!=1:
                if
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
