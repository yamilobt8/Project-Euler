def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
total_sundays = 0
current_day = 2

for year in range(1901, 2001):
    for month in range(12):
        if current_day % 7 == 0:
            total_sundays += 1
        days_in_month = month_days[month]
        if month == 1 and is_leap(year):
            days_in_month += 1

        current_day += days_in_month
print(f'Total Sundays is: {total_sundays}') # 171

