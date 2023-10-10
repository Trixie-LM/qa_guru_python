import os
from zipfile import ZipFile

import pytest


@pytest.fixture(scope='session', autouse=True)
def create_move_zip():
    # Архивирование документов
    with ZipFile('testzip.zip', 'w') as zf:
        # 1 аргумент - расположение файла, который нужно заархивировать,
        # 2 аргумент - расположение файла в архиве и его название
        zf.write(os.path.abspath('resources/pdf_file.pdf'), 'pdf_file.pdf')
        zf.write(os.path.abspath('resources/xls_file.xls'), 'xls_file.xls')
        zf.write(os.path.abspath('resources/xlsx_file.xlsx'), 'xlsx_file.xlsx')
        zf.write(os.path.abspath('resources/txt_file.txt'), 'txt_file.txt')

    if not os.path.exists('tmp'):
        # Создание папки
        os.mkdir('tmp')

    if os.path.exists('tmp/testzip.zip'):
        # Удаление директории
        os.remove('tmp/testzip.zip')
    # Перемещение файла в указанную директорию
    os.rename('testzip.zip', 'tmp/testzip.zip')

    yield
