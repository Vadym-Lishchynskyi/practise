import string

print(string.ascii_letters)

print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)
print(string.whitespace)

lead_letters = [97, 110, 98, 102, 114, 116, 118, 78, 48]

a = ''
for i in lead_letters:
    a += f'{chr(i)} '
print(a)

separators = [44, 45, 46, 58, 59]

b = ''
for i in separators:
    b += f'{chr(i)} '
print(b)
