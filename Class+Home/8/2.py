import re
file = open(r'c:\Users\ilyad\OneDrive\Документы\idiot.txt',
            'r', encoding='utf-8')
print(
    len(re.findall(r'\b[А-Яа-яЁё]+[-]?[А-Яа-яЁё]+\b', ",".join(file.readlines()))))
