from hash1_4 import *


bookName = ["A", "AA", "AAA", "AAAA"]
bookU = ["49 мм x 17 мм", "50.5 мм x 14.5 мм", "44.5 мм x 10.5 мм", "42.5 мм x 8.3 мм"]

book = {}

print("Функция 1")
for i in range(len(bookName)):
    book[hash_1(bookName[i])] = bookU[i]
    print(book)
    book.clear()


print("Функция 2")
for i in range(len(bookName)):
    book[hash_2(bookName[i])] = bookU[i]
    print(book)
    book.clear()


print("Функция 3")
for i in range(len(bookName)):
    book[hash_3(bookName[i])] = bookU[i]
    print(book)
    book.clear()


print("Функция 4")
for i in range(len(bookName)):
    book[hash_4(bookName[i], 10)] = bookU[i]
    print(book)
    book.clear()
