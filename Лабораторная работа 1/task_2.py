# TODO Найдите количество книг, которое можно разместить на дискете
one_book = 4 * 25 * 50 * 100
diskette_b = 1.44 * 1024 ** 2
number_of_books = diskette_b / one_book

print("Количество книг, помещающихся на дискету:", round(number_of_books))
