# --------------------- Максимальное и минимальное число в списке ---------------------

# Разработать функции по поиску максимального и минимального числа в списке по модулю(abs)
# На вход список из целых чисел, на выходе целое число или None.
# Пример:
# max_abs([-100, 15, 50]) -> -100
# max_abs([-100, 15, 50]) -> 15

# Если список пустой, то вернуть None

# --------------------- Максимальное и минимальное число в списке ---------------------

def max_abs(num_list):
    if len(num_list) == 0:
        return None
    max_val = 0
    val = 0
    for el in num_list:
        if abs(el) > abs(max_val):
            max_val = abs(el)
            val = el
    return val


def min_abs(num_list):
    if len(num_list) == 0:
        return None
    min_val = abs(num_list[0])
    val = num_list[0]
    for el in num_list:
        if abs(el) < abs(min_val):
            min_val = abs(el)
            val = el
    return val


if __name__ == "__main__":
    print(max_abs([-100, 15, 50]))
    print(min_abs([-100, 15, 50]))
    print(min_abs([]))

