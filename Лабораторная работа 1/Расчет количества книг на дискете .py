# TODO Найдите количество книг, которое можно разместить на дискете

information_volume_of_the_floppy_disk = 1.44  # Размер в Мб
number_of_pages_in_the_book = 100
Number_of_lines_per_page = 50
Number_of_characters_per_line = 25
one_character = 4  # Размер в байтах

# Размер одной книги в байтах
one_book = number_of_pages_in_the_book * Number_of_lines_per_page * Number_of_characters_per_line * one_character

disk_size = information_volume_of_the_floppy_disk * 1024 * 1024  # Размер в байтах


books = int(disk_size // one_book)

print("Количество книг, помещающихся на дискету:", books)
