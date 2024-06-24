# --------------------- Накопления на дом #2  ---------------------

# Условия задачи на сайте.

# --------------------- Накопления на дом #2 ---------------------

def task():
    cost = int(input("Enter cost: "))
    price = cost / 4
    salary = int(input("Enter salary: "))
    percent = int(input("Enter percentage: "))
    if percent < 1 or percent > 100:
        print('wrong percent')
        exit(-1)
    growth = int(input("Enter growth: "))
    if growth < 1 or percent > 100:
        print('wrong growth')
        exit(-1)
    interest = 0.04
    months = 1;
    amount = 0;
    while True:
        amount = amount + amount * interest / 12
        if months != 1 and (months - 1) % 6 == 0:
            salary += salary / 100 * growth
        amount = amount + (salary / 12) * percent / 100
        if amount >= price:
            break
        months += 1

    print("Number of months:", months)


if __name__ == "__main__":
    task()
