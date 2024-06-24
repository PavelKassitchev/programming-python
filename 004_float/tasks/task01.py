# --------------------- Отнсоительность расстояний  ---------------------
import math


# условия задачи описаны в уроке

# --------------------- Отнсоительность расстояний ---------------------

def task():
    c = 299792458
    L0 = float(input('Enter length: '))
    v = float(input('Enter velocity: '))
    Lr = L0 * math.sqrt(1 - v**2 / c**2)
    L = round(Lr, 8)
    print(L)


if __name__ == "__main__":
    task()
