from pathlib import Path
# with open("test.txt", "w") as fh:
#     fh.write("first line\nsecond line\nthird line")

# with open("test.txt", "r") as fh:
#     lines = [el.strip() for el in fh.readlines()]

# print(lines)
with open('raw_data.bin', 'wb') as fh:
    fh.write(b'Hello world!')
# Перетворення відносного шляху в абсолютний
# relative_path = Path("Zadachki\M4_r4.py")
# absolute_path = relative_path.absolute()
# print(absolute_path)

# current_working_directory = Path("D:\Project\Dom_Zad\Zadachki\M4_r4.py")
# relative_path = absolute_path.relative_to(current_working_directory)
# print(relative_path)

# original_path = Path("documents/example.txt")

# # Створює новий об'єкт Path з іншим ім'ям файлу
# new_path = original_path.with_name("report.txt")
# original_path.rename(new_path)

# path = Path("./picture")

# # Перевірка існування
# if path.exists():
#     print(f"{path} існує")

# # Перевірка, чи це директорія
# if path.is_dir():
#     print(f"{path} є директорією")

# # Перевірка, чи це файл
# if path.is_file():
#     print(f"{path} є файлом")