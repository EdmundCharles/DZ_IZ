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