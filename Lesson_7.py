#Task1
def read_last(lines, file):
  abstract_file = open(file, 'r', encoding='utf-8')
  rows = abstract_file.readlines()
  for row in rows[-lines:]:
    print(row)
PATH_FILE = "C:\lrticle.txt"
n = int(input('Введите целое число строк, которые хотите видеть \n'))
file = open(PATH_FILE,'r',encoding='utf-8')
rn = len(file.readlines())
if n > 0 and n < rn :
    read_last(n,PATH_FILE)
#Task2
import os
def print_docs(directory):
    files = os.walk(directory)
    for catalog in files:
        print(f'Папка {catalog[0]} содержит:')
        print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
        print(f'Файлы: {", ".join([file for file in catalog[2]])}')
        print('-' * 40)
print_docs('c:\Program Files\Betaflight\Betaflight-Configurator')
#Task3
def longest_words(file):
    text = open(file,encoding='utf-8')
    words = text.read().split()
    maxlen = len(max(words, key=len))
    final = []
    for i in words :
        if len(i) == maxlen:
            final.append(i)
    return final
PATH_FILE = "C:\lrticle.txt"
print(*longest_words(PATH_FILE))
#Task4
import os
name = str(input("Name your file\n"))+'.txt'
file = open(name,'w')
flag = 1
while flag == 1 :
    n = str(input('Enter stroka\n'))
    file.write(n + '\n')
    if len(n) == 0:
        flag = 0
file.close()
