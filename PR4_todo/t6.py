from prettytable import PrettyTable
import unicodedata

table = PrettyTable()

table.field_names = ["Код", "Символ", "Категорія Юнікода", "Класи"]

for i in range(90, 100):
    try:
        table.add_row([chr(i).encode('utf-8'), chr(i), unicodedata.name(chr(i)), unicodedata.category(chr(i))])
    except ValueError:
        table.add_row([chr(i).encode('utf-8'), chr(i), None, unicodedata.category(chr(i))])

print(table)

