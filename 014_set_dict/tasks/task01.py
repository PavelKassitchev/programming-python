# --------------------- Найти n самых частых значений в списке ---------------------

# Реализовать функцию find_n_most_common_values которая на вход принимает массив целых чисел
# и параметр n, целое число больше 0, которое означает сколько значений нужно вернуть из функции.
# Функция возвращает список из n самых частых значений, отсортированных от большего к меньшему.

# find_n_most_common_values([5,5,5,3,3,3,3,1,2,2], 3) -> [3, 5, 2]

# --------------------- Найти n самых частых значений в списке ---------------------

def find_n_most_common_values(num_list, n):
    val_dict = {}
    for k in num_list:
        if k in val_dict:
            val_dict[k] += 1
        else:
            val_dict[k] = 1
    listing = sorted(val_dict.items(), key=lambda x:x[1], reverse = True)
    temp_list = listing[0 : n]
    return [i[0] for i in temp_list]


if __name__ == "__main__":
    print(find_n_most_common_values([5, 5, 5, 3, 3, 3, 3, 1, 2, 2], 3))
