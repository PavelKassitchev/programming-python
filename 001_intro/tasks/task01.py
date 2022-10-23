# --------------------- Квадратный корень ---------------------

# Задание: рассчитывает квдратный корень, по алгоритму из первого урока
# !!! Внимание, данное задание уже решено и не нужно его изменять, оно для демонстрационных целей

# --------------------- Квадратный корень ---------------------

def task():
    x = int(input('Введите x: '))
    eps = 1e-6
    y = 1
    while abs(y * y - x) >= eps:
        y = (y + x / y) / 2
    print(y)


if __name__ == "__main__":
    task()