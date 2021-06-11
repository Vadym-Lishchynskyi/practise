from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]

for i in range(32, 192, 16):
    a = [f'{hex(i//10)}']
    for j in range(0, 16):
        a.append(f' {chr(i+j)} ')
    table.add_row(a)

for i in range(1024, 1184, 16):
    a = [f'{hex(i//10)}']
    for j in range(0, 16):
        a.append(chr(i+j))
    table.add_row(a)

for i in range(9472, 9712, 16):
    a = [f'{hex(i//10)}']
    for j in range(0, 16):
        a.append(chr(i+j))
    table.add_row(a)

print(table)
