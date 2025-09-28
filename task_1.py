str = input("Введите текст: ")
words = str.split( )
dct = {}
for word in words:
    fix_word = word.lower()
    if fix_word in dct:
        dct[fix_word] += 1
    else:
        dct[fix_word] = 1
print("Сколько раз встречается каждое слово: ")
print(dct)
uniq_word = len(dct)
print("Кол-во уникальных слов: ")
print(uniq_word)
