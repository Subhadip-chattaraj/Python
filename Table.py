from prettytable import PrettyTable

table=PrettyTable(["Student","Class","Roll no","Age"])
table.add_row(["Sujoy","X","76","16"])
table.add_row(["Somnath","X","75","16"])
table.add_row(["Ajoy","X","73","16"])
table.add_row(["Akash","X","70","16"])
table.add_row(["Sanjoy","X","71","16"])
table.add_row(["Bikash","X","72","16"])

print(table)
