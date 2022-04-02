week_hours = 40  # Стандартна работна седмица.
hours = float(input("Изработени часове: "))
hour_rate = float(input("Заплащане на час: "))


def func_hours(h, r):
    h_r = h * r
    return h_r


if hours <= week_hours:
    salary = func_hours(hours, hour_rate)
else:
    over_hours = hours - week_hours
    over_rate = hour_rate + (0.5 * hour_rate)
    over_salary = func_hours(over_hours, over_rate)
    salary = func_hours(week_hours, hour_rate) + over_salary

print(f"Седмичната заплата е: {salary:.2f}")
