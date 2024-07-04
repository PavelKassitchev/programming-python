# --------------------- Отфильтровать нечетные элементы в списке ---------------------

# Реализовать функцию filter_odd, на вход список из целых чисел.
# На выходе список из нечетных чисел.

# filter_odd([1,2,3,4,5]) -> [1,3,5]

# --------------------- Отфильтровать нечетные элементы в списке ---------------------

def filter_odd(num_list):
    result_list = []
    for element in num_list:
        if element % 2 == 1:
            result_list.append(element)
    return result_list


if __name__ == "__main__":
    print(filter_odd([1, 2, 3, 4, 5]))
    print(filter_odd([4]))
