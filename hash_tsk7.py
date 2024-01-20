from hash1_4 import *


bookName = ["Maus", "Fun Home", "Watchmen"]
bookAuthor = ["Fred Perry", "Adolf Filter", "Vladimir Utkin", "Fedor Dostoevski"]

book = {}

print("Функция 1")
for i in range(len(bookName)):
    book[hash_1(bookName[i])] = bookAuthor[i]
    print(book)
    book.clear()


print("Функция 2")
for i in range(len(bookName)):
    book[hash_2(bookName[i])] = bookAuthor[i]
    print(book)
    book.clear()


print("Функция 3")
for i in range(len(bookName)):
    book[hash_3(bookName[i])] = bookAuthor[i]
    print(book)
    book.clear()


print("Функция 4")
for i in range(len(bookName)):
    book[hash_4(bookName[i], 10)] = bookAuthor[i]
    print(book)
    book.clear()
