str = input("Введите текст: ")
words = str.split( )
dct = {}
for word in words:
    if word in dct:
        dct[word] += 1
    else:
        dct[word] = 1
print("Сколько раз встречается каждое слово: ")
print(dct)
uniq_word = len(dct)
print("Кол-во уникальных слов: ")
print(uniq_word)
