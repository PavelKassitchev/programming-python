# --------------------- Поиск по базе данных ---------------------

# Есть база данных английских слов, загружается из файла - english_words.txt
# функцией load_word_database() - это спискок слов.
# Пользователь передается шаблон поиска - pattern.

# Пример search_by_pattern("a**l*") -> ['adult', 'apply', 'apple', 'angle']

# Это означает, что слово должно быть из 5 букв, первая 'a', вместо * может быть любая буква.
# На выходе список всех слов, которые подходят под этот паттерн.

# --------------------- Поиск по базе данных ---------------------

def load_word_database():
    with open('english_words.txt', 'r') as file:
        list_words = file.readlines()
        for index, word in enumerate(list_words):
            list_words[index] = word.lower().rstrip()
        return list_words


def search_by_pattern(pattern):
    word_database = load_word_database()
    print(len(pattern))
    print(word_database)
    for word in word_database[:]:
        print("checking " + word)
        if len(word) != len(pattern):
            word_database.remove(word)
            print("removing " + word)
        else:
            for i in range(len(word)):
                if pattern[i] != '*' and pattern[i] != word[i]:
                    word_database.remove(word)
                    print("carefully removing " + word)
                    break
    return word_database





if __name__ == "__main__":
    print(search_by_pattern("a**l*"))
   # print(search_by_pattern("test"))
   # print(search_by_pattern("t**"))
