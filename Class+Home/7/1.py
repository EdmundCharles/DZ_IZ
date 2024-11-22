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