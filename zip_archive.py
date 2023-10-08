from zipfile import ZipFile


with ZipFile('resources/XXX') as zip_file:

    # Узнать список файлов
    print(zip_file.namelist())

    # Прочитать файл
    text = zip_file.read('test.txt')
    print(text)

    # Извлечь файл
    zip_file.extract('test.txt')
