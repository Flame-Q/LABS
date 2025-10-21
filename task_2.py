str = input("Введите строку: ")

str = str.lower()
new_str = str.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "")
print (new_str)