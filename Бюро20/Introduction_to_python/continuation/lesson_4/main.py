def get_shelfs_book(book_num):
    for book in range(book_num):
        shelf_num = int(input("На какую полку положить книгу? "))
        book_name = input("Название книги: ")
        author = input("Имя автора: ")
        book_format = {"book_name": book_name, "author": author}
        shelf_format = "Shelf_{} : {}\n".format(shelf_num, book_format)
        with open("Library.txt", "a", encoding="utf-8") as file:
            file.write(shelf_format)
    return "Книги добавлены"


def read_file_library():
    with open("Library.txt", "r") as file:
        for line in file:
            print(line.strip())



def main():
    print("")
    book_num = int(input("Сколько книг вам нужно добавить? "))
    print(get_shelfs_book(book_num))
    print(read_file_library())

if __name__ == "__main__":
    main()


# Спросил у человека количество книг которое ему нужно добавить
# Спросил у человека на какую полку ему нужно положить книгу
# Спросил у человека название книги
# Спросил у человека автора книги
# Записал название и автора книги на отдельном листочке формат книги
# Записал на отдельном листочке формат полки в которы включает в себя номер полки и содержымое листочка с форматом книги
# Все предыдущие действия(кроме первой строки) повторить заданное количество раз
# С формата полки я выписал в библиотечную картотеку
# После этого я сообщил пользователю то что книги добавлены