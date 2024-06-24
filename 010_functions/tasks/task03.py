# --------------------- Найти месяц по номеру дня в году ---------------------

# Реализуйте функцию get_month_by_day_number
# На вход передается номер дня в году и параметр високосный ли год
# На выходе нужно вернуть название месяца

# В обычном году 365 дней, а в високосном 366
# Если номер дня будет меньше ил равен нулю или больше максимального количества дней,
# то нужно вывести "incorrect day number"

# Иначе вывести значение месяца с большой буквы.

# Таблица месяцев.

# January - 31 days
# February - 28 days in a common year and 29 days in leap years
# March - 31 days
# April - 30 days
# May - 31 days
# June - 30 days
# July - 31 days
# August - 31 days
# September - 30 days
# October - 31 days
# November - 30 days
# December - 31 days


# --------------------- Найти месяц по номеру дня в году ---------------------

def get_month_by_day_number(day_number, is_leap_year):
    if day_number < 1 or day_number > 366 or (day_number == 366 and is_leap_year == False):
        return "incorrect day number"
    if day_number <= 31:
        return "January"
    if day_number <= 59 or (day_number == 60 and is_leap_year == True):
        return "February"
    if day_number <= 90 or (day_number == 91 and is_leap_year == True):
        return "March"
    if day_number <= 120 or (day_number == 121 and is_leap_year == True):
        return "April"
    if day_number <= 151 or (day_number == 152 and is_leap_year == True):
        return "May"
    if day_number <= 181 or (day_number == 182 and is_leap_year == True):
        return "June"
    if day_number <= 212 or (day_number == 213 and is_leap_year == True):
        return "July"
    if day_number <= 243 or (day_number == 244 and is_leap_year == True):
        return "August"
    if day_number <= 273 or (day_number == 274 and is_leap_year == True):
        return "September"
    if day_number <= 304 or (day_number == 305 and is_leap_year == True):
        return "October"
    if day_number <= 334 or (day_number == 335 and is_leap_year == True):
        return "November"
    return "December"


if __name__ == "__main__":
    print(get_month_by_day_number(60, is_leap_year=True))
    print(get_month_by_day_number(60, is_leap_year=False))
