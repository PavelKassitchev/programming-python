# --------------------- Числа Фибоначчи ---------------------

# Реализуйте функцию fibonacci
# На вход передается номер последовательности, строго больше 0
# На выходе нужно вернуть значение последовательности

# Последовательность Фибоначчи - это
# F_1 = 0
# F_2 = 1
# F_N = F_(N-1) + F_(N-2)
# т.е. каждый следущий член последовательнсоти - это сумма двух предыдущих

# Пример последовательности: 0 1 1 2 3 5 8 13 21 34
# если функцию вызовут fibonacci(7) то она вернет 8

# --------------------- Числа Фибоначчи ---------------------

def fibonacci(n):
    f_prev_prev = 0
    f_prev = 1

    if n == 1:
        return f_prev_prev
    elif n == 2:
        return f_prev

    f_n = 0
    for i in range(n-2):
        f_n = f_prev_prev + f_prev
        f_prev_prev = f_prev
        f_prev = f_n

    return f_n

