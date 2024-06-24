# --------------------- Дерево решений  ---------------------

# Пример дерева решений и условия задачи представлены на сайте

# --------------------- Дерево решений ---------------------

def task():
    age = int(input("Enter your age: "))
    exp = int(input("Enter your exp: "))
    car = input("Enter car type: ")
    dis = int(input("Accidents?: "))
    loc = input("Location?: ")
    if age > 40:
        if loc == "village":
            print("allow")
        else:
            if exp > 10:
                print("allow")
            else:
                print("refuse")
    else:
        if dis == 0:
            print("allow")
        else:
            if car =="minivan":
                print("allow")
            else:
                print("refuse")
    print()


if __name__ == "__main__":
    task()
