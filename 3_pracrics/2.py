#Задача №3764. Частотный анализ
text = {}
for word in input().split():
    text[word] = text.get(word, 0) + 1
for i in sorted(text.items(), key=lambda x:(-x[1],x[0])):
    print(i[0])