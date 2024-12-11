#Task1
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
#Task2
import re
file = open(r'c:\Users\ilyad\OneDrive\Документы\idiot.txt',
            'r', encoding='utf-8')
print(
    len(re.findall(r'\b[А-Яа-яЁё]+[-]?[А-Яа-яЁё]+\b', ",".join(file.readlines()))))

#Task3
import re
print(re.sub(r'[0-2][0-9]:[0-5][0-9]:?([0-5][0-9])?', r'(TBD)',
      'Уважаемые! Если вы к 09:00 не вернёте чемодан, то уже в 09:00:01 я за себя не отвечаю.', count=0))

#Task4
import re
print(re.findall(r'(?:[А-Я]{2,} ?)+',str(input())))