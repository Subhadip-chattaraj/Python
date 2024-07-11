import textwrap
def wrap(string, max_width):
    list1 = textwrap.wrap(string,max_width)
    s = "\n".join(list1)
    return s

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
