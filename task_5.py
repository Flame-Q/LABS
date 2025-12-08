word1 = input("Введите первое слово: ")
word1 = word1.lower()
word2 = input("Введите второе слово: ")
word2 = word2.lower()

if sorted(word1) == sorted(word2):
    print(True)
else:
    print(False)