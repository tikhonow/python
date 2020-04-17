def num_code(i):
    i = i.upper()
    return ord(i) - ord('A') + 1
words = []
while True:
    word = input('Введите слово: ')
    if word == '':
        break
    words.append(word)
print(*sorted(words, key=lambda k: (sum([num_code(i) for i in k]), k)),sep='\n')
