def print_full_name(first, last):
    # Write your code here
    name=first+" "+last
    print("Hello ",name,"! You just delved into python.",sep="")
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
