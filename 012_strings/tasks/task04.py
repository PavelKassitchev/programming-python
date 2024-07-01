# --------------------- Шифр ---------------------

# Кодируем английский алфавит маленьких букв 'a'->'z'

# Функция encode - принимает на вход строку и шифрует ее.
# Шифр по правилу:
# каждую букву мы сдвигаем на 1. 'a'->'b', ... , 'c' -> 'd', ...., 'z'->'a'
# на выходе зашифрованная строка.

# Функция decode принимает на вход зашифровонную строку и раскодирует ее.

# Пример:
# encode("apple") -> "bqqmf"
# decode("bqqmf") -> "apple"

# --------------------- Шифр ---------------------


def encode(original_str):
    encoded_str = ''
    for c in original_str:
        encoded_str += chr(ord(c) + 1)
    return encoded_str

def decode(encoded_str):
    decoded_str = ''
    for c in encoded_str:
        decoded_str += chr(ord(c) - 1)
    return decoded_str


if __name__ == "__main__":
    print(encode("apple"))
    print(decode("bqqmf"))
