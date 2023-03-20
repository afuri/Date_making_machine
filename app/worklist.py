import datetime as dt


def get_workdays_list(workdays):
    delta_time1 = dt.timedelta(days=1)
    current_date = dt.date(2022, 8, 31)
    date_end = dt.date(2023, 5, 25)
    holidays_2023 = tuple(dt.date(2023, 1, i) for i in range(1, 9)) + tuple(dt.date(2023, 3, i) for i in range(24,32)) + (dt.date(2023, 2, 23), dt.date(2023, 2, 24), dt.date(2023, 3, 8), dt.date(2023, 4, 1), dt.date(2023, 4, 2), dt.date(2023, 5, 1), dt.date(2023, 5, 8), dt.date(2023, 5, 9))
    holidays_2022 = tuple(dt.date(2022, 10, i) for i in range(28,32)) + tuple(dt.date(2022, 11, i) for i in range(1,7)) + (dt.date(2022, 12, 28), dt.date(2022, 12, 29), dt.date(2023, 12, 30), dt.date(2022, 12, 31))
    holidays = holidays_2022 + holidays_2023
    workdays_list = []
    i = 1
    weekdays = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']

    while current_date != date_end:
        current_date += delta_time1
        con_1 = current_date.weekday() in workdays.keys()
        con_2 = current_date not in holidays
        if con_1 and con_2:
            for _ in range(int(workdays[current_date.weekday()])):
                workdays_list.append((weekdays[current_date.weekday()], current_date.strftime('%d.%m')))
    return workdays_list