from pypdf import PdfReader


reader = PdfReader('resources/Книга по психологии человека.pdf')
number_of_pages = len(reader.pages)
print(number_of_pages)

# Вывод текста со страницы
page = reader.pages[1]
text = page.extractText()
print(text)
