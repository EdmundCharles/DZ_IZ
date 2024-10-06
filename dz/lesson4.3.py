s = 'аллея бенго авляция сокет адгезия сон авиация кукуха абразия едет'
s = s.split(" ")
glagol = []
for i in s:
    if i.startswith("а") and i.endswith("я"):
        glagol.append(i)
print(*glagol)
