def read_last(lines, file):
  abstract_file = open(file, 'r', encoding='utf-8')
  rows = abstract_file.readlines()
  for row in rows[lines:]:
    print(row)

PATH_FILE = r'C:\lrticle.txt'

n = int(input('Input int positive number: '))
file = open(PATH_FILE, 'r', encoding='utf-8')
rows_number = len(file.readlines()) #Получаем объем файла в строках

if n > 0 and n < rows_number:
  read_last(n, PATH_FILE)