

def hash_1(book_name):
    return 1


def hash_2(book_name):
    return len(book_name)


def hash_3(book_name):
    if book_name[0] != '':
        return book_name[0]
    else:
        return "Пусто"


def hash_4(book_name, book_len):
    hash_value = sum(ord(char) for char in book_name if char.isalpha()) % book_len
    return hash_value
