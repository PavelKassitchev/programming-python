# --------------------- trim ---------------------

# Реализовать функцию trim.
# На вход передается строка.
# На выходе строка без пробелов в начале и в конце.
# Пример trim("     Test  string     ") -> "Test  string"

# --------------------- trim ---------------------

def trim(str):

    left = 0
    right = len(str)
    for c in str:
        if c == ' ':
            left += 1
        else:
            break
    for c in str[::-1]:
        if c == ' ':
            right -= 1
        else:
            break
    return str[left:right]


if __name__ == "__main__":
    print(trim("     Test  string     "))
