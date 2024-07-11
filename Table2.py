from prettytable import PrettyTable

num_column=int(input("Enter Number of column:"))
l=[]

for i in range(num_column):
    l.append(input("Enter name of the column:"))

table=PrettyTable(l)

num_row=int(input("Enter num of rows:"))

for i in range(num_row):
    m=[]
    for j in l:
        m.append(input(j+":"))
    table.add_row(m)

print(table)
