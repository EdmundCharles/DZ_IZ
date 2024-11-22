import re 
n = str(input())
n = n.upper()
m = re.match(r'\b[АВЕКМНОРСТУХ]{1}\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}',n)
k =  re.match(r'\b[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}',n)
if m:
    print(f'{m.group(0)} - легковой номер')
elif n:
    print(f'{k.group(0)} - такси')
else :
    print(f'{n} - не номер')