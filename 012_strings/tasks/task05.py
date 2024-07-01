# --------------------- Парсим цену из html документ ---------------------

# В папке с заданием есть файл ./price_document.html посмотрите его.
# Ваша задача написать функцию которая принимает такой html документ и парсит из него цену.
# Цена находится здесь -
# <span itemprop="price" content="45579">45&nbsp;579&nbsp;AMD</span>
# content="45579" это и есть цена.

# Нужно вернуть целое число в данном случае 45579.

# Не нужно использовать готовые html парсеры. Попробуйте работать на уровне строк.

# Подсказка, используйте функцию find которая находит индекс подстраки в строке:
# word = 'geeks for geeks'
# print(word.find('for'))

# --------------------- Парсим цену из html документ ---------------------

def parse_price_from_document(doc_str):
    start = doc_str.find('"price" content') + 17
    tail = doc_str[start:]
    finish = tail.find(">")

    return tail[:finish-1]


if __name__ == "__main__":
    with open('price_document.html', 'r') as file:
        print(parse_price_from_document(file.read()))
