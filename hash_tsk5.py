from hash1_4 import *


bookName = ["Esther", "Ben", "Bob", "Dan"]
bookPhone = ["6-943-8974-018", "8-943-8974-018", "4-943-8974-018", "1-943-8974-018"]
book = {}

print("Функция 1")
for i in range(len(bookName)):
    book[hash_1(bookName[i])] = bookPhone[i]
    print(book)
    book.clear()


print("Функция 2")
for i in range(len(bookName)):
    book[hash_2(bookName[i])] = bookPhone[i]
    print(book)
    book.clear()


print("Функция 3")
for i in range(len(bookName)):
    book[hash_3(bookName[i])] = bookPhone[i]
    print(book)
    book.clear()


print("Функция 4")
for i in range(len(bookName)):
    book[hash_4(bookName[i], 10)] = bookPhone[i]
    print(book)
    book.clear()
